from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

driver.get("http://118.67.215.11/dashboard/auth/login")

### Login to openstack ###

### Login Fields ###
login_input = driver.find_element(By.ID,'id_username')
password_input = driver.find_element(By.ID, 'id_password')
login_btn = driver.find_element(By.ID, "loginBtn")


### action: Username, password and submit ###
login_input.send_keys("core-system")
password_input.send_keys(r'b#R!l1#!@nTC1$0uDC0$r3$y2$0#32m5')
login_btn.click()



project_dropdown = driver.find_element(By.CLASS_NAME,"dropdown-toggle")
project_dropdown.click()


project_ul = driver.find_elements(By.CLASS_NAME, "dropdown-title")
for project in project_ul:
    print(project.text)


project_name = "mosiur-cloud"


anchor_xpath = (
    f"//a[.//span[contains(@class, 'context-project') and normalize-space(text())='{project_name}']]"
)

anchor = driver.find_element(By.XPATH, anchor_xpath)
print(anchor.get_attribute('outerHTML'))

time.sleep(5)

driver.quit()