import requests
from bs4 import BeautifulSoup

header={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36"}

url="https://www.melon.com/chart/index.htm"
req=requests.get(url,headers=header)

html=req.text
soup=BeautifulSoup(html,"html.parser")

lst50=soup.select(".lst50")
lst100=soup.select(".lst100")

lst=lst50+lst100

for rank,i in enumerate(lst,1):
    title=i.select_one(".ellipsis.rank01 a").text
    singer = i.select_one(".checkEllipsis").text
    album = i.select_one(".ellipsis.rank03 a").text

    print(f"[순위] : {rank}")
    print(f"[제목] : {title}")
    print(f"[가수] : {singer}")
    print(f"[앨범] : {album}")
    print()
