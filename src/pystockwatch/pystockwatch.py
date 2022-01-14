# author: Affrin Sultana,Helin Wang, Shi Yan Wang and Pavel Levchenko
# date: 2022-14-01

import plotly.express as px
import pandas as pd
import numpy as np
import yfinance as yf


def (stock_ticker, start_date, end_date):
#Function 1 for percentage change calculation by Helin




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