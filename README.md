# Disclaimer

Usage of this tool for educational or authorized use only and at your own responsibility.

# Description

Performs enumeration of subdomains and directories.

# Usage

`main.py [-h] --mode {dir,sub} --address ADDRESS --list LIST [--port PORT] [--timeout TIMEOUT]`

| Option | Short | Type | Default | Description |
|---|---|---|---|---|
|--mode | -m | String | - | dir for directory enumeration, sub for subdomain enumeration |
|--address | -a | String | - | The url or IP address |
| --list | -l | String | - | Path to enumeration list |
| --port | -p | Int | 80 | The target port |
| --timeout | -t | Int | 0.01 |  Request timeout in seconds |

# Example

The following command starts directory enumeration for  **http://localhost** on port **8080** and uses  **list.txt** as wordlist:

`python3 main.py -m dir -a http://localhost -p 8080 -l list.txt` 

For each line in **list.txt** there will be an output on the console with the response code e.g.:

```
Target: http://localhost:8080/admin - Code: 404
Target: http://localhost:8080/local - Code: 200
Target: http://localhost:8080/test  - Code: 404
```


# License

MIT