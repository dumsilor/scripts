import time
from openstack import openstackDashboard
import tkinter as tk
from tkinter import ttk

url = "http://118.67.215.11/dashboard/auth/login"
username = 'core-system'
password = r'b#R!l1#!@nTC1$0uDC0$r3$y2$0#32m5'

result = {}

def gui():
    window = tk.Tk()
    window.geometry("750x250")
    window.title("Openstack Create Network")
    u_project = tk.StringVar()
    u_network = tk.StringVar()
    u_subnet = tk.StringVar()
    u_subnet_cidr = tk.StringVar()
    u_gateway = tk.StringVar()
    
    def submit():
        result['project_name'] = u_project.get()
        result['network'] = u_network.get()
        result['subnet'] = u_subnet.get()
        result['subnet_cidr'] = u_subnet_cidr.get()
        result['gateway'] = u_gateway.get()
        window.destroy()

    # Create label and entry for 'Network'
    project_label = tk.Label(window, text='Project Name', font=('calibre', 10, 'bold'))
    project_label.grid(row=0, column=0, padx=10, pady=10)
    project_entry = tk.Entry(window, textvariable=u_project, font=('calibre', 10, 'normal'))
    project_entry.grid(row=0, column=1, padx=10, pady=10)

    # Create label and entry for 'Network'
    network_label = tk.Label(window, text='Network Name', font=('calibre', 10, 'bold'))
    network_label.grid(row=1, column=0, padx=10, pady=10)
    network_entry = tk.Entry(window, textvariable=u_network, font=('calibre', 10, 'normal'))
    network_entry.grid(row=1, column=1, padx=10, pady=10)
    
    # Create label and entry for 'Subnet'
    subnet_label = tk.Label(window, text='Subnet Name', font=('calibre', 10, 'bold'))
    subnet_label.grid(row=2, column=0, padx=10, pady=10)
    subnet_entry = tk.Entry(window, textvariable=u_subnet, font=('calibre', 10, 'normal'))
    subnet_entry.grid(row=2, column=1, padx=10, pady=10)
    
    # Create label and entry for 'Subnet CIDR'
    subnet_cidr_label = tk.Label(window, text='Subnet CIDR', font=('calibre', 10, 'bold'))
    subnet_cidr_label.grid(row=3, column=0, padx=10, pady=10)
    subnet_cidr_entry = tk.Entry(window, textvariable=u_subnet_cidr, font=('calibre', 10, 'normal'))
    subnet_cidr_entry.grid(row=3, column=1, padx=10, pady=10)
    
    # Create label and entry for 'Gateway'
    gateway_label = tk.Label(window, text='Gateway IP', font=('calibre', 10, 'bold'))
    gateway_label.grid(row=4, column=0, padx=10, pady=10)
    gateway_entry = tk.Entry(window, textvariable=u_gateway, font=('calibre', 10, 'normal'))
    gateway_entry.grid(row=4, column=1, padx=10, pady=10)
    
    sub_btn=tk.Button(window,text = 'Submit', command = submit)
    sub_btn.grid(row=5, column=0)
    window.mainloop()
    return result

    




def login_dasboard(dashboard,username, password):
    dashboard.login(userName=username,passWord=password,url=url)


def create_network(dashboard,project_name, network_name,subnet_name,subnet_cidr,subnet_gateway):
    dashboard.select_project(project_name)
    dashboard.goToNetwork()
    dashboard.goToNetworksSection()
    dashboard.createNetwork(network_name,subnet_name,subnet_cidr,subnet_gateway)

def main():
    dashboard = openstackDashboard()
    network_details = gui()

    login_dasboard(dashboard,username,password)
    create_network(dashboard,network_details['project_name'],network_details['network'],network_details['subnet'],network_details['subnet_cidr'],network_details['gateway'])

    time.sleep(20)
    dashboard.quit()


if __name__=='__main__':
    main()