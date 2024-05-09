from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

import smtplib, ssl

urls = [

    'http://www.seattlebadmintonclub.com/Login.aspx' 
        
        ]
s = Service(r"chromedriver")

for url in urls:
    driver = webdriver.Chrome(service=s)
    driver.get(url)

# Login page
XPATH_username='/html/body/form/div[3]/table/tbody/tr[4]/td/div/div/table/tbody/tr/td/table/tbody/tr/td/table/tbody/tr[3]/td/input'
XPATH_password='/html/body/form/div[3]/table/tbody/tr[4]/td/div/div/table/tbody/tr/td/table/tbody/tr/td/table/tbody/tr[5]/td/input'
XPATH_login = '/html/body/form/div[3]/table/tbody/tr[4]/td/div/div/table/tbody/tr/td/table/tbody/tr/td/table/tbody/tr[8]/td/input'

driver.find_element(By.XPATH,XPATH_username).send_keys('agnelo.dcosta')
sleep(2)
driver.find_element(By.XPATH,XPATH_password).send_keys('July2017!')
sleep(2)
driver.find_element(By.XPATH,XPATH_login).click()
sleep(2)

# Ladder selection 
XPATH_fixed = '/html/body/form/div[3]/table/tbody/tr[4]/td/div/h3/table/tbody/tr[3]/td/label'
XPATH_enter = '/html/body/form/div[3]/table/tbody/tr[4]/td/div/h3/input'
driver.find_element(By.XPATH,XPATH_fixed).click()
sleep(2)
driver.find_element(By.XPATH,XPATH_enter).click()
sleep(2)

ladder_date = ""

while ladder_date == "" :
    # Fixed partner ladder
    XPATH_date = '/html/body/form/div[3]/table/tbody/tr[4]/td/div/div/select'

    try:
        ladder_date = driver.find_element(By.XPATH,XPATH_date).text
    except:
        ladder_date = ""

    print(f"date drop down text {ladder_date}")
    if ladder_date == "" :
        sleep(10000)


# if any ladder_date is available send email
port = 465  # For SSL
smtp_server = "smtp.gmail.com"
sender_email = "penpalshivani24@gmail.com"  # Enter your address
receiver_email = "agnelo.m.dcosta@gmail.com"  # Enter receiver address
app_pass = "" # Enter valid password
message = f"""\
Subject: Ladder Open for {ladder_date}

Please sign up for Ladder!!!!!!!!!!!!!

HURRY UP
- Aggi
"""

context = ssl.create_default_context()
with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
    server.login(sender_email, app_pass)
    server.sendmail(sender_email, receiver_email, message)


sleep(1000)

