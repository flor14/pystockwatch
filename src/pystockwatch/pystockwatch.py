# author: Affrin Sultana,Helin Wang, Shi Yan Wang and Pavel Levchenko
# date: 2022-14-01

import plotly.express as px
import pandas as pd
import numpy as np
import yfinance as yf


def percent_change(stock_ticker, start_date, end_date):
#Function 1 for percentage change calculation by Helin
    """
    Calculate the percentage of stock price change for each day compared to the start date for a selected period.
    
    Parameters
    ----------
    stock_ticker: string
        Ticker of the stock such as 'AAPL'
    start_date: datetime
        Initial date for data extraction
    end_date: datetime 
        Final date for stock analysis
    
    Returns
    --------
    DataFrame:
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
        12-31-2021      26.5
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
        Final date for stock analysis
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
        Final date for stock analysis


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
        Final date for stock analysis
    
    Returns
    --------
    interactive plot with overlay of line plots and bar plot
    
    
    Examples
    --------
    volume_viz('AAPL', '01-01-2015', '01-01-2022')
     
    """
