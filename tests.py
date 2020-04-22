from bs4 import BeautifulSoup
import requests
from xlwt import Workbook
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import code1
import re
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import validators

wb=Workbook()
wb1=Workbook()
sheet1=wb.add_sheet('sheet1')
sheet2=wb1.add_sheet('sheet1')
sheet1.write(0,0,'Name')
sheet2.write(0,0,'Name')
sheet1.col(0).width=8000
sheet2.col(0).width=8000
sheet1.write(0,1,'Website')
sheet2.write(0,1,'Phone Number')
sheet2.col(1).width=8000
sheet1.col(1).width=12000
sheet2.write(0,2,'Email')
sheet2.col(2).width=10000
global count1,count2
count2=count1=0
def begin(url):
    global count1,count2
    driver = webdriver.Chrome( r"D:\chromedriver")
    driver.get(url)
    count=0
    driver.maximize_window()
    driver.execute_script("window.scrollBy(0,100)","")
    python_button=driver.find_elements_by_class_name('resultSet.col-md-6.col-xs-12')
    print('buttons are',len(python_button))
    for i in python_button:
      count=count+1
      print(count)
      element = WebDriverWait(driver, 60).until(
          EC.visibility_of_element_located((By.CLASS_NAME, "ignore-click")))
      dau=i.get_attribute("data-enhanced-url")
      print(dau)
      if dau == "":
       count1=count1+1
       i.find_element_by_class_name('ignore-click').click()
       nurl = driver.current_url
       if url == nurl:
        element = WebDriverWait(driver, 60).until(
            EC.visibility_of_element_located((By.XPATH, "//*[@id='modalDetailCard']/div/div/div[1]/button"))
        )
        content=driver.page_source
        soup=BeautifulSoup(content,'html.parser')
        table = soup.find(class_='modal-title')
        name= table.contents[0]
        print(name)
        sheet1.write(count1,0,name)
        table=soup.find(class_='btn btn-default card-btn website')
        webs=table.get('href')
        valid=validators.url(webs)
        if valid:
            print(webs)
            sheet1.write(count1,1,webs)
        else:
            print('no website')
            sheet1.write(count1,1,'NONE')
        element.click()
       else:
          driver.back()
          time.sleep(10)
      else:
          count2=count2+1
          name1=code1.surgeon(1,dau)
          sheet2.write(count2,0,name1)
          ph=code1.surgeon(2,dau)
          sheet2.write(count2, 1, ph)
          email=code1.surgeon(3,dau)
          sheet2.write(count2, 2, email)

      driver.execute_script("window.scrollBy(0,110)", "")
      
    driver.close()
url="https://find.plasticsurgery.org/city/new-york/?page="
count=0
begin(url)
wb.save('doctors.xls')
wb1.save('surgeons.xls')