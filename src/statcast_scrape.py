import pandas as pd 
import numpy as np 

from pybaseball import *

def statcast_season(year):
    '''
    function that generates statcast pitch data for a given year(minimum 2015)
    input : 
        year(int) : yyyy
    return: 
        pandas dataframe 
    '''
    # may crash depending on connection and computer
    # run one month at a time if needed
    march = statcast('{}-03-01'.format(year), '{}-03-31'.format(year))
    april = statcast('{}-04-01'.format(year), '{}-04-30'.format(year))
    may = statcast('{}-05-01'.format(year), '{}-05-31'.format(year))
    june = statcast('{}-06-01'.format(year), '{}-06-30'.format(year))
    july = statcast('{}-07-01'.format(year), '{}-07-31'.format(year))
    aug = statcast('{}-08-01'.format(year), '{}-08-31'.format(year))
    sept = statcast('{}-09-01'.format(year), '{}-09-30'.format(year))
    octo = statcast('{}-10-01'.format(year), '{}-10-31'.format(year))
    nov = statcast('{}-11-01'.format(year), '{}-11-30'.format(year))

    total = pd.concat([march,april,may,june,july,aug,sept,octo,nov])
    #drop pitches that weren't classified, not useful for this project
    copy = total.dropna(subset=['pitch_type'])

    return copy

def bbref_season(year):
    '''
    function do generate baseball-reference pitching statistics for each day in given season(year)
    input : 
        year(int) : yyyy
    return: 
        pandas dataframe 
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
            # functionality test
            print(time)
            frame = pitching_stats_range(time, time)
            frame['date'] = time
            frames = frames.append(frame)
        except:
            # except statement for all-star-game errors
            print('error/no mlb games today: ', time)
            continue
    frames['date'] = pd.to_datetime(frames['date'], format="%Y/%m/%d")
    frames.columns = [x.lower().strip() for x in frames.columns]
    frames = frames.set_index(np.arange(len(frames)))
    return frames