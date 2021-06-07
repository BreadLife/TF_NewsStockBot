#Alexis Gagnon
#refait le 7 novembre 2020

#fonction:
#Collecting Data pour tout le mois d'avril
#Le programme prend tous les titres des articles sorties dans les 3 dernier jours d'une dates et les met dans une array faisant déja parti d'une array
#Puis lorsque tous les titres sont mit dans l'array, un autre programme va les traiter

#librairies:

#Navigation Web
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

#arrays
import numpy as np

#detection language
from langdetect import detect

#other
from CalendarFetch import ValidDate

#basic stuff
import sys
import time

stock_name = "amd"
year = 2020
month = 5
workday = 1

date1n = 1
date2n = 1

browser = webdriver.Chrome(ChromeDriverManager().install())
browser.get("https://www.google.com/search?q=" + stock_name + "&safe=active&rlz=1C1CHBF_frCA876CA876&sxsrf=ALeKk01oZItMHeAZzztAjzkYP9nSFO7CMg:1597540874634&source=lnms&tbm=nws&sa=X&ved=2ahUKEwiX2uLCx57rAhWul3IEHZQ5DC0Q_AUoAnoECBoQBA&biw=1707&bih=838&dpr=1.13")

browser.maximize_window()
browser.refresh()

Tools = browser.find_element_by_xpath('//*[@id="hdtb-tls"]')  # Tools
Tools.send_keys(Keys.RETURN)

td = open("test_data", "w", encoding='UTF-8')

# -*- coding: utf-8 -*-
def languageDetect(s):
    language = detect(s)
    return language

while date1n <= ValidDate.number_of_days_in_month(month):
    date1 = str(month) + "/" + str(date1n) + "/" + str(year)
    date2 = str(month) + "/" + str(date2n) + "/" + str(year)

    Recent = WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="hdtbMenus"]/span[1]/g-popup/div[1]'))) #Recent
    Recent.send_keys(Keys.RETURN)

    button = WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="lb"]/div/g-menu/g-menu-item[8]/div/div/span'))) #Custom Range
    button.click()

    parameter1 = browser.find_element_by_xpath('//*[@id="OouJcb"]') #Beginning of interval
    parameter1.clear()
    parameter1.send_keys(str(date1))

    parameter2 = browser.find_element_by_xpath('//*[@id="rzG2be"]') #End of interval
    parameter2.clear()
    parameter2.send_keys(str(date2))

    Enter = browser.find_element_by_xpath('//*[@id="T3kYXe"]/g-button') #Begin Search
    Enter.send_keys(Keys.RETURN)
    print(date1n)

    date1n +=1
    date2n +=1

    for i in range(1,11):
        try:
            info = browser.find_element_by_xpath('//*[@id="rso"]/div[' + str(i) +']/g-card/div/div/div[2]/a/div/div[2]').text
            str1 = info.splitlines()
            raw_arr = np.asarray(str1)
            ref_arr = np.delete(raw_arr, [0, 3])
            print(info)
            if (languageDetect(info) == "en"):
                print("Language: Anglais\n")
                # print(ref_arr)
                td.write(str(date1n - 1) + "\n")
                for w in ref_arr:
                    td.write(w + " ")
                td.write("\n")
            else :
                print("Language: autre\n")
                print("Mauvaise Langue")
        except Exception as e:
            print(e, "This was number: ", i, "in", raw_arr)
            #td.write(str(raw_arr))
    td.write("\n")