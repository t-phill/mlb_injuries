from pybaseball import *
import numpy as np
import pandas as pd
import pickle
import re 
import datetime

season_range = pd.read_pickle('../pickles/agg_games.pkl')

# keys_clean = keys_clean.sort_values(by='name_last')
# keys_clean = keys_clean.set_index(np.arange(len(keys_clean)))

def generate_games(year):
    '''
    function do generate baseball-reference pitching statistics for each day in given season(year)
    
    input : 2018
    return: pandas dataframe 
    '''
    start_date = '{}-04-01'.format(year)
    times = list()
    start = datetime.datetime.strptime("{}-03-29".format(year), "%Y-%m-%d")
    end = datetime.datetime.strptime("{}-10-29".format(year), "%Y-%m-%d")
    date_generated = [start + datetime.timedelta(days=x) for x in range(0, (end-start).days)]
    for date in date_generated:
        date = str(date.strftime("%Y-%m-%d"))
        times.append(date)
    frames = pd.DataFrame()
    for time in times:
        try:
            print(time)
            frame = pitching_stats_range(time, time)
            frame['date'] = time
            frames = frames.append(frame)
        except:
            print('errorrrrr: ', time)
            continue
    frames = frames
    return frames

# def clean_games():
#     firsts = []
#     lasts = []
#     season = frames
#     season.columns = map(str.lower, season.columns)
#     season['name'] = season['name'].str.lower()



def agg_year(year):
    firsts = []
    lasts = []
    season = pitching_stats_bref(season=year)
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

def merge(season, ids):
    df = season.merge(ids, on='name', how='left')
    dups = df.duplicated(subset='name', keep=False)
    print(len(df[dups]))
    to_add = test[test['mlb_played_last'].isnull()]
    return to_add

def clean_ids(file):
    ids = pd.read_pickle(file)
    ids['name_last'] = ids['name_last'].str.replace('.', '')
    ids['name_last'] = ids['name_last'].str.replace("'", '')
    ids['name_last'] = ids['name_last'].str.replace(' ', '')
    ids['name_last'] = ids['name_last'].str.strip()
    ids['name_first'] = ids['name_first'].str.replace('.', '')
    ids['name_first'] = ids['name_first'].str.replace("'", '')
    ids['name_first'] = ids['name_first'].str.replace(' ', '')
    ids['name_first'] = ids['name_first'].str.strip()

    ids['name'] = 0
    for idx, val in ids.iterrows():
        ids['name'][idx] = ids['name_first'][idx] + '' + ids['name_last'][idx]

    # ids = ids.drop(['name_last', 'name_first'], axis=1)
    return ids 

def add_to_dict_df():
    add_frame = pd.DataFrame()
    for row in to_add.iterrows():
        name = row[1][0]
        first = row[1][40]
        index = row[0]
        lookup = keys_clean[keys_clean['name'].str.contains(to_add['last'].loc[index])]
        if len(lookup) == 1:
            ins_index = lookup.index[0]
            lookup.set_value(ins_index, 'name_first', first)
            add_frame = add_frame.append(lookup)
    return add_frame

def add_to_dict_manual():
    add_frame = pd.DataFrame()
    for row in to_add.iterrows():
        name = row[1][0]
        first = row[1][40]
        index = row[0]
        lookup = keys_clean[keys_clean['name'].str.contains(to_add['last'].loc[index])]
        print(lookup)
        ins_index = int(input())
        lookup.set_value(ins_index, 'name_first', first)
        add_frame = add_frame.append(lookup)
    return add_frame


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

def correction2(string):
    corstr = re.sub('\ +',' ',string)
    final = re.sub('\.','. ',corstr)
    return final

if __name__ == '__main__':
    season = agg_year(2018)
    ids = clean_ids('../pickles/2018_ids.pkl')
    df, filtered_df = big_merge(season, ids)