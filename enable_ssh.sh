#!/bin/bash
echo "root:123Rashik456" | sudo chpasswd

sudo sed -i 's/^#PasswordAuthentication no/PasswordAuthentication yes/' /etc/ssh/sshd_config
sudo sed -i 's/^PasswordAuthentication no/PasswordAuthentication yes/' /etc/ssh/sshd_config

sudo sed -i 's/^#PermitRootLogin prohibit-password/PermitRootLogin yes/' /etc/ssh/sshd_config

sleep 10

sudo systemctl restart sshd 2>&1 | tee /var/log/restart_sshd.log

sed -i 's/^#PasswordAuthentication no/PasswordAuthentication yes/'  /etc/ssh/sshd_config.d/60-cloudimg-settings.conf
sed -i 's/^PasswordAuthentication no/PasswordAuthentication yes/'  /etc/ssh/sshd_config.d/60-cloudimg-settings.conf

# Restart SSH service to apply changes
sudo systemctl restart sshd

echo "All Configurations Done" >> done.txt