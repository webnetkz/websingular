from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from bs4 import BeautifulSoup
import urllib

# Получает webdriver
def get_new_webdriver(url):
  options = webdriver.ChromeOptions() # Создание объекта настроек
  options.add_argument('headless') # Активация скрытого режима

  EXE_PATH = "./driver" # Путь до драйвера
  driver = webdriver.Chrome(executable_path=EXE_PATH, chrome_options=options)

  driver.get(url)
  return driver

# Получает суп страницы
def get_soup(url):
  driver = get_new_webdriver(url)
  time.sleep(3)
  soup = BeautifulSoup(driver.page_source, 'html.parser')
    
  return soup
