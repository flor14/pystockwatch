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



def (stock_ticker, start_date, end_date, benchmark_ticker):
#Function 2 for line plot visualization by Affrin





def (stock_ticker, start_date, end_date):
#Function 3 for volume change calculations by Shi Yan



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