import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import pickle
import re
import datetime as dt

from pybaseball import *

from sklearn.ensemble import RandomForestClassifier
from sklearn.datasets import make_classification
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler

import psycopg2
import pandas.io.sql as psql
from sqlalchemy import create_engine

pd.set_option('display.max_columns', 500)
pd.set_option('display.max_rows', 200)


df_18 = pd.read_pickle('../pickles/2018_games_labeled.pkl')
df_17 = pd.read_pickle('../pickles/2017_games_labeled.pkl')
df_16 = pd.read_pickle('../pickles/2016_games_labeled.pkl')
df_15 = pd.read_pickle('../pickles/2015_games_labeled.pkl')
merge = pd.read_pickle('../pickles/labeled_games_agg.pkl')



conn = psycopg2.connect(dbname='statcast', user='taylorphillips', host='localhost')
cur = conn.cursor()

return_frame = pd.DataFrame()

id_list = df_18['key_mlbam'].unique().tolist()

for id in id_list:
    fastballs = psql.read_sql('''
    SELECT COUNT(pitch_type) as {0}_count, game_date as date, p_throws, AVG(release_speed) as {0}_release_speed,
    AVG(effective_speed) as {0}_percieved_speed, AVG(release_spin_rate) as {0}_spin_rate, 
    AVG(release_pos_x) as {0}_avg_x, AVG(release_pos_z) as {0}_avg_z, AVG(release_extension) as {0}_avg_extension,
    AVG(pfx_x) as {0}_x_movement, AVG(pfx_z) as {0}_z_movement 
    FROM pitches 
    WHERE pitcher = {1} AND pitch_type IN ('FF','FT', 'SI') 
    GROUP BY date, p_throws, pitcher
    ORDER BY date
    '''.format('fb', id), conn)

#     fastballs = psql.read_sql('''
#     SELECT COUNT(pitch_type) as {0}_count, game_date as date, p_throws
#     FROM pitches 
#     WHERE pitcher = {1} AND pitch_type IN ('FF','FT', 'SI')
#     GROUP BY date, p_throws
#     ORDER BY date
#     '''.format('fb', id), conn)
    
    offspeed = psql.read_sql('''
    SELECT COUNT(pitch_type) as {0}_count, game_date as date, p_throws, AVG(release_speed) as {0}_release_speed,
    AVG(effective_speed) as {0}_percieved_speed, AVG(release_spin_rate) as {0}_spin_rate, 
    AVG(release_pos_x) as {0}_avg_x, AVG(release_pos_z) as {0}_avg_z, AVG(release_extension) as {0}_avg_extension,
    AVG(pfx_x) as {0}_x_movement, AVG(pfx_z) as {0}_z_movement 
    FROM pitches 
    WHERE pitcher = {1} AND pitch_type IN ('FC', 'SL', 'FS', 'CH', 'KC', 'CU', 'FO', 'KN', 'SC', 'EP')
    GROUP BY date, p_throws, pitcher
    ORDER BY date
    '''.format('os', id), conn)
    
    frame = df_18[df_18['key_mlbam'] == id]
    
    fb_frame = frame.merge(fastballs, on='date', how='left')
    merge_frame = fb_frame.merge(offspeed, on='date', how='left')
    return_frame = return_frame.append(merge_frame)

return_frame.to_pickle('./retframe.pkl')