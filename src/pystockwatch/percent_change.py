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

    data = yf.download(stock_ticker, start=start_date, end=end_date)
    
    data = data.drop(columns={'Open', 'High', 'Low', 'Close', 'Volume'})
    
    for i in range(1,len(data)):
        data.iloc[i,:] = (data.iloc[i,:] - data.iloc[0,:])/data.iloc[0,:]
    
    data.iloc[0,:] = (data.iloc[0,:] - data.iloc[0,:])/data.iloc[0,:]
    
    data = data.rename(columns={"Adj Close": "Price Change Percentage(%)"})
    
    return pd.DataFrame(data)