# Mynet scraper

Foobar is a Python Class for the information of stocks on the mynet site.
Mynet stocks site: [Mynet](https://finans.mynet.com/borsa/hisseler/)

Returns the contents of the stock you enter the name of.

Returns the contents of the number of stocks you enter.

## Installation

1. Clone the project from GitHub to copy it to your local computer:

```bash
git clone https://github.com/username/ai-customer-support-chatbot.git
cd ai-customer-support-chatbot
```

2. Create and Activate the Virtual Environment

```bash
python -m venv .venv
source .venv/bin/activate
```

3. Install requirements

```bash
pip install -r requirements.txt
```

4. Run the Application

```bash
python main.py
```

## Usage

```python
JSON_FILE = "./data/stocks.json"
LIMIT = 5

from mynet_scraper import MynetScraper

# returns 'stocks list'
scraper = MynetScraper()
scraper.get_stocks(LIMIT)

# returns 'share data'
stock = scraper.get_stock("ACSEL")

# print 'stock details'
print(stock.code, stock.name, stock.detail.alis, stock.detail.hissenin_ilk_islem_tarihi, stock.detail.satis, type(stock.detail))

for stock in scraper.stocks:
    print(stock.code.ljust(7), stock.name.ljust(20), stock.detail.alis.ljust(8), stock.detail.satis.ljust(8))
```

## Contributing


## License

# Mynet_scraper
