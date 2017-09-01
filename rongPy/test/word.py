import requests
from bs4 import BeautifulSoup
import operator
import re

testUrl = r"http://library.duke.edu/digitalcollections/gamble_glass_lantern_slides/"

def start(url):
    word_list = []
    source_code = requests.get(url).text
    soup = BeautifulSoup(source_code, "html.parser")
    for post_text in soup.findAll('li', {'class':re.compile("^grid_3*")}):
        content = post_text.text
        words = content.lower().split()
        for each_word in words:
            word_list.append(each_word)
    clean_up_list(word_list)
    
def clean_up_list(word_list):
    clean_word_list = []
    for word in word_list:
        word = re.sub('\W',"",word)
        if len(word) > 0:
            clean_word_list.append(word)
    create_dict(clean_word_list)
    
def create_dict(clean_word_list):
    word_count = {}
    for word in clean_word_list:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1
    for key, value in sorted(word_count.items(), key=operator.itemgetter(0)):
        print(key, value)
    
start(testUrl)
    