#!/usr/local/bin/python
# -*- coding: utf-8 -*-


#
# RFID Read
#



import os,sys
import time
import json
import rfidiot
from colorama import init
init(strip=not sys.stdout.isatty()) # strip colors if stdout is redirected
from termcolor import cprint 
from pyfiglet import figlet_format
from RFIDapi import *

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
			break
		print 'Waiting: Card Placement'
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
		print "Waiting: Card Removal"
		# time.sleep(interval)

def get_time():
	""" Returns a string with the time and date """
	return time.strftime("%a, %d %b %Y %H:%M:%S + 0000", time.gmtime())


### REMOTE_FUNCTIONS

##setup stuff
# Open the card reader
card = open_reader()
card_info = card.info('cardselect v0.1m')


# Main loop
while 1:
	card_id = listen(card, 0.1)
	listen_remove(card, 0.1, card_id)

