#datakamp
test
## todo
1. make sure no tools go to sleep
3. every device should have WiFi connection, check as soon as possible what credentials are
4. alter each device its config file (especially RPis) so that we can play sounds based on location from one big folder



To stop your wifi from go to sleep after idle for awhile, you need to disable its power management.
Edit file /etc/network/interfaces
Assume you Pi connect to network through wlan0. Add new line with wireless-power off right BELOW the line iface wlan0 inet manual
Save and reboot your Pi
run iwconfig now you should see Power Management:off


If you get error 'cannot find module RFIDIot' ==> go to folder RFIDIOT-Master and run:
sudo python ./setup.py install


If you get error failed to transmit with protocol T1:
rerun the install script in datakamp folder


IP MGMT:
WC      192.168.x.x




