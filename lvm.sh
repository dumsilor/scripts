# Variables
DISK="/dev/vda"  # Replace with your actual disk (e.g., /dev/sdb)
PART_NUM=4       # The partition number (1 if it's the first partition on the disk)

sudo fdisk $DISK <<EOF
n
$PART_NUM


t
$PART_NUM
lvm
w
EOF

sudo partprobe $DISK

sudo vgextend ubuntu-vg /dev/vda4

lvextend -rv -l +100%FREE /dev/ubuntu-vg/ubuntu-lv

# Optional: Create a volume group and logical volume
# VG_NAME="vg1"
# LV_NAME="lv1"
# sudo vgcreate $VG_NAME ${DISK}${PART_NUM}
# sudo lvcreate -l 100%FREE -n $LV_NAME $VG_NAME

echo "Partition ${DISK}${PART_NUM} created and changed to LVM type."