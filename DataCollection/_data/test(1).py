from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

stock_name = "amd"

date1n = 1
date2n = 1

browser = webdriver.Chrome(ChromeDriverManager().install())
browser.get(
    "https://www.google.com/search?q=" + stock_name + "&safe=active&rlz=1C1CHBF_frCA876CA876&sxsrf=ALeKk01oZItMHeAZzztAjzkYP9nSFO7CMg:1597540874634&source=lnms&tbm=nws&sa=X&ved=2ahUKEwiX2uLCx57rAhWul3IEHZQ5DC0Q_AUoAnoECBoQBA&biw=1707&bih=838&dpr=1.13")

Tools = browser.find_element_by_xpath('//*[@id="hdtb-tls"]')  # Tools
Tools.send_keys(Keys.RETURN)

while date1n <= 30:
    date1 = "4/" + str(date1n) + "/2020"
    date2 = "4/" + str(date2n) + "/2020"

    Recent = WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="hdtbMenus"]/div/div[3]'))) #Recent
    Recent.send_keys(Keys.RETURN)

    button = WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="cdrlnk"]'))) #Custom Range
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
