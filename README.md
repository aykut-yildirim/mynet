# Mynet scraper

Mynet scraper is a Python Class for the information of stocks on the mynet site.
Mynet stocks site: [Mynet](https://finans.mynet.com/borsa/hisseler/)

I would make a makefile to help you and increase its usefulness.

Below is a python commands for example usage.

## Installation

1. Clone the project from GitHub to copy it to your local computer:

```bash
git clone https://github.com/aykut-yildirim/mynet.git
cd mynet
```

2. Create and Activate the Virtual Environment

```bash
python -m venv .venv
source .venv/bin/activate
```

If you want to install with makefile

```bash
make make_env
```

3. Command line to set up the requirements

```bash
pip install -r requirements.txt
```

If you want to install with makefile

```bash
make install_requirements
```

4. Run the Application

```bash
python main.py
```

If you want to install with makefile

```bash
make run
```

## Usage example

```python
JSON_FILE = "./data/stocks.json"
LIMIT = 5

from mynet_scraper import MynetScraper

#
scraper = MynetScraper()

# The code that lists the information of the stocks, the number of which is entered
scraper.get_stocks(LIMIT)

# The command that brings the information of the stock whose code is entered
stock = scraper.get_stock("ACSEL")

# code that extracts what is requested from the information of the stock whose code is entered
print(stock.code, stock.name, stock.detail.alis, stock.detail.hissenin_ilk_islem_tarihi, stock.detail.satis, type(stock.detail))

for stock in scraper.stocks:
    print(stock.code.ljust(7), stock.name.ljust(20), stock.detail.alis.ljust(8), stock.detail.satis.ljust(8))

# default save location: ./stocks.json
scraper.write_data(JSON_FILE)
```

# Mynet_scraper
