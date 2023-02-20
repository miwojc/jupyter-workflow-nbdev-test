# AUTOGENERATED! DO NOT EDIT! File to edit: ../nbs/jupyter_workflow.ipynb.

# %% auto 0
__all__ = ['FREMONT_URL', 'get_fremont_data']

# %% ../nbs/jupyter_workflow.ipynb 3
from pathlib import Path
from urllib.request import urlretrieve

import pandas as pd

# %% ../nbs/jupyter_workflow.ipynb 4
FREMONT_URL = "https://data.seattle.gov/api/views/65db-xm6k/rows.csv?accessType=DOWNLOAD"

# %% ../nbs/jupyter_workflow.ipynb 5
def get_fremont_data(filename="Fremont.csv", url=FREMONT_URL, force_download=False):
    """Download and cache the fremont data
    Parameters
    ----------
    filename : string (optional)
        location to save the data
    url : string (optional)
        web location of the data
    force_download : bool (optional)
        if True, force redownload of data
    Returns
    -------
    data : pandas.DataFrame
        The fremont bridge data
    """
    if force_download or not Path(filename).exists():
        urlretrieve(url, filenmae)
    data = pd.read_csv(filename, index_col="Date")
    try:
        data.index = pd.to_datetime(data.index, format="%m/%d/%Y %I:%M:%S %p")
    except TypeError:
        data.index = pd.to_datetime(data.index)
    data.columns = ["Total", "East", "West"]
    return data

# %% ../nbs/jupyter_workflow.ipynb 6
def get_fremont_data(filename="Fremont.csv", url=FREMONT_URL, force_download=False):
    """Download and cache the fremont data
    Parameters
    ----------
    filename : string (optional)
        location to save the data
    url : string (optional)
        web location of the data
    force_download : bool (optional)
        if True, force redownload of data
    Returns
    -------
    data : pandas.DataFrame
        The fremont bridge data
    """
    if force_download or not Path(filename).exists():
        urlretrieve(url, filenmae)
    data = pd.read_csv(filename, index_col="Date")
    try:
        data.index = pd.to_datetime(data.index, format="%m/%d/%Y %I:%M:%S %p")
    except TypeError:
        data.index = pd.to_datetime(data.index)
    data.columns = ["Total", "East", "West"]
    return data