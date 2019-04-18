import pandas as pd 
import numpy as np 

from pybaseball import *

pitchers = pitching_stats_range("2015-03-01", "2018-11-01")

pitchers.columns = map(str.lower, pitchers.columns)

pitchers = clean_games(pitchers)

df = pd.DataFrame()


for idx, val in pitchers.iterrows():
    first = str(pitchers['first'][idx])
    last = str(pitchers['last'][idx])
    key = playerid_lookup(last, first)
    print(first, last)
    df = df.append(key)

def clean_games(season):
    firsts = []
    lasts = []
    season = season
    season.columns = map(str.lower, season.columns)
    season['name'] = season['name'].str.lower()
    
    for row in season.iterrows():
        name = row[1][0]
        name = jr_replace(name)
        name = title_replace(name)
        index = row[0]
        first = name.split()[0]
        first = correction2(first).rstrip()
        firsts.append(first)
        last = name.split()[-1]
        lasts.append(last)
    
    season['first'] = firsts
    season['last'] = lasts

    season['name'] = season['name'].str.replace('.', '')
    season['name'] = season['name'].str.replace("'", '')
    season['name'] = season['name'].str.replace(' ', '')
    season['name'] = season['name'].str.strip()
    season['name'] = season['name'].apply(correction2)
    season['name'] = season['name'].apply(jr_replace)
    season['name'] = season['name'].apply(title_replace)

    return season