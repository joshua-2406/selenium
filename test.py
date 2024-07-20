from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.alert import Alert 
from selenium.webdriver.common.action_chains import ActionChains
import time
import psycopg2
driver = webdriver.Chrome()
url="https://www.redbus.in/online-booking/ktcl/?utm_source=rtchometile"
driver.get(url)
driver.maximize_window()
time.sleep(10)
page=0
while True: 
    try:
        route = driver.find_element(By.CLASS_NAME,"route")
        route.click()
        print("Page Visited: ", page)
        driver.get(url)
    finally:
        print("All Page visited")
        
        
    













