#!/usr/local/bin/python
# -*- coding: utf-8 -*-


#
# RFID Read
#



import os,sys
import time
import json
import time
import rfidiot
from RFIDapi import *
import array
from ola.ClientWrapper import ClientWrapper
import config

barSignal = 0
dmxwrapper = ClientWrapper()
dmxuniverse = 1
readerid = config.settings['readerID']
print readerid

#######################  DMX FUNCTIONS ################
def DmxSent(state):
	global dmxwrapper
  	dmxwrapper.Stop()

def SendDmx(dmxuniverse, dmxdata):
	global dmxwrapper
	dmxclient = dmxwrapper.Client()
	dmxclient.SendDmx(dmxuniverse, dmxdata, DmxSent)
	dmxwrapper.Run()

def RedDMX(time):
	global dmxuniverse
	dmxdata = array.array('B', [7, 0, 0, 0 ,0])
	SendDmx(dmxuniverse, dmxdata)
	time.sleep(1)
	dmxdata = array.array('B', [0, 0, 0, 0 ,0])
	SendDmx(dmxuniverse, dmxdata)
	time.sleep(0.7)
	dmxdata = array.array('B', [7, 0, 0, 0 ,0])
	SendDmx(dmxuniverse, dmxdata)
	time.sleep(0.5)
	dmxdata = array.array('B', [0, 0, 0, 0 ,0])
	SendDmx(dmxuniverse, dmxdata)
	time.sleep(0.3)
	dmxdata = array.array('B', [7, 0, 0, 0 ,0])
	SendDmx(dmxuniverse, dmxdata)
	time.sleep(0.1)
	dmxdata = array.array('B', [7, 0, 0, 128 ,0])
	SendDmx(dmxuniverse, dmxdata)
	time.sleep(0.1)
	dmxdata = array.array('B', [0, 0, 0, 0 ,0])
	SendDmx(dmxuniverse, dmxdata)

def YellowDMX(time):
	global dmxuniverse
	dmxdata = array.array('B', [19, 0, 0, 0 ,0])
	SendDmx(dmxuniverse, dmxdata)
	
def GreenDMX(time):
	global dmxuniverse
	dmxdata = array.array('B', [13, 0, 0, 0 ,0])
	SendDmx(dmxuniverse, dmxdata)

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
	    # print readerid
        data = getVistorActions(card.uid)
        if (data['visitortype'] == "Premium VIP"):
        	# print data
            # INSERT DMX CODE HERE KASPER
            RedDMX(100)
        elif (data['visitortype'] == "Premium"):
        	YellowDMX(100)
        elif (data['visitortype'] == "Basic"):
        	GreenDMX(100)   
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
    return None
       

##setup stuff
# Open the card reader
card = open_reader()
card_info = card.info('cardselect v0.1m')

# Main loop

try:
    while 1:  
        card_id = listen(card, 0.1)
	listen_remove(card, 0.1, card_id)
except KeyboardInterrupt:
	print "keyboard interrupt!"


