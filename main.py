from os import get_terminal_size
from mynet_scraper import MynetScraper

JSON_FILE = "./data/stocks.json"
LIMIT = 5

scraper = MynetScraper()
scraper.get_stocks(LIMIT)
stock = scraper.get_stock("acse")
__sep_text = "\n" + (get_terminal_size().columns * "*") + "\n"

print(__sep_text)
print(stock.code, stock.name, stock.detail.alis, stock.detail.hissenin_ilk_islem_tarihi, stock.detail.satis, type(stock.detail))

print(__sep_text)

for stock in scraper.stocks:
    print(stock.code.ljust(7), stock.name.ljust(20), stock.detail.alis.ljust(10), stock.detail.satis.ljust(10))
print(__sep_text)
for stock in list(filter(lambda x: "ACSEL" in x.code, scraper.stocks)):
    print([s for s in stock.detail.__dict__], sep="\n")

scraper.write_data(JSON_FILE)
dir(MynetScraper)
