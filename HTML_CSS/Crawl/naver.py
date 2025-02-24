import requests
from bs4 import BeautifulSoup

base_url='https://search.naver.com/search.naver?ssc=tab.blog.all&sm=tab_jum&query='
keyword=input("검색할 키워드 : ") #검색어

url=base_url+keyword
req=requests.get(url)

html=req.text
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