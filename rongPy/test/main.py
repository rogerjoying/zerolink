from operator import attrgetter

class User:
    
    def __init__(self, x, y):
        self.name = x
        self.user_id = y
        
    def __repr__(self):
        return self.name + " : " + str(self.user_id)
    
users = [
    User('Bucky', 43),
    User('Sally', 5),
    User('Tuna', 61),
    User('Brian', 2),
    User('Joby', 77),
    User('Amanda', 9)
]

for user in users:
    print(user.__str__())

print('-----')
for user in sorted(users, key = attrgetter('user_id')):
    print(user)

'''
from operator import itemgetter

users = [
    {'fname': 'Bucky', 'lname' : 'Roberts'},
    {'fname': 'Tom', 'lname' : 'Roberts'},
    {'fname': 'Bernie', 'lname' : 'Zunks'},
    {'fname': 'Jenna', 'lname' : 'Hayes'},
    {'fname': 'Sally', 'lname' : 'Joness'},
    {'fname': 'Amanda', 'lname' : 'Roberts'},
    {'fname': 'Tom', 'lname' : 'Williams'},
    {'fname': 'Dean', 'lname' : 'Hayes'},
    {'fname': 'Bernie', 'lname' : 'Barbies'},
    {'fname': 'Tom', 'lname' : 'Jones'}
]

for x in sorted(users, key = itemgetter('fname')):
    print(x)

print('-----')

for x in sorted(users, key = itemgetter('fname', 'lname')):
    print(x)
    
print(sorted(users, key = lambda x: (x['fname'], x['lname'])))
'''

'''
from collections import Counter

text = "iPhone X (X pronounced \"ten\" /ˈtɛn/)[1] is a smartphone designed, developed, and marketed by Apple Inc. It was announced on September 12, 2017, alongside the iPhone 8 and iPhone 8 Plus at the Steve Jobs Theater in the Apple Park campus, by Apple CEO Tim Cook, and will be released on November 3, 2017.[2][3][4][5] It is called the iPhone X because it marks the iPhone's tenth anniversary, X being the symbol for \"ten\" in Roman numerals. Within Apple's line-up the X model is positioned as a high-end, premium model intended to showcase advanced technologies. Leaks, including those from case manufacturers, as well as HomePod firmware and the final version of iOS 11, revealed various aspects of the device prior to its unveiling, including that it would have a nearly bezel-less design and no physical home button, an OLED display, dual cameras with improved depth sensing, and a face recognition unlock system known as Face ID.[6][7]"

words = text.split(" ")
counter = Counter(words)
top_three = counter.most_common(3)
print(top_three)
'''

'''
from _operator import itemgetter

stocks = {
        'GOOG' : 434,
        'AAPL' : 325,
        'FB' : 54,
        'AMZN' : 623,
        'F' : 32,
        'MSFT' : 549
}

min_price = min(zip(stocks.values(), stocks.keys()))
print(min_price)

print(sorted(stocks.items(), key = itemgetter(1)))
test_min = min(stocks.items(), key = itemgetter(1))
print(test_min)
'''

'''
import heapq
from _operator import itemgetter

grades = [32, 43, 654, 34, 132, 66, 99, 532]

print(heapq.nlargest(3, grades))

stocks = [
        {'ticker': 'APPL', 'price': 201},
        {'ticker': 'GOOG', 'price': 800},
        {'ticker': 'F', 'price': 54},
        {'ticker': 'MSFT', 'price': 313},
        {'ticker': 'TUNA', 'price': 68}
]

print(sorted(stocks, key = lambda x: x['price']))
print(heapq.nsmallest(2, stocks, key = lambda x : x['ticker']))
'''

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