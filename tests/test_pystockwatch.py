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
    

def test_volume_viz():
    vdf = volume_change('AAPL', '2015-01-01', '2016-01-01')
    assert vdf.shape[0] >= 1, 'dataframe should have at least one row'
    assert list(vdf.columns) == ['Date', 'Volume', 'Volume_Change'], "columns should be named 'Date', 'Volume', 'Volume_Change'"
    assert vdf['Volume'].min() >= 0, 'trading volumes should be positive'
    

    fig = volume_viz('AAPL', '2015-01-01', '2015-01-05')
    assert str(fig.select_xaxes).split("'type':")[1].split(',')[0].replace("'", "").replace(' ', '') == 'bar', 'volumes should be plotted as bar chart'
    
    

