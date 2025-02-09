import time
from openstack import openstackDashboard
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options



def main():
    options = Options()
    options.add_argument('--headless=new')
    driver = webdriver.Chrome(options=options)
 

    dashboard = openstackDashboard()
    url = "http://118.67.215.11/dashboard/auth/login"
    username = 'core-system'
    password = r'b#R!l1#!@nTC1$0uDC0$r3$y2$0#32m5'
    ### Login to openstack ###
    dashboard.login(userName=username,passWord=password,url=url)
    ### Login Fields ###
    dashboard.select_project('mosiur-cloud')
    dashboard.goToNetwork()
    dashboard.goToNetworksSection()
    dashboard.createNetwork("mosiur-4","subnet-1","10.10.100.0/24","10.10.100.1")



    time.sleep(5)
    dashboard.quit()


if __name__=='__main__':
    main()