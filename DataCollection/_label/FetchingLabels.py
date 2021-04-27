from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import numpy as np
import sys

stock_name = "amd"

year = 20
month = 5
day = 1

browser = webdriver.Chrome(ChromeDriverManager().install())
td = open("../_data/test_label", "w", encoding='UTF-8')

sauce = 'https://bigcharts.marketwatch.com/historical/default.asp?symb=amd&closeDate=' + str(month) + '%2F' + str(
    day) + '%2F' + str(year) + '&x=0&y=0'

browser.get(sauce)
while day <= 31:
    try:
        ClosingPrice = browser.find_element_by_xpath('//*[@id="historicalquote"]/tbody/tr[3]/td').text
        OpeningPrice = browser.find_element_by_xpath('//*[@id="historicalquote"]/tbody/tr[4]/td').text
        Pourcentage = 100*(1-(float(ClosingPrice)/float(OpeningPrice)))
        print(str(Pourcentage) + "%")
        td.write(str(Pourcentage) + "\n")

    except Exception as e:
        td.write("\n")
        print(e)
    sauce = 'https://bigcharts.marketwatch.com/historical/default.asp?symb=amd&closeDate=' + str(month) + '%2F' + str(
        day) + '%2F' + str(year) + '&x=0&y=0'
    browser.get(sauce)
    print(day)
    day +=1
print(day)