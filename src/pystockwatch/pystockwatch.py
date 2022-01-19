# author: Affrin Sultana,Helin Wang, Shi Yan Wang and Pavel Levchenko
# date: 2022-14-01

import plotly.express as px
import pandas as pd
import numpy as np
import yfinance as yf
import pandas_datareader as pdr
import datetime
import warnings


def percent_change(stock_ticker, start_date, end_date):
    """
    Calculate the daily profit percentage change of a stock within a given period of time.
    
    Parameters
    ----------
    stock_ticker : string 
        Ticker of the stock such as 'AAPL'
    start_date : string
        Initial date for data extraction
    end_date : string
        Final date for stock analysis
    
    Returns
    --------
    DataFrame
        A data frame with dates and their corresponding stock price percentage changes.
    
    Examples
    --------
    >>> increase_percent('AAPL', '01-01-2021', '12-31-2021')
        Date            Price Change Percentage(%)
        01-01-2021      0
        01-02-2021      0.7
        01-03-2021      1.1
        ...
        12-30-2021      23
        12-31-2021      6.5
    """ 
    pass
    # TODO
    

def profit_viz(stock_ticker, start_date, end_date, benchmark_ticker):
    """
    Visualize trend of a stock profit rate change against the market benchmark within a given period of time.
    
    Parameters
    ----------
    stock_ticker : string
        Ticker of the stock such as 'AAPL'
    start_date : string 
        Initial date for data extraction
    end_date : string
        Final date for stock analysis
    benchmark_ticker : string 
        Ticker with which comparison is to be done such as 'SPX' 
    
    Returns
    --------
    Interactive line plots which shows the percentage change in profit over time 
    
    Examples
    --------
    >>> profit_viz('AAPL', '01-01-2015', '01-01-2022', 'SPX')
    """
    pass
    # TODO


def volume_change(stock_ticker, start_date, end_date):
    """ 
    Calculate the daily trading volume change status of a stock within a given period of time.

    Parameters
    ----------
    stock_ticker : string 
        Ticker of the stock such as 'AAPL'
    start_date : string
        Initial date for data extraction
    end_date : string 
        Final date for stock analysis
        
    Returns
    --------
        A data frame with dates and their corresponding trading volume changes.

    Examples
    --------
        >>> volume_change('AAPL', '01-01-2021', '01-01-2022)
        Date             Volume_Change
        01-01-2021       Nan
        01-02-2021       Increase
        01-03-2021       Increase
        01-04-2021       Decrease
        ...
        12-31-2021       Increase
        01-01-2022       Increase
    """
    yf.pdr_override()
    # Assert ticker value
    ticker = yf.Ticker(stock_ticker)
    if(ticker.info["regularMarketPrice"] == None):
        raise NameError("You enter an invalid stock ticker! Try again.")
    # Assert date value
    format = "%Y-%m-%d"
    try: datetime.datetime.strptime(start_date, format)
    except ValueError:
        raise ValueError("You enter an invalid start date! Try again.")
    try: datetime.datetime.strptime(end_date, format)
    except ValueError:
        raise ValueError("You enter an invalid end end! Try again.")
    data = pdr.get_data_yahoo(stock_ticker, start=start_date, end=end_date)
    # Assert correct data fetched
    try:
        isinstance(data, pd.DataFrame)
    except ValueError:
        raise ValueError("You input can't be converted to a pandas dataframe.")
    df = data["Volume"].diff().to_frame()
    df["Volume_Change"] = np.select([df["Volume"] > 0, df["Volume"]<0],
                             ["Increase", "Decrease"],
                             default = np.nan)
    # Assert correct indicator values
    for indicator in df["Volume_Change"]:
        if(indicator != "Decrease" and indicator != "Increase" and indicator != "nan"):
            raise ValueError("Incorrect Volume Change indicator")
    return df[["Volume_Change"]]
    

def volume_viz(stock_ticker, start_date, end_date):
    """
    Visualize the daily trading volume of a stock using bar plot within a given period of time.

    Parameters
    ----------
    stock_ticker : string  
        Ticker of the stock such as 'AAPL'
    start_date : string 
        Initial date for data extraction
    end_date : string 
        Final date for stock analysis
    
    Returns
    --------
    Interactive plot with overlay of line plots and bar plot
    
    Examples
    --------
    >>> volume_viz('AAPL', '01-01-2015', '01-01-2022')
    """
    pass
    # TODO
