
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.alert import Alert 
import time
import psycopg2


driver = webdriver.Chrome()

url="https://www.redbus.in/bus-tickets/goa-airport-to-calangute-goa?fromCityId=197221&toCityId=253650&fromCityName=Goa%20Airport&toCityName=Calangute%20(goa)&busType=Any&srcCountry=IND&destCountry=IND&onward=21-Jul-2024"

driver.get(url)
driver.maximize_window()
time.sleep(10)
button = driver.find_element(By.CLASS_NAME, "button")
button.click();

conn = psycopg2.connect(database = "postgres", 
                        user = "postgres", 
                        host= 'localhost',
                        password = "admin",
                        port = 5432)


cur = conn.cursor()

# cur.execute("""CREATE TABLE redbus(
#              id SERIAL PRIMARY KEY,
#              State VARCHAR(50),
#              route_name VARCHAR(100),
#              route_link VARCHAR(600),
#              busname VARCHAR (255),
#              bustype VARCHAR (255),
#              departing_time VARCHAR (10),
#              duration VARCHAR (10),
#              reaching_time VARCHAR (10),
#              star_rating VARCHAR (5),
#              price VARCHAR (5),
#              seats_available VARCHAR (35));
#              """)
# # # Make the changes to the database persistent
# conn.commit()
# # # Close cursor and communication with the database
# cur.close()
# conn.close()

ins_qry = "INSERT INTO public.redbus(State, route_name, route_link, busname, bustype, departing_time, duration, reaching_time, star_rating, price, seats_available) VALUES ("

for x in range(20):
	busname = driver.find_elements(By.XPATH, "//div[contains(@class,'column-two')]/div[contains(@class,'travels')]")
	bustype = driver.find_elements(By.XPATH, "//div[contains(@class,'column-two')]/div[contains(@class,'bus-type')]")
	departing_time = driver.find_elements(By.XPATH, "//div[contains(@class,'column-three')]/div[contains(@class,'dp-time')]")
	duration = driver.find_elements(By.XPATH, "//div[contains(@class,'column-four')]/div[contains(@class,'dur ')]")
	reaching_time = driver.find_elements(By.XPATH, "//div[contains(@class,'column-five')]/div[contains(@class,'bp-time')]")
	star_rating = driver.find_elements(By.XPATH, "//div[contains(@class,'column-six')]//div[contains(@class,'rating-sec')]//span")
	price = driver.find_elements(By.XPATH, "//div[contains(@class,'column-seven')]//div[@class='fare d-block']/span")
	seats_available = driver.find_elements(By.XPATH, "//div[contains(@class,'column-eight')]//div[contains(@class,'seat-left')]")

	for i in range(len(departing_time)):
		data = "'KTCL','goa-airport-to-calangute-goa'"+ ",'" + url + "', '"  + busname[i].text + "', '" + bustype[i].text + "', '" + departing_time[i].text + "', '" + duration[i].text + "', '" + reaching_time[i].text + "', '" + star_rating[i].text + "', '" + price[i].text + "', '" + seats_available[i].text + "')"
		qry = ins_qry + data
		print(qry)

		cur.execute(qry)
		conn.commit()

	driver.execute_script("window.scrollBy(0,300)")
	time.sleep(3)

cur.close()
conn.close()