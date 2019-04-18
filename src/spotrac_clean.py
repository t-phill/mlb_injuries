import pandas as pd
import numpy as np
import pickle
import re

# clean injury csv created from spotrac_scrape.py

def clean_inj(file, year):
    '''
    function to clean injury data created in spotrac_scrape.py
    applies needed regex functions, creates start_date feature
    
    input:
        file: name (csv)
        year: int (yyyy)
    output:
        pandas dataframe
        
    '''
    inj = pd.read_csv(file)
    inj['Year'] = year
    inj['Status'] = inj.Status.str[9:]
    DL_df = inj.copy()
    DL_df['List'], DL_df['Status'] = DL_df['Status'].str.split('|', 1).str
    DL_df['Dates'], DL_df['Status'] = DL_df['Status'].str.split('|', 1).str
    DL_df['StartDate'], DL_df['EndDate'] = DL_df['Dates'].str.split('-', 1).str
    DL_df['Dates'] = DL_df['Dates'].str.replace('..-day', '')
    DL_df['MoneyEarned'] = DL_df['Money_Earned'].str[1:]
    DL_df['MoneyEarned'] = DL_df['MoneyEarned'].str.replace(',', '')
    del DL_df['Dates']
    del DL_df['Status']
    del DL_df['Money_Earned']
    DL_df['Player'] = DL_df['Player'].str.lower()
    DL_df['List'] = DL_df['List'].str.replace('-day', '', regex=True)
    dates = []
    df = DL_df
    df.columns = map(str.lower, df.columns)
    for idx, val in df.iterrows():
        val.startdate = str(val.year)+val.startdate
        dates.append(val.startdate)

    dates = [x.rstrip() for x in dates]
    dates = [x.replace(' ','/') for x in dates]
    df['startdate'] = dates
    df['startdate'] = pd.to_datetime(df['startdate'], infer_datetime_format=True)
    
    lasts = []
    firsts = []

    for row in df.iterrows():
        name = row[1][0]
        name = jr_replace(name)
        name = title_replace(name)
        index = row[0]
        first = name.split()[0]
        first = correction2(first).rstrip()
        firsts.append(first)
        last = name.split()[-1]
        lasts.append(last)
    
    df['last'] = lasts
    df['first'] = firsts
    df['player'] = df['player'].str.lower()
    df['player'] = df['player'].str.replace('.', '')
    df['player'] = df['player'].str.replace("'", '')
    df['player'] = df['player'].str.replace(' ', '')
    df.rename(columns={'player': 'name'}, inplace=True)
    
    return df

def jr_replace(x):
    #removes 'jr' from names
    match = re.sub(r'jr$',"",x)
    return match

def title_replace(x):
    #removes titles
    match = re.sub(r'iii$',"",x)
    return match

def correction2(string):
    #function to make initialed names consistent
    corstr = re.sub('\ +',' ',string)
    final = re.sub('\.','. ',corstr)
    return final

