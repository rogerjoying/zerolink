from stock.googleSession import GoogleSession
from bs4 import BeautifulSoup
from urllib import request
import re
import json
import urllib

class StockCollector(GoogleSession):
    
    url_finance = "https://finance.google.com"
    
    def __init__(self, login, pwd, dir):
        super(StockCollector, self).__init__(login, pwd)
        self.dir = dir

    def get_stock_listUrl(self):
        source_code = self.get(self.url_finance)
        soup = BeautifulSoup(source_code,"html.parser")
        for link in soup.findAll('a', {"href":re.compile("^/finance/portfolio\?action=view\&ei=*")}):
            href = link.get('href')
            break
        return href
           
    def get_stock_list(self, list_url):
        stock_list = []
        source_code = self.get(self.url_finance + list_url)
        soup = BeautifulSoup(source_code, "html.parser")
        
        for source_stockinfo in soup.findAll("script"):
            if source_stockinfo.string:
                stockinfo = re.search('^google.finance.data = (.*);', source_stockinfo.string, re.M)
                if stockinfo:
                    break
        
        stocklist_info = re.search('streaming:(.*)},stickyUrlArgs', stockinfo.group(1))
        
        str_data = re.sub(re.compile('cid:".*?",'), "", stocklist_info.group(1))
        str_data = re.sub(re.compile('s:'), '"s":', str_data)
        str_data = re.sub(re.compile('e:'), '"e":', str_data)
        
        stock_json = json.loads(str_data)
        
        for stock in stock_json:
            stock_list.append(stock["e"]+':'+stock["s"])
            
        return stock_list
        
    def download_stock_csv(self, stock_list):
        for stock in stock_list:
            try:
                url = self.url_finance + r"/finance/historical?q="+stock+r"&output=csv"
                response = request.urlopen(url)
                csv = response.read().decode("utf-8-sig")
                csv_str = str(csv)
                lines = csv_str.split(r'\n')
                dest_url = ''.join([self.dir, re.sub(re.compile('.*?:'), "", stock), '.csv'])
                fw = open(dest_url, 'w')
                for line in lines:
                    fw.write(line + '\n')
                fw.close()
                print(stock + " CSV download complete.\n")
            except urllib.error.HTTPError:
                print("Download failed: " + url + "\n")
                continue
