import matplotlib.pyplot as plt
import seaborn as sns
__author__ = 'mdippel'


def prettify_axis(ax):
    ax.patch.set_facecolor('grey')
    ax.patch.set_alpha(0.5)
    ax.grid(linestyle='-', linewidth='0.5', color='white')
    
def pretty_scatter(df, x, y):
    plt.clf()
    ax = df.plot(kind='scatter', x=x, y=y)
    prettify_axis(ax)
    return ax
    
def pretty_bar(seq):
    plt.clf()
    ax = seq.plot(kind='bar')
    prettify_axis(ax)
    return ax

def pretty_histogram(df, col):
    plt.clf()
    ax = sns.distplot(df[col], bins=100)
    ax.set_xlabel(col)
    prettify_axis(ax)
    return ax

def categorical_distribution(df, data_col, cat_col):
    plt.clf()
    import pandas as pd
    data = pd.concat([df[data_col], df[cat_col]])
    ax = sns.boxplot(x=cat_col, y=data_col, data=df)
    prettify_axis(ax)
    return ax

def correlation_matrix_heatmap(df):
    plt.clf()
    corrmat = df.corr()
    ax = sns.heatmap(corrmat, vmax=1.0, vmin=-1.0, square=True, cmap='RdBu_r')
    return ax
    
def correlation_with_column_topk_heatmap(df, col, k):
    plt.clf()
    corrmat = df.corr()
    cols = corrmat.nlargest(k, col)[col].index
    cm = np.corrcoef(df[cols].values.T)
    sns.set(font_scale=1.25)
    ax = sns.heatmap(cm, cbar=True, annot=True, square=True, fmt='.2f', annot_kws={'size': 10},
                     yticklabels=cols.values, xticklabels=cols.values)
    return ax

def pairwise_scatterplot(df, cols):
    plt.clf()
    sns.set()
    ax = sns.pairplot(df[cols], size=2.5)
    return ax
    
def save_ax_as_file(ax, fname):
    fig = ax.get_figure()
    if fname is not None:
        fig.savefig(fname)

    
if __name__ == "__main__":
    import pandas as pd
    import os
    import numpy as np
    dir = os.path.dirname(os.path.abspath(__file__))
    iris_df = pd.read_csv(dir + "/../sampledata/iris.csv")
    #ax = iris_df.plot()
    #prettify_axis(ax)
    numeric_columns = ['sepal_length', 'sepal_width', 'petal_length', 'petal_width']
    #for c1 in numeric_columns:
    #    for c2 in numeric_columns:
    #        pretty_scatter(iris_df, c1, c2)
    
    correlation_matrix_heatmap(iris_df)
    for c in numeric_columns:
        pretty_histogram(iris_df, c)
        plt.clf()
    
    for col in iris_df:
        if not (iris_df[col].dtype == np.float64 or iris_df[col].dtype == np.int64):
            for data_col in numeric_columns:
                ax = categorical_distribution(iris_df, data_col, col)
                plt.show()
                plt.clf()
    
    