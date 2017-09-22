# -*- coding: utf-8 -*- 
from fb.whCollector import WhCollector

odds_list = []

wh = WhCollector()
urls = wh.getMatchLinks()

for url in urls:
    lst = wh.getAllOdds(wh.getOddsUrl(url[1]))
    for odds in lst:
        odds_list.append(odds)

for odds in odds_list:
    print(odds.title)
    for line in odds.lst:
        print(line) 