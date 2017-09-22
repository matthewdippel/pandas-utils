import matplotlib.pyplot as plt
__author__ = 'mdippel'


def prettify_axis(ax):
    ax.patch.set_facecolor('grey')
    ax.patch.set_alpha(0.5)
    ax.grid(linestyle='-', linewidth='0.5', color='white')
    
def pretty_scatter(df, x, y):
    ax = df.plot(kind='scatter', x=x, y=y)
    prettify_axis(ax)
    plt.show()
    
def pretty_bar(seq):
    ax = seq.plot(kind='bar')
    prettify_axis(ax)
    plt.show()

def pretty_histogram(df, col):
    ax = df[col].plot(kind='hist', bins=100)
    ax.set_xlabel(col)
    prettify_axis(ax)
    plt.show()
    
if __name__ == "__main__":
    import pandas as pd
    import os
    dir = os.path.dirname(os.path.abspath(__file__))
    iris_df = pd.read_csv(dir + "/../sampledata/iris.csv")
    #ax = iris_df.plot()
    #prettify_axis(ax)
    numeric_columns = ['sepal_length', 'sepal_width', 'petal_length', 'petal_width']
    #for c1 in numeric_columns:
    #    for c2 in numeric_columns:
    #        pretty_scatter(iris_df, c1, c2)
    for c in numeric_columns:
        pretty_histogram(iris_df, c)
    