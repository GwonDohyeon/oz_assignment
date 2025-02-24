from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import time

header="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36"

base_url='https://search.naver.com/search.naver?ssc=tab.blog.all&sm=tab_jum&query='
keyword="손흥민"#input("검색할 키워드 : ") #검색어

url=base_url+keyword
options_=Options()
options_.add_argument(f"User-Agent={header}")
options_.add_experimental_option("detach",True)
options_.add_experimental_option("excludeSwitches",["enable-automation"])
driver = webdriver.Chrome(options=options_)
driver.get(url)

for i in range(5):
    driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
    time.sleep(1)
    
html=driver.page_source

soup=BeautifulSoup(html,"html.parser")
results=soup.select(".view_wrap")# select_one은 가장 상단에 있는 정보 가져오고 select는 모든 정보를 가져온다

for index,i in enumerate(results,start=1):
    title=i.select_one(".title_link").text
    link=i.select_one(".title_link")["href"]
    writer=i.select_one(".name").text
    dsc=i.select_one(".dsc_link").text
    
    print(index)
    print(title)
    print(link)
    print(writer)
    print(dsc)

driver.quit()