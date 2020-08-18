import sched
import time
import yaml

from utils import *

from endpoint import Endpoint


def parse_config():
    with open(r'config.yaml') as f:
        config = yaml.load(f, Loader=yaml.FullLoader)
        return config


def parse_endpoints(config):
    endpoints = []
    for endpoint_dict in config['endpoints']:
        endpoints.append(Endpoint(endpoint_dict))
    return endpoints


def check_endpoints(config, endpoints):
    for endpoint in endpoints:
        endpoint.check(config)


scheduler = sched.scheduler(time.time, time.sleep)


def event_loop(scheduler, config, endpoints):
    scheduler.enter(1, 1, event_loop, (scheduler, config, endpoints))
    print_log('Checking endpoints.')
    check_endpoints(config, endpoints)


def main():
    print_log('Initializing uptime.')
    print_log('Parsing config.')
    config = parse_config()
    print(config)
    endpoints = parse_endpoints(config)
    print_log(f'Beginning endpoint check with {len(endpoints)} endpoints.')
    for endpoint in endpoints:
        print(f' - {str(endpoint)}')
    scheduler.enter(1, 1, event_loop, (scheduler, config, endpoints))
    scheduler.run()


main()
