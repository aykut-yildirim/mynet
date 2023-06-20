"""this module collect data from `mynet finans`"""
import re
import json
from typing import List, Optional
from dataclasses import make_dataclass, asdict
import fnmatch

import requests
from bs4 import BeautifulSoup
from tqdm import tqdm

from .models import Stock


HTML = "https://finans.mynet.com/borsa/hisseler/"


class MynetScraper:
    """
    starts scraping data from mynet with `get_stocks` method.

    EX:
    ```python
        scraper = MynetScraper()
        scraper.get_stocks()
    ```
    """

    def __init__(self):
        self.base_url = HTML
        self.base_link_list = []
        self.stocks: List[Stock] = []

    @classmethod
    def __make_soup(cls, html):
        """creates bs4 object from given url

        Args:
            url (str): url of stock's detail page

        Returns:
            : soup of detail's page
        """
        response = requests.get(html, timeout=30)
        html_content = response.text
        soup = BeautifulSoup(html_content, "html.parser")
        return soup

    @classmethod
    def __tr_ing(cls, turkce):
        """_summary_"""
        turkce = turkce.lower()
        turkce = turkce.replace("20", "yirmi")
        turkce = turkce.replace("52", "elliiki")
        turkce = re.sub(r"\d+", "", turkce)
        tr2eng = str.maketrans("üıçğşö()% ", "uicgso____")
        ing = turkce.translate(tr2eng)
        return ing

    def write_data(self, output_file: str = "./stocks.json"):
        """write stocks data to json file"""

        _stocks = [asdict(stock) for stock in self.stocks]

        with open(output_file, "w", encoding="utf-8") as json_dosya:
            json.dump(_stocks, json_dosya, ensure_ascii=False)

    def __get_link(self, limit: Optional[int]):
        """for to add links"""
        souplink = MynetScraper.__make_soup(self.base_url)
        links_find = souplink.find("tbody").find_all("tr", limit=limit)
        links_find_tqdm = tqdm(
            links_find,
            desc="linkler toplanıyor.",
            leave=False,
            total=len(links_find),
        )

        for item in links_find_tqdm:
            link = item.find("a").get("href")
            self.base_link_list.append(link)

    @classmethod
    def __create_detail_dataclass(cls, data: dict):
        _data = make_dataclass(
            "StockDetail",
            [(cls.__tr_ing(k), type(v)) for k, v in data.items()],
        )
        data: type = _data(**{cls.__tr_ing(k): v for k, v in data.items()})
        return data

    def get_stocks(self, limit: Optional[int] = None):
        """for to add share data"""
        self.__get_link(limit)
        link_list_tqdm = tqdm(
            self.base_link_list, leave=False, desc="veriler isleniyor"
        )
        for link in link_list_tqdm:  # TOTO change the algorithm
            dict_item = {}
            soup = self.__make_soup(link)
            name = soup.find("div", {"flex-list-heading"}).h2.text
            child = soup.find("div", {"flex-list-2-col"}).find_all("li")
            for elem in child:
                key_a = elem.find_all("span")[0].text
                value_a = elem.find_all("span")[1].text
                dict_item[key_a] = value_a
            share = Stock(
                name[-5:], name[:-7], self.__create_detail_dataclass(dict_item)
            )
            self.stocks.append(share)

    def get_stock(self, stock_name: str):
        """for to make list
        Args:
            stock_name (str, optional): sahare name. Defaults to "".
        ex:
        """
        for stock in self.stocks:
            stock_name = stock_name.upper()
            if fnmatch.fnmatch(stock.code, "*" + stock_name + "*"):
                return stock
