from bs4 import BeautifulSoup
import requests
import re
import util.alignLists
from util.alignLists import alignLst

class WhCollector():
    
    baseUrl = "https://www.williamhill138.com"
    
    matches = [
        '英格兰超级联赛',
        '西班牙甲组联赛'
    ]
    
    types = {
        'a' : '亚洲让分盘'
    }
    
    def getMatchLinks(self):
        source = requests.get(self.baseUrl + "/zh-cn/sport/football")
        soup = BeautifulSoup(source.text.encode('utf_8'), 'html.parser')
        
        matchUrls = []
        
        for match in self.matches:
            url = soup.find('a', {'title' : match, 'class' : 'coupon-homepage__group-link'})
            matchUrls.append(tuple((match, self.baseUrl + url.get('href'))))
        
        return matchUrls
    
    def getOddsUrl(self, matchUrl, type = 'a'):
        source = requests.get(matchUrl)
        soup = BeautifulSoup(source.text, 'html.parser')

        url = soup.find('a', {'class' : 'coupon-nav__link'}, text = re.compile("^"+self.types[type]+"*"))
        
        return str(self.baseUrl + url.get('href'))
    
    def getAllOdds(self, oddUrl):
        odds_list = []
        
        source = requests.get(oddUrl)
        soup = BeautifulSoup(source.text, 'html.parser')
        
        markets = soup.findAll('div', {'class' : 'multiple_markets'})
        
        for market in markets:
            odds_list.append(self.getOdds(market))
            
        return odds_list
        
    def getOdds(self, market):
        title = market.find('span', {'class' : 'coupon-title single'}).text
        odds = Odds(title.replace('\n', ''))
        
        #print(market)
        #print(odds.title)
        
        raw_lst = []
        header_row_lst = []
        table = market.find('tr', {'class' : 'header'})
        headers = table.findAll('td')
        for header in headers:
            if (header.text):
                header_row_lst.append(header.text)
        header_row_lst.append('所有盘口')
        
        raw_lst.append(header_row_lst)
        
        for tr in market.findAll('tr', {'class' : 'body', 'data-market-cash-out-elegible' : 'true'}):
            odds_row_lst = []
            odds_row_lst.append(tr.find('td', {'class' : 'date'}).get('data-sort'))
            odds_row_lst.append(tr.find('a', {'class' : 'title-wrapper'}).text)
            for td in tr.findAll('td', {'class' : 'outcome_ou'}):
                odds_row_lst.append(td.find('span', {'class' : 'player'}).text)
                odds_row_lst.append(td.get('data-sort'))
            odds_row_lst.append(tr.find('a', {'class' : 'sports-coupon__more-bets'}).text)
            raw_lst.append(odds_row_lst)
        
        odds.lst = alignLst(raw_lst)
 
        return odds
    

class Odds():
    
    lst = []
    
    def __init__(self, title):
        self.title = title
        
    
    