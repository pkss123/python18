from selenium import webdriver
import time
from bs4 import BeautifulSoup
import codecs

f = codecs.open("e:/crawler/result.txt", encoding="utf-8", mode="w")

driver = webdriver.Chrome('e:/crawler/chromedriver.exe')

driver.get("http://www.kyobobook.co.kr/bestSellerNew/bestseller.laf?orderClick=d79")
time.sleep(3)

source = driver.page_source

titlelist = []
authorlist = []
pricelist = []

s1 = BeautifulSoup(source,"html.parser")
s2 = s1.find_all("div", class_="title")
for data in s2[4:]:
    print(data.text.strip())
s3 = s1.find_all("div", class_="author")
for data in s3:
    print(data.text.strip().replace("\t", ""))
s4 = s1.find_all("div", class_="price")
for data in s4:
    print(data.text.strip())
time.sleep(5)
    
for idx in range(len(titlelist)):
    f.write(str(idx+1)+"등 도서 정보\r\n")
    f.write(titlelist[idx]+"\r\n")
    f.write(authorlist[idx]+"\r\n")
    f.write(pricelist[idx]+"\r\n")
    f.write("-"*50+"\r\n")
driver.close()