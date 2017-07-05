#!/usr/local/bin/python
# -*- coding: utf-8 -*-


#
# RFID Read
#



import os,sys
import time
import json
import rfidiot
import RPi.GPIO as GPIO
from colorama import init
init(strip=not sys.stdout.isatty()) # strip colors if stdout is redirected
from termcolor import cprint 
from pyfiglet import figlet_format
from RFIDapi import logAction,getVistorActions
from screensavers import *
from pygame import mixer

import config

readerprofile = [0,3]  #action items are only the ones listed in the readerprofile
state = 0 
screensaverstate = 0

readerid = config.settings['readerID']

#GPIO Config RPi#
GPIO.setmode(GPIO.BCM)


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
	global screensaverstate
	while 1:
		# Screen.wrapper(datascreen)
		# print("now is the time to exit the program by CTRL-C")
		# time.sleep(2)
		if card.select():
			post = logAction(readerid, card.uid, "mobilescan")
			screensaverstate = 0
			if post:
				data = getVistorActions(card.uid)
				print data
				print ("aantal punten: " + str(data['credits']))
				print ("huidige status: ")
				cprint(figlet_format(data['visitortype'], font='banner'),'yellow', 'on_red', attrs=['bold'])
				# print ("naam: " + str(data['name']) )
                    		playAudio(str(data['visitortype']), readerid)
           		break
        #print 'Waiting: Card Placement'
		time.sleep(interval)
	return card.uid

def listen_remove(card, interval, card_id):
	""" Listens for a card to be placed on the reader """
	# Screen.wrapper(datascreen)
	while 1:
		screensaverstate = 1
		if not card.select():
			# data = json.dumps({"card_info":
			# 	[{"card_id": card_id}, {"timedate": get_time()}, {"action": "Removed"}]})
			# print(data)
			break
		#print "Waiting: Card Removal"
		time.sleep(interval)

def playAudio(userType, location):
    mixer.init()
    dir = os.path.dirname(__file__)
	print location
    if "Basic" in userType: 
    	filename = os.path.join(dir, 'soundboard/',location,'/Flush.mp3')
    else :
        filename = os.path.join(dir, 'soundboard/WC/kakken_kort.mp3')

    mixer.music.load(filename)
    mixer.music.play()
    return None
        
##setup stuff
# Open the card reader
card = open_reader()
card_info = card.info('cardselect v0.1m')




# Main loop
while 1:
	card_id = listen(card, 0.1)
	listen_remove(card, 0.1, card_id)


#Read RFID

#send ID to server


#print stuff

#print when ready for new scan

