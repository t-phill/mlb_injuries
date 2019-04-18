import pandas as pd 
import numpy as np 

from pybaseball import *

def pitches_season(year):
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
    copy = total.dropna(subset=['pitch_type'])

    return copy



