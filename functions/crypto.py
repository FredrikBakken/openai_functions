import requests
from datetime import datetime, timedelta


def get_crypto_peak_price(cryptocurrency: str = 'Ethereum'):
    """
    Get the peak price of a cryptocurrency from yesterday, e.g. Ethereum

    Parameters
    ----------
    cryptocurrency : string
        cryptocurrency to get yesterday's peak price from

    Returns
    -------
    integer
        peak price
    """

    yesterday = datetime.now() - timedelta(days=1)
    yesterday_str = yesterday.strftime("%d-%m-%Y")

    # Fetch historical price data for Ethereum
    url = f"https://api.coingecko.com/api/v3/coins/{cryptocurrency.lower()}/market_chart?vs_currency=usd&days=2"
    response = requests.get(url)
    data = response.json()

    # Get the prices from the API response
    prices = data["prices"]

    # Filter prices for yesterday
    yesterday_prices = [price for price in prices if
                        datetime.fromtimestamp(price[0] / 1000).strftime("%d-%m-%Y") == yesterday_str]

    # Calculate the peak price from yesterday
    peak_price = max(yesterday_prices, key=lambda x: x[1])

    return peak_price[1]
