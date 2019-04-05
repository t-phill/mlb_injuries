import pandas as pd 
import numpy as np 

from pybaseball import *

unique_pitchers = pitching_stats_range("2015-03-01", "2018-11-01")

unique_pitchers.columns = map(str.lower, unique_pitchers.columns)

df = pd.DataFrame()

for idx, val in unique_pitchers.iterrows():
    try:
        first = unique_pitchers['Name'][idx].split()[0]
        last = unique_pitchers['Name'][idx].split()[1]
        data = playerid_lookup(last, first)
        df = df.append(data)
    except:
        print('error: ', first, last)
        continue