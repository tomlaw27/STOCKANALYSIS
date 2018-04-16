import pandas_datareader as pdr
import pandas_datareader.data as web
import pandas_datareader.nasdaq_trader as nas
import pandas as pd
import numpy as np
import sklearn as sk
from datetime import datetime
import scraper

def acquire():
    header = ["close_price","high_price","low_price","open_price","session","volume"]
    ticker = scraper.save_sp500_tickers()
    df = web.DataReader(ticker[0], 'robinhood')
    for i in range(1, ticker.__len__()-1):
        df = df.append(web.DataReader(ticker[i], 'robinhood'))
    df.to_csv("s&p500.csv",columns=header)
    #return df








