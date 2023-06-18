import json
import pandas as pd


def _read_dataset(filepath: str):
    df = pd.read_csv(filepath)
    return df


def get_property_location_area_dataset(filepath: str, location: str):
    """
    Obtain a dataset from file containing a pandas dataframe with property listing information such as date, location, type, total price, number of bedrooms, size, and ad link

    Parameters
    ----------
    filepath : string
        path to the local file to read from
    location : string
        name of property location area to filter data for

    Returns
    -------
    pandas.core.frame.DataFrame
        pandas dataframe containing property date, location, type, total price, number of bedrooms, size, and ad link
    """

    df = _read_dataset(filepath)
    selected_columns = df[[
        'date',
        'location_area',
        'property_type_description',
        'price_total',
        'number_of_bedrooms',
        'area_range',
        'ad_link']].dropna()
    selected_columns = selected_columns.rename(columns={'location_area': 'location'})

    return selected_columns
