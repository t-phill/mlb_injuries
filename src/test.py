# from pybaseball import *
import numpy as np
import pandas as pd
import pickle


filtered_df = pd.read_pickle('/Users/taylorphillips/galvanize/mlb/mlb_injuries/src/filtered_df.pkl')

ids_sub = pd.read_pickle('/Users/taylorphillips/galvanize/mlb/mlb_injuries/src/ids_sub.pkl')

for index, value in filtered_df.iterrows():
    for i in range(-3, -10):
        results = ids_sub[ids_sub['name'].str.contains(str(filtered_df['name'].values[0][i:]))]
        if len(results) == 1:
            filtered_df['name'][index] = results['name'].values[0]