# author: Affrin Sultana,Helin Wang, Shi Yan Wang and Pavel Levchenko
# date: 2022-14-01

import plotly.express as px
import pandas as pd
import numpy as np
import yfinance as yf


def pencent_change(stock_ticker, start_date, end_date):
    """
    Calculate the daily profit rate change of a stock within a given period of time.
    
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


def volumeChange(stock_ticker, start_date, end_date):
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
        >>> volumeChange('AAPL', '01-01-2021', '01-01-2022)
        01-01-2021       Nan
        01-02-2021       Increase
        01-03-2021       Increase
        01-04-2021       Decrease
        ...
        12-31-2021       Increase
        01-01-2022       Increase
    """
    pass
    # TODO
    

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
