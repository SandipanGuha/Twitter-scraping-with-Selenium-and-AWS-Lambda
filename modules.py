# this will contain all libraries and modules needed for this project along with configurations ready
# configurations were done implicitly for replit environment 

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def configure_driver(url: str):
  
  chrome_options = Options()
  chrome_options.add_argument('--no-sandbox')
  chrome_options.add_argument('--headless')
  chrome_options.add_argument('--disable-dev-shm-usage')
  driver = webdriver.Chrome(options=chrome_options)
  driver.get(url)
  #import time
  #time.sleep(2)  #to properly load all the contents in given url
  try:
    WebDriverWait(driver,timeout=10).until(EC.title_is('Explore / Twitter'))
  except webdriver.TimeoutException:
    print("Error: URL didn't load correctly, please check your internet connection speed")
  return driver

import pandas
