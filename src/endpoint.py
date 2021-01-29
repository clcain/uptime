import datetime
import ping3
import requests


class Endpoint:

    def __init__(self, dict):
        self.name = dict.get('name')
        self.log_file = dict.get('log_file')
        self.type = dict.get('type')
        self.address = dict.get('address')
        self.url = dict.get('url')
        self.http_success_code = dict.get('http_success_code')
        self.refresh = dict.get('refresh')
        self.tick = 0

    def __str__(self):
        return(f'Endpoint (name="{self.name}", type={self.type}, url="{self.url}", refresh={self.refresh})')

    def check(self, config):
        self.tick -= 1
        if self.tick > 0:
            return
        else:
            self.tick = self.refresh

        if self.type == 'http':
            print(f'Checking endpoint: {self.name}')
            start_time = datetime.datetime.now().timestamp()
            r = requests.get(self.url)
            end_time = datetime.datetime.now().timestamp()
            latency = end_time - start_time
            print(f'Status code: {r.status_code}')
            result = r.status_code == self.http_success_code
            self.report_result(result, latency)

        elif self.type == 'ping':
            print(f'Checking endpoint: {self.name}')
            latency = ping3.ping(self.address)
            print(f'Ping time: {latency} ms')
            self.report_result(1, latency)

    def report_result(self, result, latency):
        with open(self.log_file, 'a') as f:
            f.write(f'{datetime.datetime.now().timestamp()},{result},{latency}\n')
            f.close()
