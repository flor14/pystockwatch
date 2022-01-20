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
        2017-01-03                      0.0000
        2017-01-04                     -0.1119
        2017-01-05                      0.3960
        2017-01-06                      1.5153
        2017-01-09                      2.4451
    >>> percent_change('AAPL MSFT', '2017-01-01', '2017-01-10')
                    Price Change Percentage(%) 
                              AAPL        MSFT
              Date
        2017-01-03          0.0000      0.0000
        2017-01-04         -0.1119     -0.4474
        2017-01-05          0.3960     -0.4474
        2017-01-06          1.5153      0.4155
        2017-01-09          2.4451      0.0959
    """ 
    
    # Import original dataframe by giving stock ticker, start data and end date
    data = yf.download(stock_ticker, start=start_date, end=end_date)
    
    # Only Keep "Adj Close" Price for 
    data = data.drop(columns={'Open', 'High', 'Low', 'Close', 'Volume'})
    
    # Carry out calculation
    for i in range(1,len(data)):
        data.iloc[i,:] = (data.iloc[i,:] - data.iloc[0,:])/data.iloc[0,:]*100
    
    data.iloc[0,:] = (data.iloc[0,:] - data.iloc[0,:])/data.iloc[0,:]*100
    
    # Manipulate column name
    data = data.rename(columns={"Adj Close": "Price Change Percentage(%)"})
    
    # Return result
    return pd.DataFrame(data)