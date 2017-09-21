from fb.whCollector import WhCollector

wh = WhCollector()
urls = wh.getMatchLinks()

for url in urls:
    wh.getAllOdds(wh.getOddsUrl(url[1]))