from pystockwatch import pystockwatch
from pytest import raises

def test_percent_change():
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


def test_profit_viz():
  pass


def test_volume_change():
    df = volume_change("AAPL", "2017-01-01", "2017-01-10")
    
    # Test output datatype
    assert type(df) == type(pd.DataFrame())
    
    # Test output shape
    assert len(df.columns) == 3
  
    # Test indicators values
    indicators = ['nan', 'Decrease', 'Increase']
    df_unique = df["Volume_Change"].unique()
    assert set(df_unique) <= set(indicators)
    

def volume_viz():
    vdf = volume_change('AAPL', '2015-01-01', '2016-01-01')

    assert vdf.shape[0] >= 1 # Check that at least one row is present in dataframe
    assert list(vdf.columns) == ['Date', 'Volume', 'Volume_Change'] # Check if all three columns are present in dataframe
    assert vdf['Volume'].min() >= 0  # Check for negative values of trading volume
