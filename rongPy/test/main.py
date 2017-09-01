'''
from urllib import request

goog_url = 'http://www.google.com/finance/historical?q=NYSE%3ATAL&ei=MimdWdnWH9jCeueCpcAI&output=csv'

def download_stock_data(csv_url):
    response = request.urlopen(csv_url)
    csv = response.read().decode("utf-8-sig")
    csv_str = str(csv)
    lines = csv_str.split(r'\n')
    dest_url = r'goog.csv'
    fw = open(dest_url, 'w')
    for line in lines:
        fw.write(line + '\n')
    fw.close()
    
download_stock_data(goog_url)
'''
'''
fw = open('sample.txt', 'w')
fw.write('Writing some stuff in my text file\n')
fw.write('I like bacon\n')
fw.close()
from urllib.request import urlretrieve

fr = open('sample.txt', 'r')
text = fr.read()
print(text)
fr.close()
'''

'''
import random
import urllib.request

import beautifulscraper

def download_web_image(url):
    name= random.randrange(1, 1000)
    full_name = str(name) + ".jpg"
    urllib.request.urlretrieve(url, full_name)
    
download_web_image("https://www.google.com/images/branding/googlelogo/1x/googlelogo_color_272x92dp.png")
'''