from os import get_terminal_size
from mynet_scraper import MynetScraper

JSON_FILE = "./data/stocks.json"
LIMIT = 30

scraper = MynetScraper()
scraper.get_stocks(LIMIT)

for stock in scraper.stocks:
    print(stock.name, stock.detail.alis, stock.detail.satis, type(stock.detail))

__sep_text = "\n" + (get_terminal_size().columns * "*") + "\n"
print(__sep_text)

for stock in list(filter(lambda x: "ACSEL" in x.code, scraper.stocks)):
    print([s for s in stock.detail.__dict__], sep="\n")

scraper.write_data(JSON_FILE)
