import numpy as np
import pandas as pd
import pickle

import requests
from bs4 import BeautifulSoup

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import random

import time
import csv

import re

import os
chromedriver = "/Applications/chromedriver"
os.environ["webdriver.chrome.driver"] = chromedriver


driver = webdriver.Chrome(chromedriver)
driver.get("http://www.brooksbaseball.net/landing.php?player=592094")


playercarddict = {}
df = pd.read_pickle('2018_ids.pkl')
# df = df.set_index(np.arange(len(df)))
    
for index, row in df.iterrows():
    try:
        player = df.iloc[index]['name_first'] + ' ' + df.iloc[index]['name_last']
        playerid = df.iloc[index]['key_mlbam']
        
        page = "http://www.brooksbaseball.net/landing.php?player=" + str(playerid)

        driver.get(page)
        
        soup = BeautifulSoup(driver.page_source, 'html.parser')
        row = soup.find(class_='well').find('p').text.strip()
        
        
        playercarddict[player] = row
    except:
        continue

with open('playercard.pkl', 'wb+') as handle:
    pickle.dump(playercarddict, handle, protocol=pickle.HIGHEST_PROTOCOL)