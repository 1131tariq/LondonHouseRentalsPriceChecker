import time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By


class Checkdistance():
    def __init__(self):
        self.dist = "/html/body/div[3]/div[9]/div[3]/div[1]/div[2]/div/div[2]/div/div/div/div[3]/button/div[1]"
        self.city = "https://www.google.com/maps/dir//City,+University+of+London,+Northampton+Square,+London,+UK/@51.5472113,0.0533506,12z/data=!4m8!4m7!1m0!1m5!1m1!1s0x48761ca7b1d83351:0x570d19c20ab22a83!2m2!1d-0.1024624!2d51.5279719?hl=en"
        self.westminister = "https://www.google.com/maps/dir//University+of+Westminster+-+Cavendish+Campus,+New+Cavendish+Street,+London,+UK/@51.5209138,-0.2101328,12z/data=!4m8!4m7!1m0!1m5!1m1!1s0x48761ad602153b7d:0x7cae57b547cdf178!2m2!1d-0.1400932!2d51.5209347?hl=en"
        self.chrome_webdriver_path = "/Users/USER/Desktop/chromedriver_win32/chromedriver.exe"
        self.options = Options()
        self.options.add_argument("−−lang=es")

    def distance_city(self, rental):
        self.driver = webdriver.Chrome(executable_path=self.chrome_webdriver_path, options=self.options)
        self.actions = ActionChains(self.driver)
        self.driver.maximize_window()
        self.driver.get(self.city)
        time.sleep(2)
        # same for both functions
        self.actions.send_keys(rental)
        self.actions.send_keys(Keys.ENTER)
        self.actions.perform()
        time.sleep(4)
        time_needed = self.driver.find_element(By.XPATH, value=self.dist).text
        time.sleep(2)
        try:
            transit_time = int(time_needed.split(' ', 1)[0])
            return transit_time
        except:
            return time_needed.split(' ', 1)[0]

    def distance_westminister(self, rental):
        self.driver = webdriver.Chrome(executable_path=self.chrome_webdriver_path, options=self.options)
        self.actions = ActionChains(self.driver)
        self.driver.maximize_window()
        self.driver.get(self.westminister)
        time.sleep(2)
        # same for both functions
        self.actions.send_keys(rental)
        self.actions.send_keys(Keys.ENTER)
        self.actions.perform()
        time.sleep(4)
        time_needed = self.driver.find_element(By.XPATH, value=self.dist).text
        time.sleep(2)
        try:
            transit_time = int(time_needed.split(' ', 1)[0])
            return transit_time
        except:
            print(time_needed.split(' ', 1)[0])


