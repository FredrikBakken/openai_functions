import os
import json
import pandas as pd

from dotenv import load_dotenv
from entsoe import EntsoePandasClient


def get_all_market_codes(not_used: str):
    """
    Get market codes for all market areas

    Parameters
    ----------
    not_used : string
        unused parameter

    Returns
    -------
    list
        list of all market codes
    """

    return ['NO_1', 'NO_2', 'NO_3', 'NO_4', 'NO_5']


def market_area_to_market_code(market_area: str):
    """
    Convert the market area name to its corresponding market code

    Parameters
    ----------
    market_area : string
        name of the market area to get the market code for

    Returns
    -------
    string
        market code of market area
    """

    market_code = {
        "oslo": "NO_1",
        "kristiansand": "NO_2",
        "trondheim": "NO_3",
        "tromsø": "NO_4",
        "bergen": "NO_5",
    }

    return market_code.get(market_area.lower())


def _get_hourly_prices(market_code: str, start_date: str, end_date: str):
    """
    Get the hourly spot prices for market code from start date to end date

    Parameters
    ----------
    market_code : string
        market code of area to get hourly spot prices from
    start_date : string
        start date to get the hourly spot prices from
    end_date : string
        end date to get the hourly spot prices to

    Returns
    -------
    pandas.core.series.Series
        pandas series containing the hourly spot prices for a specific market area by its market code
    """

    load_dotenv()
    client = EntsoePandasClient(api_key=os.getenv("ENTSOE_API_KEY"))

    start = pd.Timestamp(start_date, tz='Europe/Oslo')
    end = pd.Timestamp(end_date, tz='Europe/Oslo')
    series = client.query_day_ahead_prices(market_code, start=start, end=end)

    return series


def calculate_mean_price(market_code: str, start_date: str, end_date: str):
    """
    Get the mean/average price for market code from start date to end date

    Parameters
    ----------
    market_code : string
        market code of area to get hourly spot prices from
    start_date : string
        start date to get the hourly spot prices from
    end_date : string
        end date to get the hourly spot prices to

    Returns
    -------
    string
        JSON string containing the hourly spot prices for a specific market area by its market code
    """

    series = _get_hourly_prices(market_code, start_date, end_date)

    print(series)
    print(series.mean())

    return series.mean()
