
from numpy import asfortranarray
from pandas import read_csv
from parameters import pls_path


def read_pls_table():
    """Read the standard attributes table saved in csv format. 
       Return numpy array (shape=(ntraits, npls), F_CONTIGUOUS)"""
    assert pls_path.exists()
    return asfortranarray(read_csv(pls_path).__array__()[:,1:].T)