#Web navigation stuff
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

#Basics
import numpy as np
import sys

#Calendar stuff
from CalendarFetch import ValidDate

stock_name = "amd"

year = 2020
month = 5
day = 1

browser = webdriver.Chrome(ChromeDriverManager().install())

td = open("test_label.txt", "w", encoding='UTF-8')

while day <= ValidDate.number_of_days_in_month(month):
    print(day)

    if ValidDate.operable_day(year, month, day) == 1:
        sauce = 'https://bigcharts.marketwatch.com/historical/default.asp?symb=amd&closeDate=' + str(month) + '%2F' + str(
            day) + '%2F' + str(year) + '&x=0&y=0'
        browser.get(sauce)

        ClosingPrice = browser.find_element_by_xpath('//*[@id="historicalquote"]/tbody/tr[3]/td').text
        OpeningPrice = browser.find_element_by_xpath('//*[@id="historicalquote"]/tbody/tr[4]/td').text
        Pourcentage = 100*(1-(float(ClosingPrice)/float(OpeningPrice)))
        print(str(Pourcentage) + "%")
        #td.write(str(Pourcentage) + "\n")

    day+=1