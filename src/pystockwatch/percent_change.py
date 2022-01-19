import pandas as pd
import numpy as np
import yfinance as yf


def percent_change(stock_ticker, start_date, end_date):
    """
    Calculates daily percentage change of a stock price within a given period of time
    
    Parameters
    ----------
    stock_ticker : string 
        Ticker of the stock such as 'AAPL', or 'AAPL MSFT SPY' for multiple tickers
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
    >>> percent_change('AAPL', '2017-01-01', '2017-01-10')
                    Price Change Percentage(%) 
              Date
        2017-01-03                    0.000000
        2017-01-04                   -0.001119
        2017-01-05                    0.003960
        2017-01-06                    0.015153
        2017-01-09                    0.024451
    >>> percent_change('AAPL MSFT', '2017-01-01', '2017-01-10')
                    Price Change Percentage(%) 
                              AAPL        MSFT
              Date
        2017-01-03        0.000000    0.000000
        2017-01-04       -0.001119   -0.004474
        2017-01-05        0.003960   -0.004474
        2017-01-06        0.015153    0.004155
        2017-01-09        0.024451    0.000959
    """ 

    data = yf.download(stock_ticker, start=start_date, end=end_date)
    
    data = data.drop(columns={'Open', 'High', 'Low', 'Close', 'Volume'})
    
    for i in range(1,len(data)):
        data.iloc[i,:] = (data.iloc[i,:] - data.iloc[0,:])/data.iloc[0,:]
    
    data.iloc[0,:] = (data.iloc[0,:] - data.iloc[0,:])/data.iloc[0,:]
    
    data = data.rename(columns={"Adj Close": "Price Change Percentage(%)"})
    
    return pd.DataFrame(data)