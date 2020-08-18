import datetime


def print_log(s):
    print(f'[{datetime.datetime.now().isoformat()}] {str(s)}')
