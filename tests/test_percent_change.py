from pystockwatch.percent_change import percent_change
from pytest import raises

def test_percent_change():
    # Invalid input for stock ticker
    with raises(NameError) as error_ticker:
        percent_change("Some Stock", "2017-01-01", "2017-01-10")
    assert(
        str(error_ticker.value) == "You enter an invalid stock ticker! Try again.")

    # Invalid input for start date
    with raises(ValueError) as error_start_date:
        percent_change("AAPL", "20170101", "2017-01-10")
    assert(
        str(error_start_date.value) == "You enter an invalid start date! Try date formatted in YYYY-MM-DD.")

    # Invalid input for end date
    with raises(ValueError) as error_end_date:
        percent_change("AAPL", "2017-01-01", "20170110")
    assert(
        str(error_end_date.value) == "You enter an invalid end date! Try date formatted in YYYY-MM-DD.")

    # End date is ealier than start date
    with raises(ValueError) as error_end_date:
        percent_change("AAPL", "2017-01-10", "2017-01-01")
    assert(
        str(error_end_date.value) == "End date should not be earlier than start date! Try again.")