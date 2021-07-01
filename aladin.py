from selenium import webdriver
import time
from bs4 import BeautifulSoup
import codecs

f = codecs.open("e:/crawler/test.txt", encoding="utf-8", mode="a")

driver = webdriver.Chrome('e:/crawler/chromedriver.exe')

driver.get("https://www.aladin.co.kr/shop/common/wbest.aspx?BranchType=1&start=we")
time.sleep(3)

source = driver.page_source

s1 = BeautifulSoup(source,"html.parser")
s2 = s1.find_all("div",class_="ss_book_box")

rank = 0

for item in s2:
    rank += 1
    f.write(str(rank) +"위 도서\r\n")
    li = item.find_all("li")
    if len(li) < 8:
        f.write(li[0].text + "\r\n")
        f.write(li[1].text + "\r\n")
        f.write(li[2].text + "\r\n")
    else:
        f.write(li[1].text + "\r\n")
        f.write(li[2].text + "\r\n")
        f.write(li[3].text + "\r\n")
    f.write("-"*50 + "\r\n")
driver.close()