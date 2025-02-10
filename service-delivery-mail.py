from datetime import date;

client_name = input("Enter Client name: ")
vcpu = input("vCPU: ")
ram = input("ram: ")
storage = input("Storage: ")
storage_type = input("storage_type: ")
os = input("Os:")
ip = input("IP:")
vm_userName = input("VM UserName: ")
vm_password = input("VM password: ")
bcp_email = input("BCP EMAIL: ")
bcp_password = input("BCP Password: ")
today = date.today().strftime("%d/%m/%y")




mail =  f"""

Service Delivery || {client_name} || {today}
###########################################################################

Dear Sir,

Greetings from Brilliant!
As per request, we have provisioned the VM. Please find the information below:


VM Package Details:
Cores: {vcpu} vCPU
RAM: {ram} GB
Storage: {storage}GB {storage_type}
Operating System: {os}

VM Credentials:
VM Public IP: {ip}
Username: {vm_userName}
Password: {vm_password}

Kindly change the password after the first login.
We have attached the security group "{client_name}-SG" to the VM. ICMP and SSH ports have been allowed in the security group. You can configure additional ports as per your requirements from the BCP portal: https://bcp.brilliant.com.bd/

BCP Portal Credentials:
URL: https://bcp.brilliant.com.bd/
Username: {bcp_email}
Password: {bcp_password}

For more details about Brilliant Cloud, please explore https://cloud-docs.brilliant.com.bd/
"""


print(mail)
with open (client_name+".txt","a+") as file:
    file.write(mail)