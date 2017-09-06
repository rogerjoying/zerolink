from realE.ljSession import LjSession
from bs4 import BeautifulSoup
import re
import json

class ReCollector(LjSession):
    
    url_prop = "http://user.sh.lianjia.com/favor/getMyFavorPropertyList.json"
    url_base = "http://sh.lianjia.com"
    
    def __init__(self, login, pwd):
        super(ReCollector, self).__init__(login, pwd)

    def get_re_list(self):
        xiaoqu_links = []
        
        source_code = self.get(self.url_prop)
        soup = BeautifulSoup(source_code,"html.parser")
    
        soup_json = json.loads(soup.encode("utf-8"))    
        for prop in soup_json["data"]:
            url = prop["houseServerUrl"] + "/ershoufang/q" + prop["propertyNo"]
            xiaoqu_links.append(url)
        
        return xiaoqu_links
    
    def get_re_msg(self, xiaoqu_links):
        re_msg_list = []
        
        for xiaoqu in xiaoqu_links:
            source_code = self.get(xiaoqu)
            soup = BeautifulSoup(source_code, "html.parser")
            
            for data in soup.find('ul', {"class" : "js_fang_list"}).findAll('li'):
                infoData = data.find('div', {"class" : "info"})
                
                titleData = infoData.find('a', {"gahref" : re.compile("^results_click_order_*")})
                title = titleData.get("title")
                href = self.url_base + titleData.get("href")
                
                reData = infoData.find('div', {"class" : "info-table"})
                desData = reData.find('span', {"class" : "info-col row1-text"})
                des = re.sub("\n", "", desData.text)
                des = re.sub("\t", "", des)
                
                priceData = reData.find('span', {"class" : "total-price strong-num"})
                price = priceData.text + '万'
                
                propData = reData.find('a', {"class" : "laisuzhou"})
                propName = propData.text
                
                re_msg_list.append(propName + "\t" + des + "\t" + price + "\t" + title + "\t" + href)    
        
        return re_msg_list
        