import psycopg2
import sys
from datetime import datetime

from sqlalchemy import create_engine
import pandas as pd 
import numpy as np 

import pickle
from pybaseball import statcast_pitcher

df = pd.read_pickle('2018_ids.pkl')


engine = create_engine('postgresql+psycopg2://taylorphillips@localhost/pitches_2018')


def pand(df):
    frames = []
    for index, value in df.iterrows():
        frame = statcast_pitcher('2018-02-01', '2018-12-01', player_id = df['key_mlbam'][index])
        frames.append(frame)
    result = pd.concat(frames)
    return result


def pipe(df):
    for idx, val in df.iterrows():
        data = statcast_pitcher('2018-02-01', '2018-12-01', player_id = df['key_mlbam'][idx])
        data.to_sql('pitches', engine, if_exists='append')
    