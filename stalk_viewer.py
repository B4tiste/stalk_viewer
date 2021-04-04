# -*- coding: utf-8 -*-
"""
Created on Mon Oct 19 10:28:17 2020

@author: batiste w./Ludo
"""

from selenium import webdriver
import time
import os
import json


def clear(): return os.system('cls')


def stalk():
    clear()
    url = 'https://tmi.twitch.tv/group/user/b4tiste_sw/chatters'

    options = webdriver.ChromeOptions()
    options.add_argument("-headless")
    options.add_argument("-disable-gpu")

    chrome = webdriver.Chrome(
        "Ressources/chromedriver.exe", chrome_options=options)

    chrome.get(url)

    clear()

    time.sleep(2)

    json_viewers = chrome.find_element_by_xpath("/html/body/pre").text

    chrome.quit()

    # Open an write in the Json file
    f_json = open('viewer.json', 'w')
    f_json.write(json_viewers)
    f_json.close()

    # Open the Json file
    f_json = open('viewer.json')

    # Load the content of the file
    data = json.load(f_json)

    f_json.close()

    # data est un dictionnaire, on l'utilise comme un tableau :

    print("\n")
    print("\tMods (" + str(len(data['chatters']['moderators'])) + ") : ")
    for i in range(len(data['chatters']['moderators'])):
        print(data['chatters']['moderators'][i])

    print("\n")

    print("\tViewer (" + str(len(data['chatters']['viewers'])) + ") : ")
    for i in range(len(data['chatters']['viewers'])):
        print(data['chatters']['viewers'][i])
