from selenium import webdriver
from selenium.webdriver.common.by import By
import time

#setting up the webdriver
driver = webdriver.Chrome()

#get the link
driver.get("https://web.whatsapp.com/")
time.sleep(70)

#search/find the contact
search=driver.find_element(By.XPATH,'//*[@id="side"]/div[1]/div/div/div[2]/div/div[1]/p')
search.send_keys("01117376548")
time.sleep(10)
contact=driver.find_element(By.XPATH,'//*[@id="pane-side"]/div[1]/div/div/div[11]/div/div/div/div[2]/div[1]/div[1]/span[1]')
contact.click()
time.sleep(10)

#type 10 message
for i in range (10):
   message_type=driver.find_element(By.XPATH,'//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[1]/p')
   message_type.send_keys("Hello")
   send_button=driver.find_element(By.XPATH,'//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[2]/button/span')
   send_button.click()
time.sleep(1000)