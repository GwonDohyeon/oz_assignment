from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import time

header="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36"
url="https://kream.co.kr"
options_=Options()
options_.add_argument(f"User-Agent={header}")
options_.add_experimental_option("detach",True)
options_.add_experimental_option("excludeSwitches",["enable-automation"])
driver = webdriver.Chrome(options=options_)
driver.get(url)

