# authors: Affrin Sultana, Helin Wang, Shi Yan Wang and Pavel Levchenko
# January,2022

from pystockwatch.pystockwatch import percent_change
from pystockwatch.pystockwatch import profit_viz
from pystockwatch.pystockwatch import volume_change
from pystockwatch.pystockwatch import volume_viz

import altair as alt
import pytest
from pytest import raises
import pandas as pd


def test_percent_change():
    """
    Test input, output and exeption handling for percent_change()
    Example
    -------
    >>> test_percent_change()
    """

    # Invalid input for stock ticker
    with raises(NameError) as error_ticker:
        percent_change("Some Stock", "2017-01-01", "2017-01-10")

    # Invalid input for start date
    with raises(ValueError) as error_start_date:
        percent_change("AAPL", "20170101", "2017-01-10")

    # Invalid input for end date
    with raises(ValueError) as error_end_date:
        percent_change("AAPL", "2017-01-01", "20170110")

    # End date is ealier than start date
    with raises(ValueError) as error_end_date:
       percent_change("AAPL", "2017-01-10", "2017-01-01")

    # Check output dataframe
    output = percent_change("AAPL", "2017-01-01", "2017-01-10")
    assert isinstance(
        output, pd.DataFrame
    ), "Pandas dataframe object should be returned."


def test_profit_viz_input():
    """
    Test input, output and exeption handling for profit_viz()
    Example
    -------
    >>> test_profit_viz_input()
    """
    profit = percent_change("AAPL", "2017-01-01", "2017-01-10").reset_index()

    # Regression Testing
    assert profit.shape[0] >= 1, 'dataframe should have at least one row'
    # Test output shape
    assert len(profit.columns) == 2, "Dataframe should have two columns!"

    # Raise specific type errors

    #Invalid input for stock ticker
    with pytest.raises(NameError):
        profit_viz("XYZ", "2017-01-01", "2017-01-10","MSFT")

    # Invalid input for bench ticker
    with pytest.raises(NameError):
        profit_viz("AAPL", "2017-01-01", "2017-01-10","XYZ")

    # Invalid input for start date
    with pytest.raises(ValueError):
        profit_viz("AAPL", "20170101", "2017-01-10","MSFT")
    
    # Invalid input for end date
    with pytest.raises(ValueError):
        profit_viz("AAPL", "2017-01-01", "20170110","MSFT")

    # End date is ealier than start date
    with pytest.raises(ValueError):
        profit_viz("AAPL", "2017-01-10", "2017-01-01","MSFT")
    
def test_profit_viz_plot():
    """
    Test plot title and type for profit_viz()
    Example
    -------
    >>> test_profit_viz_plot()
    """


    chart =  profit_viz("AAPL", "2017-01-01", "2017-01-10","MSFT")
    dict = chart.to_dict()
    assert type(chart) == type(alt.Chart()), "Expected an altair Chart but given something else! "
    assert dict['encoding']['x']['field'] == 'Date', 'Date should be mapped to the x axis'
    assert dict['encoding']['y']['field'] == 'Profit Percent', 'Profit Percent should be mapped to the y axis'
    assert dict['mark'] == 'line', "Altair mark should be 'line'"
    assert dict['title'] == 'Profit Percent trend of Stock vs Benchmark ticker', "Title is incorrect should be 'line'"
    
    


def test_volume_change():
    """
    Test input, output and exeption handling for volume_change()
    Example
    -------
    >>> test_volume_change()
    """

    df = volume_change("AAPL", "2017-01-01", "2017-01-10")
    
    # Test output datatype
    assert type(df) == type(pd.DataFrame()), "Expect a dataframe but given something else! "
    
    # Test output shape
    assert len(df.columns) == 3, "Dataframe should have three columns!"
  
    # Test indicators values
    indicators = ['nan', 'Decrease', 'Increase']
    df_unique = df["Price_change"].unique()
    assert set(df_unique) <= set(indicators)
    

def test_volume_viz():
    """
    Test input, output and exeption handling for volume_viz()
    Example
    -------
    >>> test_volume_viz()
    """

    vdf = volume_change('AAPL', '2015-01-01', '2016-01-01')
    assert vdf.shape[0] >= 1, 'dataframe should have at least one row'

    assert list(vdf.columns) == ['Date', 'Volume', 'Price_change'], "columns should be named 'Date', 'Volume', 'Price_Change'"

    assert vdf['Volume'].min() >= 0, 'trading volumes should be positive'
    

    fig = volume_viz('AAPL', '2015-01-01', '2015-01-05')
    assert str(fig.select_xaxes).split("'type':")[1].split(',')[0].replace("'", "").replace(' ', '') == 'bar', 'volumes should be plotted as bar chart'
    
   
