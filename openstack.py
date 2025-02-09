from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import time

class openstackDashboard:
    def __init__ (self, driver=None):
        """
        Initializes the OpenStackDashboard instance.
        If no driver is provided, it creates a new Chrome WebDriver instance.
        """
        if driver is None:
            self.driver = webdriver.Chrome()
        else: 
            self.driver = driver

    def login(self, userName, passWord, url):
        self.driver.get(url)
        time.sleep(2)

        login_input = self.driver.find_element(By.ID,'id_username')
        password_input = self.driver.find_element(By.ID, 'id_password')
        login_btn = self.driver.find_element(By.ID, "loginBtn")

        login_input.send_keys(userName)
        password_input.send_keys(passWord)
        login_btn.click()
    
    def select_project(self, project_name):
        project_dropdown = self.driver.find_element(By.CLASS_NAME, "dropdown-toggle")
        project_dropdown.click()

        xpath_anchor = f"//span[contains(text(), '{project_name}')]//.."
        anchor = self.driver.find_element(By.XPATH, xpath_anchor)
        anchor.click()

    def goToNetwork(self):
        network_anchor_xPath = r'//*[@id="sidebar-accordion-project"]/li[3]/a'
        network_anchor  = self.driver.find_element(By.XPATH,network_anchor_xPath)
        network_anchor.click()

    def goToNetworksSection(self):
        networksTab_anchor_xPath = "//div[@id='sidebar-accordion-project-network']//a[2]"
        networksTab_anchor  = self.driver.find_element(By.XPATH,networksTab_anchor_xPath)
        networksTab_anchor.click()

    def createNetwork(self, networkName, subnetName, subnet,gatewayIp):
        time.sleep(2)
        create_network_btn = self.driver.find_element(By.ID, "networks__action_create")
        create_network_btn.click()

        network_name = self.driver.find_element(By.XPATH, "//input[@id='id_net_name']")
        network_name.send_keys(networkName)

        next_btn = self.driver.find_element(By.XPATH,"//*[@id='modal_wrapper']/div/form/div/div/div[3]/div/div/button[2]")
        next_btn.click()

        subnet_name = self.driver.find_element(By.ID, "id_subnet_name")
        subnet_name.send_keys(subnetName)

        cidr = self.driver.find_element(By.ID,"id_cidr")
        cidr.send_keys(subnet)

        gateway = self.driver.find_element(By.ID,"id_gateway_ip")
        gateway.send_keys(gatewayIp)
        next_btn.click()

        dns = self.driver.find_element(By.ID,"id_dns_nameservers")
        dns.send_keys("8.8.8.8")

    def quit(self):
        self.driver.quit()
