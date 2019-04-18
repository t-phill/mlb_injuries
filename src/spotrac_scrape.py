import numpy as np
import pandas as pd

import requests
from bs4 import BeautifulSoup

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

import random
import time
import csv
import re
import os

# Python script scraping spottrac injury data

chromedriver = "/Applications/chromedriver"
os.environ["webdriver.chrome.driver"] = chromedriver

driver = webdriver.Chrome(chromedriver)
# Alter link for desired year
driver.get("https://www.spotrac.com/mlb/disabled-list/2018/cumulative-player/pitching/")

# Choose file name
with open('dl_list_2018.csv', 'w',newline='') as csvfile:
    file = csv.writer(csvfile)
    file.writerow(['Player', 'Posititon', 'Team', 'Injury', 'Status', 'Days', 'Money_Earned'])
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    rows = soup.find_all(class_='parent')
    # Change row slicing based on year
    rows = rows[68:]

    players = []
    dl_data = []

    for row in rows:
        player = row.find('a').text
        players.append(player)
        injury = row.find_all(class_='center')
        for info in injury:
            inj = info.text
            dl_data.append(inj)
        
    positions = []
    teams = []
    injuries = []
    status = []
    days = []
    money = []
    
    for index, item in enumerate(dl_data):
        if index%6 == 0:
            positions.append(item)
            
    dl_data = dl_data[1:]

    for index, item in enumerate(dl_data):
        if index%6 == 0:
            teams.append(item)
    
    dl_data = dl_data[1:]

    for index, item in enumerate(dl_data):
        if index%6 == 0:
            injuries.append(item)
            
    dl_data = dl_data[1:]

    for index, item in enumerate(dl_data):
        if index%6 == 0:
            status.append(item)
    
    dl_data = dl_data[1:]
    
    for index, item in enumerate(dl_data):
        if index%6 == 0:
            days.append(item)
    
    dl_data = dl_data[1:]

    for index, item in enumerate(dl_data):
        if index%6 == 0:
            money.append(item)
    
    # Year dependent
    for num in np.arange(0,339):
            
        observation = [players[num], positions[num], teams[num], injuries[num], status[num], days[num], money[num]]
        file.writerow(observation)