import csv
import time
from base import user_log_collection
import argparse

csv_data = [
    ['Date', 'Time', 'User', 'Action']
]

if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description='user action log'
    )

    parser.add_argument('-d', '--date', type=str, default=time.strftime('%Y-%m-%d', time.localtime()))
