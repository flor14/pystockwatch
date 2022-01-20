from pystockwatch import pystockwatch
from pytest import raises

def test_percentchange():
  pass


def test_profit_viz():
  pass


def test_volume_change():
    # Invalid stock ticker
    test_1 = "invalid ticker"
    with raises(NameError) as error_ticker:
        volume_change(test_1, "2021-12-01", "2021-12-31")
    assert(
        str(error_ticker.value) == "You enter an invalid stock ticker! Try again.")
    
    # Invalid date
    test_2 = "invalid start_date"
    with raises(ValueError) as error_start_date:
        volume_change("A", "2021", "2021-01-01")
    assert(
        str(error_start_date.value) == "You enter an invalid start date! Try again.")
    
    test_3 = "invalid_end_date"
    with raises(ValueError) as error_end_date:
        volume_change("A", "2021-01-01", 100)
    assert(
        str(error_end_date.value) == "You enter an invalid end date! Try again.")

    # Test indicators values
    indicators = ['nan', 'Decrease', 'Increase']
    df = volume_change("A", "2017-01-01", "2017-01-01")
    df_unique = df["Volume_Change"].unique()
    assert set(df_unique) <= set(indicators)
    

def volume_viz():
    vdf = volume_change('AAPL', '2015-01-01', '2016-01-01')

    assert vdf.shape[0] >= 1 # Check that at least one row is present in dataframe
    assert list(vdf.columns) == ['Date', 'Volume', 'Volume_Change'] # Check if all three columns are present in dataframe
    assert vdf['Volume'].min() >= 0  # Check for negative values of trading volume
