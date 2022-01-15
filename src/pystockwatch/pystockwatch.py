# author: Affrin Sultana,Helin Wang, Shi Yan Wang and Pavel Levchenko
# date: 2022-14-01

import plotly.express as px
import pandas as pd
import numpy as np
import yfinance as yf


def increase_pencent(stock_ticker, start_date, end_date):
#Function 1 for percentage change calculation by Helin
    """
    Calculate the stock price increase percentage by using end_date price minus start_date price and divided by the start_date price.
    
    Parameters
    ----------
    stock_ticker: string
        Ticker of the stock such as 'AAPL'
    start_date: datetime
        Initial date for data extraction
    end_date: datetime 
        Final data for stock analysis
    
    Returns
    --------
    The value of stock profit increase percentage.
    
    
    Examples
    --------
    >>>increase_percent('AAPL', '01-01-2021', '01-02-2021')
     
    """



def profit_viz(stock_ticker, start_date, end_date, benchmark_ticker):

    """
    Creates line plot showing the percentage change in profit for a given stock ticker in comparison to the benchmark ticker for a given date range
    
    Parameters
    ----------
    stock_ticker: string
        Ticker of the stock such as 'AAPL'
    start_date: datetime
        Initial date for data extraction
    end_date: datetime 
        Final data for stock analysis
    benchmark_ticker: string
        Ticker with which comparison is to be done such as 'SPX' 
    
    Returns
    --------
    interactive line plots which shows the percentage change in profit over time 
    
    
    Examples
    --------
    profit_viz('AAPL', '01-01-2015', '01-01-2022', 'SPX')
    
    """



def volumeChange(stock_ticker, start_date, end_date):
    """ 
    Return a dataframe that indicates daily volume change against previous day for the given time period

    Parameters
    ----------
    stock_ticker: string
        Ticker of the stock such as 'AAPL'
    start_date: datetime
        Initial date for data extraction
    end_date: datetime 
        Final data for stock analysis


    Returns:
        [pandas.core.frame.DataFrame]: [A Pandas dataframe contains indicators of daily volume change]

    Examples:
        >>> volumeChange('AAPL', '01-01-2015', '01-01-2022)
        0       Nan
        1       Increase
        2       Increase
        3       Decrease
        ...
        2255    Increase
        2256    Increase
    """
    pass
    # TODO




def volume_viz(stock_ticker, start_date, end_date):
    """
    Creates bar plot with trading volumes for a given stock colored by changes in volume, where increased volume is colored by green and decreased volume is colored by reduce
    
    Parameters
    ----------
    stock_ticker: string
        Ticker of the stock such as 'AAPL'
    start_date: datetime
        Initial date for data extraction
    end_date: datetime 
        Final data for stock analysis
    
    Returns
    --------
    interactive plot with overlay of line plots and bar plot
    
    
    Examples
    --------
    volume_viz('AAPL', '01-01-2015', '01-01-2022')
     
    """
