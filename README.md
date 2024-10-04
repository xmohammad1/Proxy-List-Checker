# Proxy Checker

This project is a Python script that allows you to check the validity of a list of proxies by sending requests to a specified URL. It utilizes multithreading to speed up the proxy-checking process, allowing for efficient scanning of large lists of proxies.

## Features
- Checks a list of proxies concurrently using a configurable number of threads.
- Retries each proxy up to a configurable maximum number of retries if a request fails.
- Logs the status of each proxy (whether it is working or failed).
- Outputs a list of successful proxies.

## Requirements
- Python 3.x
- `requests` library

To install the `requests` library, run the following command:

```sh
pip install requests
```

## Usage
1. Clone or download the repository to your local machine.
2. Create a text file (`proxys.txt`) containing the list of proxies you want to check, with each proxy on a new line in the following format:
   ```
   ip:port
   ip:port
   ...
   ```
3. Edit the script to specify the correct file path to your proxy list (`file_path`) and adjust the number of threads (`threads`), request timeout (`timeout`), and maximum retries (`max_retries`) as needed.
4. Run the script using the following command:

```sh
python proxy_checker.py
```

### Example Proxy File (`proxys.txt`)
```
123.123.123.123:8080
111.111.111.111:3128
222.222.222.222:1080
```

## Configuration
The script contains several configurable parameters:
- **`url`**: The URL to which the request will be sent to check if a proxy is working (default: Google).
- **`timeout`**: The request timeout in seconds.
- **`threads`**: The number of threads to use for concurrent requests (default: 3).
- **`max_retries`**: The maximum number of retries for each proxy if the initial request fails (default: 1).

## Logging
The script uses the built-in `logging` module to provide informative messages during execution. These messages include whether a proxy works or fails, and the progress of the scanning process.

## Code Explanation
- **`read_proxies_from_file(file_path)`**: Reads the list of proxies from the specified file and returns it as a list.
- **`check_proxy(proxy, retries=0)`**: Sends a request to the specified URL using the provided proxy. If the request is successful, the proxy is added to the list of successful proxies. Otherwise, the function retries the request up to `max_retries` times.
- **`main()`**: The main function that uses `ThreadPoolExecutor` to concurrently check proxies using multiple threads.

## Output
- The script outputs a list of successful proxies at the end of execution.
- It also prints the total number of proxies scanned.

## License
This project is open source and available under the MIT License.

## Contributing
Feel free to open an issue or submit a pull request if you want to contribute to this project.

## Disclaimer
Please note that some proxies may be used for malicious activities. Make sure to use proxies responsibly and abide by the legal requirements in your country.
