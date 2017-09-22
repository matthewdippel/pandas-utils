__author__ = 'mdippel'
import numpy as np
pdu = __import__("pandas-utils")

def print_descriptive_statistics(df):
    for col in df:
        print(col)
        print('-----')
        print("type: %s" % str(df[col].dtype))
        if df[col].dtype == np.float64 or df[col].dtype == np.int64:
            print(df[col].describe())
        else:
            print("unique count: %s" % str(df[col].nunique()))
            print(df[col].unique())
        print("")
    
def create_descriptive_histograms(df):
    for col in df:
        pdu.plots.plotutils.pretty_histogram(df, col)


if __name__ == "__main__":
    import pandas as pd
    import os
    dir = os.path.dirname(os.path.abspath(__file__))
    iris_df = pd.read_csv(dir + "/../sampledata/iris.csv")
    
    print_descriptive_statistics(iris_df)
    create_descriptive_histograms(iris_df)