__author__ = 'mdippel'
import pandas as pd

def read_pickle_to_df(fname):
    return pd.read_pickle(fname)

def write_df_to_pickle(df, fname):
    pd.to_pickle(df, fname)