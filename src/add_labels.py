import pandas as pd
import numpy as np
import pickle
import re
import datetime as dt

from pybaseball import *


games_18 = pd.read_pickle('../pickles/2018_apps_ids.pkl')
games_17 = pd.read_pickle('../pickles/2017_apps_ids.pkl')
games_16 = pd.read_pickle('../pickles/2016_apps_ids.pkl')
games_15 = pd.read_pickle('../pickles/2015_apps_ids.pkl')


games_18['date'] = pd.to_datetime(games_18['date'])
games_17['date'] = pd.to_datetime(games_17['date'])
games_16['date'] = pd.to_datetime(games_16['date'])
games_15['date'] = pd.to_datetime(games_15['date'])


games_18 = games_18.sort_values(by=['key_mlbam', 'date'])
games_17 = games_17.sort_values(by=['key_mlbam', 'date'])
games_16 = games_16.sort_values(by=['key_mlbam', 'date'])
games_15 = games_15.sort_values(by=['key_mlbam', 'date'])

inj_18 = pd.read_pickle('../pickles/2018_inj_ids.pkl')
inj_17 = pd.read_pickle('../pickles/2017_inj_ids.pkl')
inj_16 = pd.read_pickle('../pickles/2016_inj_ids.pkl')
inj_15 = pd.read_pickle('../pickles/2015_inj_ids.pkl')

merge_18 = games_18.merge(inj_18, on='key_mlbam', how='left')
merge_17 = games_17.merge(inj_17, on='key_mlbam', how='left')
merge_16 = games_16.merge(inj_16, on='key_mlbam', how='left')
merge_15 = games_15.merge(inj_15, on='key_mlbam', how='left')

merge_18 = merge_18.sort_values(by=['key_mlbam', 'date'])
merge_17 = merge_17.sort_values(by=['key_mlbam', 'date'])
merge_16 = merge_16.sort_values(by=['key_mlbam', 'date'])
merge_15 = merge_15.sort_values(by=['key_mlbam', 'date'])

merge_18['days_preceeding'] = merge_18['startdate'] - merge_18['date']
merge_17['days_preceeding'] = merge_17['startdate'] - merge_17['date']
merge_16['days_preceeding'] = merge_16['startdate'] - merge_16['date']
merge_15['days_preceeding'] = merge_15['startdate'] - merge_15['date']

merge_18['days_rest'] = merge_18['date'] - merge_18['date'].shift()
merge_17['days_rest'] = merge_17['date'] - merge_17['date'].shift()
merge_16['days_rest'] = merge_16['date'] - merge_16['date'].shift()
merge_15['days_rest'] = merge_15['date'] - merge_15['date'].shift()

merge_18_inj = merge_18[merge_18['days_preceeding'].notnull()]
merge_17_inj = merge_17[merge_17['days_preceeding'].notnull()]
merge_16_inj = merge_16[merge_16['days_preceeding'].notnull()]
merge_15_inj = merge_15[merge_15['days_preceeding'].notnull()]

merge_18_noinj = merge_18[merge_18['days_preceeding'].isnull()]
merge_17_noinj = merge_17[merge_17['days_preceeding'].isnull()]
merge_16_noinj = merge_16[merge_16['days_preceeding'].isnull()]
merge_15_noinj = merge_15[merge_15['days_preceeding'].isnull()]

id_list_18 = merge_18_inj['key_mlbam'].unique().tolist()
id_list_17 = merge_17_inj['key_mlbam'].unique().tolist()
id_list_16 = merge_16_inj['key_mlbam'].unique().tolist()
id_list_15 = merge_15_inj['key_mlbam'].unique().tolist()

frames_18 = pd.DataFrame()
for id in id_list_18:
    frame = merge_18_inj[merge_18_inj['key_mlbam'] == id]
    try:
        inj_index = frame.index[frame['days_preceeding'] < dt.timedelta(0)][0]-1
    except:
        inj_index = frame.tail(1).index.item()
    frame.at[inj_index, 'injured?'] = 1
    frames_18 = frames_18.append(frame)
    frames_18 = frames_18.drop_duplicates(keep=False)
df_18 = frames_18.append(merge_18_noinj)
df_18 = df_18.sort_values(by=['key_mlbam', 'date'])

frames_17 = pd.DataFrame()
for id in id_list_17:
    frame = merge_17_inj[merge_17_inj['key_mlbam'] == id]
    try:
        inj_index = frame.index[frame['days_preceeding'] < dt.timedelta(0)][0]-1
    except:
        inj_index = frame.tail(1).index.item()
    frame.at[inj_index, 'injured?'] = 1
    frames_17 = frames_17.append(frame)
    frames_17 = frames_17.drop_duplicates(keep=False)
df_17 = frames_17.append(merge_17_noinj)
df_17 = df_17.sort_values(by=['key_mlbam', 'date'])


frames_16 = pd.DataFrame()
for id in id_list_16:
    frame = merge_16_inj[merge_16_inj['key_mlbam'] == id]
    try:
        inj_index = frame.index[frame['days_preceeding'] < dt.timedelta(0)][0]-1
    except:
        inj_index = frame.tail(1).index.item()
    frame.at[inj_index, 'injured?'] = 1
    frames_16 = frames_16.append(frame)
    frames_16 = frames_16.drop_duplicates(keep=False)
df_16 = frames_16.append(merge_16_noinj)
df_16 = df_16.sort_values(by=['key_mlbam', 'date'])


frames_15 = pd.DataFrame()
for id in id_list_15:
    frame = merge_15_inj[merge_15_inj['key_mlbam'] == id]
    try:
        inj_index = frame.index[frame['days_preceeding'] < dt.timedelta(0)][0]-1
    except:
        inj_index = frame.tail(1).index.item()
    frame.at[inj_index, 'injured?'] = 1
    frames_15 = frames_15.append(frame)
    frames_15 = frames_15.drop_duplicates(keep=False)
df_15 = frames_15.append(merge_15_noinj)
df_15 = df_15.sort_values(by=['key_mlbam', 'date'])


