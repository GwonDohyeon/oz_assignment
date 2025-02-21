from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import time
import pymysql
import pymysql.cursors

header="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36"
url="https://kream.co.kr"
options_=Options()
options_.add_argument(f"User-Agent={header}")
options_.add_experimental_option("detach",True)
options_.add_experimental_option("excludeSwitches",["enable-automation"])
driver = webdriver.Chrome(options=options_)
driver.get(url)

driver.find_element(By.CSS_SELECTOR,".btn_search.header-search-button.search-button-margin").click()
driver.find_element(By.CSS_SELECTOR,".input_search.show_placeholder_on_focus").send_keys("슈프림")
driver.find_element(By.CSS_SELECTOR,".input_search.show_placeholder_on_focus").send_keys(Keys.RETURN)

for i in range(30):
    driver.find_element(By.TAG_NAME,'body').send_keys(Keys.PAGE_DOWN)
    time.sleep(0.5)

html=driver.page_source
soup=BeautifulSoup(html,"html.parser")
items=soup.select(".item_inner")
item_list=[]
for item in items:
    name=item.select_one(".translated_name").text
    if "후드" in name:
        category="상의"
        product_brand=item.select_one(".product_info_brand.brand").text
        price=item.select_one(".text-lookup.bold.display_paragraph.line_break_by_truncating_tail").text
        print(category,product_brand,name,price,sep="\n")
        item_info=[category,product_brand,name,price]
        item_list.append(item_info)
print(item_list)
driver.quit()
connection=pymysql.connect(
    host='localhost',
    user='root',
    password='1234',
    db='kream',
    charset='utf8mb4',
    cursorclass=pymysql.cursors.DictCursor
)

connection.cursor()

def execute_query(connection,query,args=None):
    with connection.cursor() as cursor:
        cursor.execute(query,args or ())
        if query.strip().upper().startswith('select'):
            return cursor.fetchall()
        else:
            connection.commit()
            
for i in item_list:
    execute_query(connection,"insert into kream (category,brand,name,price) values (%s,%s,%s,%s)",(i[0],i[1],i[2],int(i[3].replace(",","")[:-1])))