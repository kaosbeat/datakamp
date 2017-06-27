#WARNING COMPLETELY UNTESTED - this may ruin your system YMMV
#this will probably fail teh first time it's run on a fresh system, plz adapt script immediately in this file
#purpose of this script is to install the software for datakamp and the dependencies in an automated way
#for the mobile readers we start with standard pocketCHIP firmware (4.4)
#this script should be run with SUDO

echo "export LC_ALL=en_US.UTF-8" >> /home/chip/.bashrc
echo "export LANG=en_US.UTF-8" >> /home/chip/.bashrc

apt-get install swig
apt-get install libpcsclite-dev
apt-get install pcscd
pip install pyscard


echo "installing RFIDIOT"

wget https://github.com/AdamLaurie/RFIDIOt/archive/master.zip
unzip master.zip
cd RFIDIOt-master
python ./setup.py install
cd ..

echo "installing some more dependencies"

apt-get install libjpeg-dev 
pip install asciimatics
pip install requests
pip install colorama
pip install termcolor
pip install pyfiglet
