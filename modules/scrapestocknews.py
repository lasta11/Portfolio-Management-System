# -*- coding: utf-8 -*-
"""ScrapeStockNews.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1re-dh3zI9x5LOvF0fRjezKZMhOBSlVFf
"""

import pandas as pd
import requests
from bs4 import BeautifulSoup
import os

tickers = ['AMZN','TSLA', 'GOOG','PEP','DDOG','SONY','AAPL','COST','JPM','TSM', 'WMT','JPM','PG','HD','META','ABBV','BABA' ] 
start_date = '2020-01-01' 
end_date = '2020-12-31'

def get_news_data(ticker):
    finviz_url = f'https://finviz.com/quote.ashx?t={ticker}'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:20.0) Gecko/20100101 Firefox/20.0'
    }
    html = requests.get(finviz_url, headers=headers).text
    soup = BeautifulSoup(html, 'html.parser')
    news_table = soup.find(id='news-table')
    news_data = []
    for row in news_table.findAll('tr'):
        title = row.a.text if row.a else ''
        timestamp = row.td.text.strip()
        date = timestamp.split(' ')[0]
        if start_date <= date <= end_date:
            news_data.append({'date': date, 'title': title})
    return pd.DataFrame(news_data)

news = {}
for ticker in tickers:
    news[ticker] = get_news_data(ticker)
# This will give us a dictionary of tickers with their news