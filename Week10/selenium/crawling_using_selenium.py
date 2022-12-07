from bs4 import BeautifulSoup
from selenium import webdriver
import time

# url = "http://v.media.daum.net/v/20161103113844417"
url = "http://v.media.daum.net/v/20161120134647462"

driver = webdriver.Chrome('chromedriver') # 'chromedriver 대신에 chromedriver의 경로를 제공 (예: c:\data\crawling\chromedriver.exe) 
driver.get(url)
time.sleep(3) # 전체 페이지가 로딩될 때까지 기다림.

# 댓글 열기 버튼 누르기
driver.find_element_by_xpath("//button[@class='btn_foldup']").click()

found_element = True
while found_element:
    try:
        element = driver.find_element_by_xpath("//div[@class='alex_more']")
        element.click()
        time.sleep(3)

    except Exception:
        found_element = False

html = driver.page_source
soup = BeautifulSoup(html, "html.parser")

comments = soup.find_all("ul", class_="list_comment")
print(comments)
