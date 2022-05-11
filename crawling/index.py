from bs4 import BeautifulSoup
import requests
from datetime import datetime

url = "http://rank.ezme.net/"
response = requests.get(url)
soup = BeautifulSoup(response.content.decode('utf-8','replace'), 'html.parser')
rank = 1

results = soup.findAll('b')

favorsch = open("rankresult.txt", "w")

print(datetime.today().strftime("%Y년 %m월 %d일의 실시간 검색어 순위입니다.\n"))

for result in results:
    if rank > 10 :
        break
    favorsch.write(str(rank) + "위 " + result.get_text() + "\n")
    print(rank,"위 : ",result.get_text(),"\n")
    rank += 1

favorsch.close() 