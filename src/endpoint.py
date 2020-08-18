import datetime
import requests


class Endpoint:

    def __init__(self, dict):
        self.name = dict['name']
        self.log_file = dict['log_file']
        self.type = dict['type']
        self.url = dict['url']
        self.http_success_code = dict['http_success_code']
        self.refresh = dict['refresh']
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
            print(r.status_code)
            result = r.status_code == self.http_success_code
            self.report_result(result, latency)

    def report_result(self, result, latency):
        with open(self.log_file, 'a') as f:
            f.write(f'{datetime.datetime.now().timestamp()},{result},{latency}\n')
            f.close()
