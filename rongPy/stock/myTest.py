from stock.stockCollector import StockCollector
from config.configData import configData
import getpass

config_data = configData('../config.json')

#sc = StockCollector(input("Sir, account please.\n"), getpass.getpass("Sir, your password?\n"), input('Where would you put csv files?\n'))
sc = StockCollector(input("Sir, account please.\n"), getpass.getpass("Sir, your password?\n"), config_data.data["stock"][0]["dir"])

print(config_data.data["stock"][0]["dir"])

list_url = sc.get_stock_listUrl()
stock_list = sc.get_stock_list(list_url)
sc.download_stock_csv(stock_list)
