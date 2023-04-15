import time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import csv
from checkdistance import Checkdistance
from googledirections import distance_wst, distance_city
from csv import DictWriter
import os.path

cd = Checkdistance()

# Variables
URL = "https://www.rightmove.co.uk/"
chrome_webdriver_path = "/Users/USER/Desktop/chromedriver_win32/chromedriver.exe"
rent_button = "/html/body/div/div[2]/main/div[1]/div/div/div/button[2]"
input_field = '/html/body/div/div[2]/main/div[1]/div/div/div/div/input'
location = "WC1"
price_min = "1,750 PCM"
price_max = "2,500 PCM"
beds_min = "3"
desired_time = 50
miles = "Within 10 miles"

# Parsed data
field_names = ['image', 'Name', "westminister", "City UOL", 'Price', 'Bedrooms', 'Bathrooms', "link"]
rental_properties = []

path = './rentals.csv'

check_file = os.path.isfile(path)

if not check_file:
    with open('rentals.csv', 'w', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=field_names)
        writer.writeheader()

# prevent window from closing after execution
options = Options()
options.add_experimental_option("detach", True)
# initialization of webdriver with chrome webdriver and options above
service = Service(executable_path=chrome_webdriver_path)
driver = webdriver.Chrome(service=service, options=options)
# initialization of action chains
actions = ActionChains(driver)
# Maximised window to prevent any elements/popups not displaying properly
driver.maximize_window()
# requesting the URL required
driver.get(URL)
time.sleep(2)

# cookie handling
try:
    driver.find_element(By.CLASS_NAME, value="accept-cookies-button").click()
finally:
    time.sleep(3)
search_box = driver.find_element(By.XPATH, value=input_field)
search_box.send_keys(location)
driver.find_element(By.XPATH, value=rent_button).click()

# cookie handling
# try:
#     driver.find_element(By.CLASS_NAME, value="accept-cookies-button").click()
# finally:
#     time.sleep(3)

radius = driver.find_element(By.ID, value="radius")
radius.send_keys(miles)

max_price = driver.find_element(By.ID, value="minPrice")
max_price.send_keys(price_min)

max_price = driver.find_element(By.ID, value="maxPrice")
max_price.send_keys(price_max)

max_price = driver.find_element(By.ID, value="minBedrooms")
max_price.send_keys(beds_min)

driver.find_element(By.XPATH, value='/html/body/div[3]/div[2]/div/div[1]/div/form/fieldset[2]/div[4]/button').click()
time.sleep(4)

driver.find_element(By.XPATH, value='/html/body/div[3]/div[1]/form/div/button[2]').click()
time.sleep(1)

driver.find_element(By.XPATH,
                    value='/html/body/div[3]/div[1]/div[2]/div[1]/div[7]/div/div[1]/div[2]/div/div[2]/div[1]').click()
driver.find_element(By.XPATH,
                    value='/html/body/div[3]/div[1]/div[2]/div[1]/div[7]/div/div[1]/div[2]/div/div[2]/div[2]').click()
driver.find_element(By.XPATH,
                    value='/html/body/div[3]/div[1]/div[2]/div[1]/div[7]/div/div[1]/div[2]/div/div[2]/div[3]').click()
driver.find_element(By.XPATH, value='/html/body/div[3]/div[1]/div[2]/div[2]/div/div[3]/button').click()

# Adding Keywords-------------------------------------------------------------------------------------------------------
# driver.find_element(By.XPATH, value='/html/body/div[3]/div[2]/div[1]/div[2]/div[3]/div/div/div/div[2]/button').click()
# actions.send_keys("3 Bathrooms")
# actions.send_keys(Keys.ENTER)
# actions.perform()
# ----------------------------------------------------------------------------------------------------------------------

pages = int(
    driver.find_element(By.XPATH, value='/html/body/div[3]/div[2]/div[1]/div[3]/div/div/div/div[2]/span[3]').text)
time.sleep(5)
for page in range(0, pages):
# for page in range(0, 1):
    rentals_on_page = driver.find_elements(By.CLASS_NAME, value='l-searchResult')
    for rental in rentals_on_page:
        try:
            rent = {
                "image": rental.find_element(By.TAG_NAME, value='img').get_attribute("src"),
                "Name": rental.find_element(By.TAG_NAME, value="address").text,
                "link": rental.find_element(By.CLASS_NAME, value="propertyCard-link").get_attribute("href"),
                "westminister": distance_wst(rental.find_element(By.TAG_NAME, value="address").text),
                "City UOL": distance_city(rental.find_element(By.TAG_NAME, value="address").text),
                # "westminister": cd.distance_westminister(rental.find_element(By.TAG_NAME, value="address").text),
                # "City UOL": cd.distance_city(rental.find_element(By.TAG_NAME, value="address").text),
                "Price": rental.find_element(By.CLASS_NAME, value="propertyCard-priceValue").text,
                "Bedrooms": int(
                    rental.find_element(By.CLASS_NAME, value='property-information').find_elements(By.TAG_NAME,
                                                                                                   value="span")[
                        2].text),
                "Bathrooms": int(
                    rental.find_element(By.CLASS_NAME, value='property-information').find_elements(By.TAG_NAME,
                                                                                                   value="span")[
                        4].text),
            }
        except:
            rent = {
                "image": rental.find_element(By.TAG_NAME, value='img').get_attribute("src"),
                "Name": rental.find_element(By.TAG_NAME, value="address").text,
                "link": rental.find_element(By.TAG_NAME, value="a").get_attribute("href"),
                # "westminister": cd.distance_westminister(rental.find_element(By.TAG_NAME, value="address").text),
                # "City UOL": cd.distance_city(rental.find_element(By.TAG_NAME, value="address").text),
                "westminister": distance_wst(rental.find_element(By.TAG_NAME, value="address").text),
                "City UOL": distance_city(rental.find_element(By.TAG_NAME, value="address").text),
                "Price": rental.find_element(By.CLASS_NAME, value="propertyCard-priceValue").text,
                "Bedrooms": int(
                    rental.find_element(By.CLASS_NAME, value='property-information').find_elements(By.TAG_NAME,
                                                                                                   value="span")[
                        2].text),
                "Bathrooms": 0, }
        finally:
            # print(rent)
            if rent["westminister"] is None:
                rent["westminister"] = 0
            if rent["City UOL"] is None:
                rent["City UOL"] = 0
            if rent["Bathrooms"] > 1 and rent["westminister"] < desired_time and rent["City UOL"] < desired_time:
                rental_properties.append(rent)
                # Open CSV file in append mode
                # Create a file object for this file
                with open('rentals.csv', 'a', newline='') as f_object:
                    # Pass the file object and a list
                    # of column names to DictWriter()
                    # You will get a object of DictWriter
                    dictwriter_object = DictWriter(f_object, fieldnames=field_names)

                    # Pass the dictionary as an argument to the Writerow()
                    dictwriter_object.writerow(rental_properties[-1])

                    # Close the file object
                    f_object.close()
    driver.find_element(By.CLASS_NAME, value='pagination-direction--next').click()
    time.sleep(3)

# with open('rentals.csv', 'w', newline='') as csvfile:
#     writer = csv.DictWriter(csvfile, fieldnames=field_names)
#     writer.writeheader()
#     writer.writerows(rental_properties)
