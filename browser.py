'''
login method will do the followings:

(1)Open browser (chrome)
(2)Open site 
(3)will explicit wait not more than 10s 
(4)enter login details
(5)gets kapacha text from kepacha.py 
(6)clicks login

'''
import kook

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import Select

#from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os

chrome_options = Options()
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')

#driver.get("https://www.google.com/")

def login():
  global driver  
  driver = webdriver.Chrome(options=chrome_options)
  #driver = webdriver.Edge(service=Service(x))
  
  
  driver.get("https://schoolattendancegujarat.in/")
  
  #waiting 10s for login buttion to show up
  WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "btnLogin")))
  
  #finding all webElements
  uname = driver.find_element(by='id',value='UserName')
  upass = driver.find_element(by='id',value='Password')
  captcha_box = driver.find_element(by='id',value='captcha')
  login_button = driver.find_element(by='id',value='btnLogin')
  
  
  #creating a new file named kepacha.png and saving
  #..it from webpage
    
  with open('kepacha.png' , 'wb') as kepacha:
      kepacha.write(
            driver.find_element(
            by='xpath',value = '//*[@id="divlogin"]/form/div[3]/img').screenshot_as_png)
  
  
  #filling up the details
  uname.send_keys(os.getenv('uname'))
  upass.send_keys(os.getenv('pass'))
  kepacha_text = kook.kepacha()
  captcha_box.send_keys(kepacha_text)
  
  login_button.click()

def update_data(absent_students):
  driver.get("https://schoolattendancegujarat.in/Students/Create")
  WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, "Attendance")))
  
  list_of_path = driver.find_elements(
    by='xpath', value='//*[@id="Attendance"]')

  
  for i in absent_students:
    Select(list_of_path[i-1]).select_by_index(1)
  submitBtn = driver.find_element(by='xpath',value='//*[@id="divData"]/div/div/div[2]/input')
  submitBtn.click()
  

def ss():
  driver.find_elements(
    By.CLASS_NAME, 'panel')[0].screenshot(
    "success.png"
    )
def close():
  driver.close()
  driver.quit()
