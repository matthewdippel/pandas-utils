__author__ = 'mdippel'
import numpy as np
import pandas as pd
from pandasutils.plots import plotutils as plotutils

def print_descriptive_statistics(df):
    for col in df:
        print(col)
        print('-----')
        print("type: %s" % str(df[col].dtype))
        if df[col].dtype == np.float64 or df[col].dtype == np.int64:
            print(df[col].describe(percentiles=[.1, .2, .3, .4, .5, .6, .7, .8, .9]))
            print("Skewness: %f" % df[col].skew())
            print("Kurtosis: %f" % df[col].kurt())
        else:
            print(df[col].unique())
            print(df[col].describe())
        print("")


def create_descriptive_histograms(df, save_dir):
    for col in df:
        #print(df[col])
        if df[col].dtype == np.float64 or df[col].dtype == np.int64:
            ax = plotutils.pretty_histogram(df, col)
            fname = None
            if save_dir is not None:
                fname = save_dir + "histogram-%s.pdf" % col
            plotutils.save_ax_as_file(ax, fname)
        else:
            seq = df[col].value_counts()
            ax = plotutils.pretty_bar(seq)
            fname = None
            if save_dir is not None:
                fname = save_dir + "histogram-%s.pdf" % col
            plotutils.save_ax_as_file(ax, fname)
    return

def create_all_numeric_scatterplots(df, save_dir):
    numeric_columns = []
    for col in df:
        if df[col].dtype == np.float64 or df[col].dtype == np.int64:
            numeric_columns.append(col)
    for i in range(len(numeric_columns)):
        for j in range(i):
            c1 = numeric_columns[i]
            c2 = numeric_columns[j]
            ax = plotutils.pretty_scatter(df, c1, c2)
            fname = None
            if save_dir is not None:
                fname = save_dir + "scatter-%s-vs-%s.pdf" % (c1, c2)
            plotutils.save_ax_as_file(ax, fname)

def create_all_categorical_split_distributions(df, save_dir):
    numeric_columns = []
    object_columns = []
    for col in df:
        if df[col].dtype == np.float64 or df[col].dtype == np.int64:
            numeric_columns.append(col)
        elif df[col].dtype == np.object or df[col].dtype == np.str:
            object_columns.append(col)
    for cat_col in object_columns:
        for data_col in numeric_columns:
            ax = plotutils.categorical_distribution(df, data_col=data_col, cat_col=cat_col)
            fname = None
            if save_dir is not None:
                fname = save_dir + "categorical-%s-cut_on-%s.pdf" % (data_col, cat_col)
            plotutils.save_ax_as_file(ax, fname)


def create_missing_fields_count(df):

    total = df.isnull().sum().sort_values(ascending=False)
    percent = (df.isnull().sum() / df.isnull().count()).sort_values(ascending=False)
    missing_data = pd.concat([total, percent], axis=1, keys=['Total', 'Percent'])
    return missing_data

def create_correlation_heatmaps(df, save_dir):
    ax = plotutils.correlation_matrix_heatmap(df)
    fname = None
    if save_dir is not None:
        fname = save_dir + "correlation_heatmap_all.pdf"
    plotutils.save_ax_as_file(ax, fname)
    
def create_topk_corr_heatmap(df, col, k, save_dir):
    ax = plotutils.correlation_with_column_topk_heatmap(df, col, k)
    fname = None
    if save_dir is not None:
        fname = save_dir + "correlation_heatmap_with_%s_top%s.pdf" % (col, str(k))
    plotutils.save_ax_as_file(ax, fname)
    

if __name__ == "__main__":
    import pandas as pd
    import os
    dir = os.path.dirname(os.path.abspath(__file__))
    iris_df = pd.read_csv(dir + "/../sampledata/iris.csv")

    print_descriptive_statistics(iris_df)
    create_descriptive_histograms(iris_df, '/Users/mdippel/test_plots/')
    create_all_numeric_scatterplots(iris_df, '/Users/mdippel/test_plots/')
    create_all_categorical_split_distributions(iris_df, '/Users/mdippel/test_plots/')
    print(create_missing_fields_count(iris_df))