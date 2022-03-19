from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
def initDriver(filePath):
  chromeOption = webdriver.chromeOptions()
  # config chrome with Path
  chromeOption.add_argument(
    "user-data-dir=" + filePath)
  driver = webdriver.Chrome('./chromedriver', Option = chromeOption)
  return driver
