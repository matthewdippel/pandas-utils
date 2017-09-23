__author__ = 'mdippel'
import pandasutils.plots.plotutils as plotutil
import pandasutils.descriptives.descriptivestatistics as desc
import os
import pandas as pd

def check_make_folder(folder_fname):
    if not os.path.exists(folder_fname):
        os.makedirs(folder_fname)

def run_all_scripts(df, root_folder):
    check_make_folder(root_folder)
    fname = root_folder + '/descriptive_histograms/'
    check_make_folder(fname)
    desc.create_descriptive_histograms(df, fname)
    
    fname = root_folder + '/numeric_scatterplots/'
    check_make_folder(fname)
    desc.create_all_numeric_scatterplots(df, fname)
    
    fname = root_folder + '/categorical_distributions/'
    check_make_folder(fname)
    desc.create_all_categorical_split_distributions(df, fname)
    
    fname = root_folder + '/heatmaps/'
    check_make_folder(fname)
    desc.create_correlation_heatmaps(df, fname)
    
    
    from contextlib import redirect_stdout
    
    text_folder = root_folder + '/text_descriptipns/'
    check_make_folder(text_folder)
    with open(text_folder + 'descriptions.txt', 'w') as f:
        with redirect_stdout(f):
            desc.print_descriptive_statistics(df)
            
    with open(text_folder + 'missing_fields.txt', 'w') as f:
        with redirect_stdout(f):
            print(desc.create_missing_fields_count(df))
            
if __name__ == "__main__":
    dir = os.path.dirname(os.path.abspath(__file__))
    iris_df = pd.read_csv(dir + "/../sampledata/iris.csv")
    run_all_scripts(df=iris_df, root_folder='/Users/mdippel/run_all_test')