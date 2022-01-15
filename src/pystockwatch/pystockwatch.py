# authors: Affrin Sultana, Helin Wang, Shi Yan Wang and Pavel Levchenko

import plotly.express as px
import pandas as pd
import numpy as np
import yfinance as yf


def percent_change(stock_ticker, start_date, end_date):
    """
    Calculates daily percentage change of a stock price within a given period of time
    
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
    >>> percent_change('AAPL', '01-01-2021', '12-31-2021')
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
    Visualizes trend of a stock price change against the market benchmark within a given period of time
    
    Parameters
    ----------
    stock_ticker : string
        Ticker of the stock such as 'AAPL'
    start_date : string 
        Initial date for data extraction
    end_date : string
        Final date for stock analysis
    benchmark_ticker : string 
        Ticker for benchmark comparison such as 'SPX' 
    
    Returns
    --------
    Interactive line plots which shows percentage change in stock price and market performance over time 
    
    Examples
    --------
    >>> profit_viz('AAPL', '01-01-2015', '01-01-2022', 'SPX')
    """
    pass
    # TODO


def volume_change(stock_ticker, start_date, end_date):
    """ 
    Calculate the daily trading volume change status of a stock within a given period of time

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
        A data frame with dates and their corresponding trading volume changes

    Examples
    --------
        >>> volume_change('AAPL', '01-01-2021', '01-01-2022)
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
    Visualize the daily trading volume of a stock using bar plot within a given period of time

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
