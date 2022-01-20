# authors: Affrin Sultana, Helin Wang, Shi Yan Wang and Pavel Levchenko

import plotly.express as px
import plotly.graph_objects as go
import pandas as pd
import numpy as np
import yfinance as yf
import pandas_datareader as pdr
import datetime
import warnings

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
    
    # Assert ticker input value
    ticker = yf.Ticker(stock_ticker)
    if(ticker.info["regularMarketPrice"] == None):
        raise NameError("You enter an invalid stock ticker! Try again.")
    
    # Assert start date input value
    format = "%Y-%m-%d"
    try: datetime.datetime.strptime(start_date, format)
    except ValueError:
        raise ValueError("You enter an invalid start date! Try date formatted in YYYY-MM-DD.")
    
    # Assert end date input value
    try: datetime.datetime.strptime(end_date, format)
    except ValueError:
        raise ValueError("You enter an invalid end end! Try date formatted in YYYY-MM-DD.")

    # Assert end date is later than start date
    format = "%Y-%m-%d"
    if(datetime.datetime.strptime(end_date, format) < datetime.datetime.strptime(start_date, format)):
        raise ValueError("You enter an end date which is earlier than the start date! Try again.")
    
    # Import original dataframe by giving stock ticker, start data and end date
    data = yf.download(stock_ticker, start=start_date, end=end_date)
    
    # Only Keep "Adj Close" Price for 
    data = data.drop(columns={'Open', 'High', 'Low', 'Adj Close', 'Volume'})
    
    # Carry out calculation
    for i in range(1,len(data)):
        data.iloc[i,:] = (data.iloc[i,:] - data.iloc[0,:])/data.iloc[0,:]*100
    
    data.iloc[0,:] = (data.iloc[0,:] - data.iloc[0,:])/data.iloc[0,:]*100
    
    # Manipulate column name
    data = data.rename(columns={"Close": "Price Change Percentage(%)"})
    
    # Return result
    return pd.DataFrame(data)


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
    Calculates the daily trading volume change status of a stock within a given period of time
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
        >>> volume_change('AAPL', '2021-01-01', '2022-01-01')
        Date             Volume Volume_Change
        01-01-2021        1000        Nan
        01-02-2021        2000        Increase
        01-03-2021        3000        Increase
        01-04-2021        2500        Decrease
        ...
        12-31-2021        4000        Increase
        01-01-2022        5000        Increase
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
    df = pdr.get_data_yahoo(stock_ticker, start=start_date, end=end_date)['Volume'].reset_index()
    # Assert correct data fetched
    try:
        isinstance(df, pd.DataFrame)
    except ValueError:
        raise ValueError("You input can't be converted to a pandas dataframe.")
    df['Volume_dif'] = df['Volume'].diff().to_frame()
    df["Volume_Change"] = np.select([df["Volume_dif"] > 0, df["Volume_dif"]<0], ["Increase", "Decrease"], 
                                    default = np.nan)
    # Assert correct indicator values
    for indicator in df["Volume_Change"]:
        if(indicator != "Decrease" and indicator != "Increase" and indicator != "nan"):
            raise ValueError("Incorrect Volume Change indicator")
    return df[['Date','Volume', 'Volume_Change']]
    

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
    vdf = volume_change(stock_ticker, start_date, end_date)
    vdf_increase = vdf.loc[vdf['Volume_Change']=='Increase']
    vdf_decrease = vdf.loc[vdf['Volume_Change']=='Decrease']

    fig = go.Figure()
    fig.add_trace(go.Bar(x=vdf_increase['Date'], y=vdf_increase['Volume'],
                    base=0,
                    marker_color='green',
                    name='Volume Increase'))
    fig.add_trace(go.Bar(x=vdf_decrease['Date'], y=vdf_decrease['Volume'],
                    base=0,
                    marker_color='red',
                    name='Volume Decrease'
                    ))

    fig.show()
