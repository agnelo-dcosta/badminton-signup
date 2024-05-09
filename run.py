from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

urls = [

    'http://www.seattlebadmintonclub.com/Login.aspx' 
        
        ]
s = Service(r"chromedriver")

for url in urls:
    driver = webdriver.Chrome(service=s)
    driver.get(url)

XPATH_username='/html/body/form/div[3]/table/tbody/tr[4]/td/div/div/table/tbody/tr/td/table/tbody/tr/td/table/tbody/tr[3]/td/input'
XPATH_password='/html/body/form/div[3]/table/tbody/tr[4]/td/div/div/table/tbody/tr/td/table/tbody/tr/td/table/tbody/tr[5]/td/input'
XPATH_login = '/html/body/form/div[3]/table/tbody/tr[4]/td/div/div/table/tbody/tr/td/table/tbody/tr/td/table/tbody/tr[8]/td/input'

driver.find_element(By.XPATH,XPATH_username).send_keys('agnelo.dcosta')
sleep(2)
driver.find_element(By.XPATH,XPATH_password).send_keys('July2017!')
sleep(2)
driver.find_element(By.XPATH,XPATH_login).click()
sleep(2)

XPATH_fixed = '/html/body/form/div[3]/table/tbody/tr[4]/td/div/h3/table/tbody/tr[3]/td/label'
XPATH_enter = '/html/body/form/div[3]/table/tbody/tr[4]/td/div/h3/input'
driver.find_element(By.XPATH,XPATH_fixed).click()
sleep(2)
driver.find_element(By.XPATH,XPATH_enter).click()
sleep(2)

XPATH_date = '/html/body/form/div[3]/table/tbody/tr[4]/td/div/div/select'

print("date drop down text %s", driver.find_element(By.XPATH,XPATH_date).text)

sleep(1000)

