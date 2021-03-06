#WARNING COMPLETELY UNTESTED - this may ruin your system YMMV
#this will probably fail teh first time it's run on a fresh system, plz adapt script immediately in this file
#purpose of this script is to install the software for datakamp and the dependencies in an automated way
#for the mobile readers we start with standard pocketCHIP firmware (4.4)
#this script should be run with SUDO

#echo 'export LC_ALL=en_US.UTF-8' >> /home/chip/.bashrc
#echo 'export LANG=en_US.UTF-8' >> /home/chip/.bashrc
#echo 'bash /home/chip/datakamp/startup.sh' >> /home/chip/.bashrc


apt-get install swig -y
apt-get install libpcsclite-dev -y
apt-get install pcscd -y
apt-get install libjpeg-dev -y
apt-get install zlib1g-dev -y
apt-get install python-pip python-dev build-essential -y
apt-get build-dep python-pygame -y
apt-get install openssh-server -y



echo "installing RFIDIOT"

wget https://github.com/AdamLaurie/RFIDIOt/archive/master.zip
unzip master.zip
cd RFIDIOt-master
python ./setup.py install
cd ..

echo "installing some more dependencies"

pip install asciimatics
pip install requests
pip install colorama
pip install termcolor
pip install pyfiglet
pip install pyscard
pip install CHIP-IO
pip install pygame
pip install pycrypto


cp libccid_Info.plist /etc/libccid_Info.plist
#cp rc.local /etc/rc.local
cp .bashrcChip /home/chip/.bashrc
#https://access.redhat.com/documentation/en-US/Red_Hat_Enterprise_Linux/7/html/Networking_Guide/sec-Using_the_NetworkManager_Command_Line_Tool_nmcli.html
nmcli con add con-name datakamp ifname wlan0 type wifi ssid guesst 
#ip4 10.0.3.1/24 gw4 10.0.0.1
nmcli con modify datakamp wifi-sec.key-mgmt wpa-psk
nmcli con modify datakamp wifi-sec.psk VdxLC3B9o6hienL


#make sure default audio output = audio jack, NOT HDMI
amixer cset numid=3 1
#!/usr/bin/env python

cd RFIDIOt-master
chmod +x setup.py
python /home/chip/datakamp/RFIDIOt-master/setup.py install