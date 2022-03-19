import
def initDriver(filePath):
  chromeOption = webdriver.chromeOptions()
  # config chrome with Path
  chromeOption.add_argument(
    "user-data-dir=" + filePath)
  driver = webdriver.Chrome('./chromedriver', Option = chromeOption)
  return driver
