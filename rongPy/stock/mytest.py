from stock.stockCollector import StockCollector
import getpass

#sc = StockCollector(input("Sir, account please.\n"), getpass.getpass("Sir, your password?\n"), input('Where would you put csv files?\n'))
sc = StockCollector(input("Sir, account please.\n"), getpass.getpass("Sir, your password?\n"), "C:\\Rong\\99 Temp\\stocks\\")

list_url = sc.get_stock_listUrl()
stock_list = sc.get_stock_list(list_url)
sc.download_stock_csv(stock_list)
