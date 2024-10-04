import requests
import concurrent.futures
import time
import logging

# URL to check
url = "https://www.google.com"
# Timeout for the request (in seconds)
timeout = 3
# Number of threads to use
threads = 3
# Maximum number of retries for each proxy
max_retries = 1
# File containing the list of proxies
file_path = r"D:\proxys.txt"


logging.basicConfig(
    format="%(levelname)s - %(message)s",
    level=logging.INFO
)
logger = logging.getLogger(__name__)

# Read list of proxies from file
def read_proxies_from_file(file_path):
    with open(file_path, "r") as file:
        return [line.strip() for line in file]

# Prepend "http://" to each proxy read from the file
proxies_list = [f"http://{proxy}" for proxy in read_proxies_from_file(file_path)]

# List to store successful proxies
successful_proxies = []

# Counter for scanned proxies
scanned_count = 0

def check_proxy(proxy, retries=0):
    global scanned_count
    try:
        proxies = {
            "https": proxy,
        }
        # Send a GET request to the URL using the proxy
        response = requests.get(url, proxies=proxies, timeout=timeout)
        # Check if the response status code is 200 (OK)
        if response.status_code == 200:
            logger.info(f"[+] Proxy works: {proxy}")
            successful_proxies.append(proxy.replace("http://", ""))
            scanned_count += 1
            logger.info(f"Proxies scanned: {scanned_count}/{len(proxies_list)}")
    except requests.RequestException:
        # Retry if the proxy fails and the maximum retries haven't been reached
        if retries < max_retries:
            time.sleep(1)  # Optional: add a delay between retries
            check_proxy(proxy, retries + 1)
        else:
            logger.info(f"[-] Proxy failed after {max_retries} retries: {proxy}")
            scanned_count += 1
            logger.info(f"Proxies scanned: {scanned_count}/{len(proxies_list)}")


def main():
    # Use ThreadPoolExecutor to check proxies concurrently
    with concurrent.futures.ThreadPoolExecutor(max_workers=threads) as executor:
        # Submit each proxy to be checked by a thread
        executor.map(check_proxy, proxies_list)
    
    # Print all successful proxies
    if successful_proxies:
        print("\nSuccessful proxies:")
        for proxy in successful_proxies:
            print(proxy)
    
    # Print total number of proxies scanned
    print(f"\nTotal proxies scanned: {scanned_count}")

if __name__ == "__main__":
    main()
