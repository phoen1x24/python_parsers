import requests
from bs4 import BeautifulSoup
from proxy_config import login, password, proxy
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9'
}

proxies = {
    'https': f'http://{login}:{password}@{proxy}'
}

def get_data(url):
    response = requests.get(url=url, headers=headers, proxies=proxies)
    print(response)

def main():
    get_data(url='https://www.bls.gov/regions/midwest/data/AverageEnergyPrices_SelectedAreas_Table.htm')


if __name__ == '__main__':
    main()
