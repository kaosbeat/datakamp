#
# RFID Read
#

import sys
import time
import json
import rfidiot
import CHIP_IO.GPIO as GPIO
from colorama import init
init(strip=not sys.stdout.isatty()) # strip colors if stdout is redirected
from termcolor import cprint 
from pyfiglet import figlet_format

# Card reader Functions
def open_reader():
	""" Attempts to open the card reader """
	try:
		card = rfidiot.card
		return card
	except:
		print "Couldn't open reader!"
		sys.exit()
		return None

def listen(card, interval):
	""" Listens for a card to be placed on the reader """
	
	while 1:	
		if card.select():
			data = json.dumps({"card_info":
				[{"card_id": card.uid}, {"timedate": get_time()}, {"action": "Placed"}]})
			print(data)
			checkID(card.uid)
			break
		#print 'Waiting: Card Placement'
		time.sleep(interval)
	return card.uid

def listen_remove(card, interval, card_id):
	""" Listens for a card to be placed on the reader """
	while 1:
		if not card.select():
			data = json.dumps({"card_info":
				[{"card_id": card_id}, {"timedate": get_time()}, {"action": "Removed"}]})
			print(data)
			break
		#print "Waiting: Card Removal"
		time.sleep(interval)

def get_time():
	""" Returns a string with the time and date """
	return time.strftime("%a, %d %b %Y %H:%M:%S + 0000", time.gmtime())



###LEDpin functions
def enable_LED(pin,flash,duration):
	if flash:
		for x in xrange(1,duration):
			GPIO.output(pin,GPIO.HIGH)
			time.sleep(0.5)
			GPIO.output(pin,GPIO.LOW)
			time.sleep(0.5)
	else:
		GPIO.output(pin,GPIO.HIGH)
		time.sleep(duration)
		GPIO.output(pin,GPIO.LOW)





### REMOTE_FUNCTIONS
def checkID(ID):
	if (ID == '048B50B2FD3480'):
		cprint(figlet_format('datakamp', font='banner'),'yellow', 'on_red', attrs=['bold'])
		enable_LED("GPIO1",True,5)
	if (ID == '1AF97D05'):
		cprint(figlet_format('cirq!', font='banner3'),'red', 'on_white', attrs=['bold'])
		enable_LED("GPIO2",True,5)




##setup stuff
# Open the card reader
card = open_reader()
card_info = card.info('cardselect v0.1m')
#setup GPIOs
GPIO.cleanup()
GPIO.setup("GPIO1",GPIO.OUT)
GPIO.setup("GPIO2",GPIO.OUT)
GPIO.setup("GPIO3",GPIO.OUT)


# Main loop
while 1:
	card_id = listen(card, 0.1)
	listen_remove(card, 0.1, card_id)

