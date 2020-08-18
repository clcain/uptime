# Uptime

A simple and configurable uptime monitor application written in Python. This application reads a YAML config file that specifies endpoints to check. It then schedules itself to run every 1 second and check if any endpoints need to be assessed. If any endpoints are ready to be checked, it will run a check on each of them. The results are output to a CSV file that is designed to be easy to parse.

See the example `config.yaml` for configuration syntax.

## Supported endpoints

Currently, only the HTTP endpoint is supported.

### HTTP

An HTTP endpoint has a target URL as well as an expected HTTP status code. If the status code matches the expected code, the check will be considered successful.
