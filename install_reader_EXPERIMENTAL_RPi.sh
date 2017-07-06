#WARNING COMPLETELY UNTESTED - this may ruin your system YMMV
#this will probably fail the first time it's run on a fresh system, plz adapt script immediately in this file
#purpose of this script is to install the software for datakamp and the dependencies in an automated way
#for the mobile readers we start with standard pocketCHIP firmware (4.4)
#this script should be run with SUDO

echo "export LC_ALL=en_US.UTF-8" >> ~/.bashrc
echo "export LANG=en_US.UTF-8" >> ~/.bashrc
echo "python datakamp/MobileReader_RPi.py &" >> ~/.bashrc

# https://choffee.co.uk/posts/2015/01/nfc_reader_acr122_linux/
# errors while claiming RFID reader solution: CHECK!!
#echo 'blacklist pn533' > /etc/modprobe.d/rfid-blacklist.conf
#echo 'blacklist nfc' > /etc/modprobe.d/rfid-blacklist.conf
#modprobe -r pn533 nfc
# 

apt-get install swig -y
apt-get install libpcsclite-dev -y
apt-get install libusb-dev -y
apt-get install pcscd -y
apt-get install python-dev -y
apt-get install python-gobject -y
apt-get install libjpeg-dev -y
apt-get install zlib1g-dev -y
apt-get install python-pip build-essential -y


# Install libNFC? CHECK!!
#cd ~
#wget http://dl.bintray.com/nfc-tools/sources/libnfc-1.7.1.tar.bz2
#tar -xf libnfc-1.7.1.tar.bz2  
#cd libnfc-1.7.1
#./configure --prefix=/usr --sysconfdir=/etc
#make
#sudo make install 
#
#apt-get install libjpeg-dev 
#more dependencies necessary? CHECK!!
#apt-get install libtiff5-dev libjpeg-dev zlib1g-dev libfreetype6-dev liblcms2-dev libwebp-dev tcl8.6-dev tk8.6-dev python-tk

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
pip install pycrypto
pip install pyscard
pip install gi
pip install playsound

#automated start of script TEST!!
#echo "@python2.7 ~/Documents/datakamp/MobileReader_RPi.py &" >> /home/pi/.config/lxsession/LXDE-pi/autostart
cp libccid_Info.plist /etc/libccid_Info.plist
cd RFIDIOt-master
python ./setup.py install
