#datakamp
test


To stop your wifi from go to sleep after idle for awhile, you need to disable its power management.
Edit file /etc/network/interfaces
Assume you Pi connect to network through wlan0. Add new line with wireless-power off right BELOW the line iface wlan0 inet manual
Save and reboot your Pi
run iwconfig now you should see Power Management:off


If you get error 'cannot find module RFIDIot' ==> go to folder RFIDIOT-Master and run:
sudo python ./setup.py install


If you get error failed to transmit with protocol T1:
rerun the install script