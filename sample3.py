from selenium import webdriver
from selenium.webdriver.common.by import By
 
# create webdriver object
driver = webdriver.Chrome()
 
 
# get geeksforgeeks.org
driver.get("https://www.geeksforgeeks.org/")
 