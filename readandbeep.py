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

lastID = "0"
ID1 = '048B50B2FD3480'
score1 = 0
ID2 = '1AF97D05'
score2 = 0


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



###GPIO functions
def enable_LED(pin):
	GPIO.output(pin,GPIO.HIGH)

def disable_LED(pin):
	GPIO.output(pin,GPIO.LOW)

def flash_LED(pin,flash,duration):
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


def got_input(channel):
	global lastID
	global score1, score2
	print("gotinput from " + channel)
	if (channel == "GPIO3"):
		print("channel was really GPIO3")
		print lastID
		print ID1
		if (lastID == ID1):
			score1 = score1 + 1
			cprint(figlet_format(str(score1), font='banner'),'green', 'on_red', attrs=['bold'])
		if (lastID == ID2):
			score2 = score2 + 1
			cprint(figlet_format(str(score2), font='banner'),'green', 'on_red', attrs=['bold'])	
		disable_LED("GPIO1")		
	if(channel == "GPIO4"):
		if (lastID == ID1):
			score1 = score1 - 1
			cprint(figlet_format(str(score1), font='banner'),'green', 'on_red', attrs=['bold'])
		if (lastID == ID2):
			score2 = score2 - 1
			cprint(figlet_format(str(score2), font='banner'),'green', 'on_red', attrs=['bold'])
		disable_LED("GPIO2")


### REMOTE_FUNCTIONS
def checkID(ID):
	global lastID
	if (ID == ID1):
		cprint(figlet_format('datakamp', font='banner'),'yellow', 'on_red', attrs=['bold'])
		lastID = ID1
		enable_LED("GPIO1")




	if (ID == ID2):
		cprint(figlet_format('cirq!', font='banner3'),'red', 'on_yellow', attrs=['bold'])
		lastID = ID2
		enable_LED("GPIO2")

	print(lastID)





##setup stuff
# Open the card reader
card = open_reader()
card_info = card.info('cardselect v0.1m')
#setup GPIOs
###clean
GPIO.cleanup()
GPIO.remove_event_detect("GPIO3")
###setup
GPIO.setup("GPIO1",GPIO.OUT)
GPIO.setup("GPIO2",GPIO.OUT)
GPIO.setup("GPIO4",GPIO.IN)
GPIO.setup("GPIO3",GPIO.IN)
#add callback for GPIO3
GPIO.add_event_detect("GPIO3", GPIO.FALLING, got_input)
GPIO.add_event_detect("GPIO4", GPIO.FALLING, got_input)


# Main loop
while 1:
	card_id = listen(card, 0.1)
	listen_remove(card, 0.1, card_id)

