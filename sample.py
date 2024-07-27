from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.alert import Alert 
import time
import psycopg2
driver = webdriver.Chrome()


#url ="https://www.redbus.in/bus-tickets/kozhikode-to-bangalore?fromCityId=74661&toCityId=122&fromCityName=Kozhikode&toCityName=Bangalore&busType=Any&onward=18-Jul-2024"
#url = "https://www.redbus.in/bus-tickets/kozhikode-to-ernakulam?fromCityId=74661&toCityId=216&fromCityName=Kozhikode&toCityName=Ernakulam&busType=Any&srcCountry=IND&destCountry=IND&onward=19-Jul-2024"
#url="https://www.redbus.in/bus-tickets/ernakulam-to-kozhikode?fromCityId=216&toCityId=74661&fromCityName=Ernakulam&toCityName=Kozhikode&busType=Any&srcCountry=IND&destCountry=IND&onward=08-Aug-2024"
#url="https://www.redbus.in/bus-tickets/kozhikode-to-mysore?fromCityId=74661&toCityId=129&fromCityName=Kozhikode&toCityName=Mysore&busType=Any&srcCountry=IND&destCountry=IND&onward=05-Sep-2024"
#url="https://www.redbus.in/bus-tickets/kozhikode-to-thiruvananthapuram?fromCityId=74661&toCityId=71425&fromCityName=Kozhikode&toCityName=Thiruvananthapuram&busType=Any&srcCountry=IND&destCountry=IND&onward=15-Aug-2024"
#url="https://www.redbus.in/bus-tickets/bangalore-to-kalpetta?fromCityId=122&toCityId=606&fromCityName=Bangalore&toCityName=Kalpetta%20(kerala)&busType=Any&onward=06-Aug-2024&srcCountry=IND&destCountry=IND"
url="https://www.redbus.in/bus-tickets/jammu-to-srinagar?fromCityName=Jammu&fromCityId=734&toCityId=84913&toCityName=Srinagar%20%28J%20and%20K%29&srcCountry=&destCountry=&doj=19-Jul-2024&step=srp"

driver.get(url);
driver.maximize_window()
time.sleep(10)

# button = driver.find_element(By.CLASS_NAME, "button")
# button.click();

99999

# travels = driver.find_elements(By.XPATH, "//div[contains(@class,'column-two')]/div[contains(@class,'travels')]")
# bus_type = driver.find_elements(By.XPATH, "//div[contains(@class,'column-two')]/div[contains(@class,'bus-type')]")
# tm = driver.find_elements(By.XPATH, "//div[contains(@class,'column-three')]/div[contains(@class,'dp-time')]")
# duration = driver.find_elements(By.XPATH, "//div[contains(@class,'column-four')]/div[contains(@class,'dur ')]")
# reach_time = driver.find_elements(By.XPATH, "//div[contains(@class,'column-five')]/div[contains(@class,'bp-time')]")
# rating = driver.find_elements(By.XPATH, "//div[contains(@class,'column-six')]//div[contains(@class,'rating-sec')]//span")
# price = driver.find_elements(By.XPATH, "//div[contains(@class,'column-seven')]//div[@class='fare d-block']/span")
# seats_avbl = driver.find_elements(By.XPATH, "//div[contains(@class,'column-eight')]//div[contains(@class,'seat-left')]")



travels = driver.find_elements(By.XPATH, "//*[@id="23012454"]/div/span[4]/span[1]/span")