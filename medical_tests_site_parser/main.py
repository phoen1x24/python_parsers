import requests
import os
import csv
import json
from datetime import datetime



def collect_data():
    proxies = {
        'https': f'http://{os.getenv("ZiqWD1sB")}:{os.getenv("JNBe2hnX")}@213.209.134.250:62487'
    }
    t_date = datetime.now().strftime('%d_%m_%Y')



def main():
    collect_data()

if __name__ == '__main__':
    main()

