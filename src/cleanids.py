from pybaseball import *
import numpy as np
import pandas as pd
import pickle
import re 

season_range = pd.read_pickle('../pickles/agg_games.pkl')

def agg_year(year):
    season = pitching_stats_bref(season=year)
    season.columns = map(str.lower, season.columns)
    season['name'] = season['name'].str.lower()
    season['name'] = season['name'].str.replace('.', '')
    season['name'] = season['name'].str.replace(' ', '')
    season['name'] = season['name'].str.strip()
    season['name'] = season['name'].apply(jr_replace)
    season['name'] = season['name'].apply(title_replace)

    return season



def clean_ids(file):
    ids = pd.read_pickle(file)
    ids['name_last'] = ids['name_last'].str.replace('.', '')
    ids['name_last'] = ids['name_last'].str.replace(' ', '')
    ids['name_last'] = ids['name_last'].str.strip()
    ids['name_first'] = ids['name_first'].str.replace('.', '')
    ids['name_first'] = ids['name_first'].str.replace(' ', '')
    ids['name_first'] = ids['name_first'].str.strip()

    ids['name'] = 0
    for idx, val in ids.iterrows():
        ids['name'][idx] = ids['name_first'][idx] + '' + ids['name_last'][idx]

    ids = ids.drop(['name_last', 'name_first'], axis=1)
    return ids 



def big_merge(season, ids):
    df = season.merge(ids, on='name', how='outer')
    filtered_df = df[df['lev'].isnull()]
    print(len(filtered_df))

    for row in filtered_df.iterrows():
        player = str(row[1][0])
        try:
            index = season.loc[season['name'].str.contains(player[-5:])].index[0]
            season.set_value(index, 'name', player)
        except:
            index = season.loc[season['name'].str.contains(player[-4:])].index[0]
            season.set_value(index, 'name', player)
            continue
    if len(filtered_df) == 0:
        print('successfully filtered')
        df = season.merge(ids, on='name', how='outer')

    return df, filtered_df

def jr_replace(x):
    match = re.sub(r'jr$',"",x)
    return match

def title_replace(x):
    match = re.sub(r'iii$',"",x)
    return match


if __name__ == '__main__':
    season = agg_year(2018)
    ids = clean_ids('../pickles/2018_ids.pkl')
    df, filtered_df = big_merge(season, ids)