#datakamp
test


To stop your wifi from go to sleep after idle for awhile, you need to disable its power management.
Edit file /etc/network/interfaces
Assume you Pi connect to network through wlan0. Add new line with wireless-power off right BELOW the line iface wlan0 inet manual
Save and reboot your Pi
run iwconfig now you should see Power Management:off