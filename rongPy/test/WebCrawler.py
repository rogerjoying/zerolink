from bs4 import BeautifulSoup
import requests

def pic_spider(max_pages):
    page = 1
    while page <= max_pages:
        url = r'http://library.duke.edu/digitalcollections/gamble_RL_10074_LS_00'
        print(url + str(page).zfill(2))
        source_code = requests.get(url + str(page).zfill(2), headers={'Accept-Encoding': 'identity'})
        plain_text = source_code.text
        soup = BeautifulSoup(plain_text, 'html.parser')
        for link in soup.findAll('a', {'onclick':r"ga('send', 'event', 'Item Options', 'All Sizes', 'Image Direct Click');"}):
            href = link.get('href')
            print(href)
            get_picTiltle(href)
        page += 1

def get_picTiltle(pic_url):
    source_code = requests.get("http://library.duke.edu" + pic_url, headers={'Accept-Encoding': 'identity'})
    plain_text = source_code.text
    soup = BeautifulSoup(plain_text, 'html.parser')
    for item_name in soup.findAll('title'):
        print(item_name)

pic_spider(10)