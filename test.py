from selenium import webdriver
import  time
##############
#把下面兩行改成你的email帳密，不然會error
mail_address = 'change at here'
password = 'change at here'

###################
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
driver = webdriver.Edge('./msedgedriver')
#driver.get("http://www.google.com") # 更改網址以前往不同網頁
#
#element.send_keys('classroom')
#element.send_keys('\ue007')
#time.sleep(3)
url = 'https://classroom.google.com/u/0/c/MzcwNjc0MzM3NTUx'
driver.get(url)
driver.find_element_by_id("identifierId").send_keys(mail_address)
driver.find_element_by_id("identifierNext").click()
time.sleep(2.5)
driver.find_element_by_name("password").send_keys(password)
driver.find_element_by_id("passwordNext").click()
time.sleep(7)
titles = driver.find_elements_by_class_name("ZjCSDe.dDKhVc.pco8Kc.j70YMc")
sort_of_article = 1
for title in titles:
    print("第", '(', sort_of_article, ')', "新的文章\n")
    print(title.text)

    sort_of_article = sort_of_article + 1

#driver.close()
