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
from RFIDapi import *
from screensavers import *
from pygame import mixer

import config

readerprofile = [0,3]  #action items are only the ones listed in the readerprofile
state = 0 
screensaverstate = 0
barSignal = 1

readerid = config.settings['readerID']
################################################################################    
def premiumVipHell(data):
    while barSignal:
        playAudio(str(data['visitortype']), readerid)
        GPIO.output(4,1)
################################################################################  
def stopHell(channel):
    print "button pressed!"
    barSignal=0
    GPIO.output(4,0)

#GPIO Config RPi#
GPIO.setmode(GPIO.BCM)
GPIO.setup(21, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) #input for button, connected to 3.3V so pull down resistor
GPIO.setup(4, GPIO.OUT) #output for relay
GPIO.add_event_detect(21, GPIO.FALLING, callback=stopHell, bouncetime=300)
mixer.init()
mixer.pre_init(44100, 16, 2, 4096) #frequency, size, channels, buffersize
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
		    if (readerid=="Ingang"):
			#post = logAction(readerid, card.uid, "mobilescan")
			post = logIngang(readerid, card.uid, "mobilescan")
			screensaverstate = 0
			if post:
			    data = getVistorActions(card.uid)
			    #print data
			    #print ("aantal punten: " + str(data['credits']))
			    #print ("huidige status: ")
			    #cprint(figlet_format(data['visitortype'], font='banner'),'yellow', 'on_red', attrs=['bold'])
			    # print ("naam: " + str(data['name']) )
			    playAudio(str(data['visitortype']), readerid)
			    break
			break
		    # TBD    
		    if (readerid=="Premium"):
			#tbd
			break
		    #KASSA geluid (en licht?) afspelen bij succes via POST
		    if (readerid=="Kassa"):
			post = logIngang(readerid, card.uid, "ADK")
			screensaverstate = 0
			if post:
			    playAudio(str(data['visitortype']), readerid)
			    break
			break
		    #BAR geluid en licht tot GPIO input gegeven via POST
		    if (readerid=="Bar"):
			#post = logAction(readerid, card.uid, "mobilescan")
			data = logBar(readerid, card.uid, "Bar")
	#                print data
	#                print ("aantal punten: " + str(data['credits']))
	#                print ("huidige status: ")
	#                cprint(figlet_format(data['visitortype'], font='banner'),'yellow', 'on_red', attrs=['bold'])
	#                print ("naam: " + str(data['name']) )
			print(str(data['visitortype']))
#            		if(str(data['visitortype'])=="Premium VIP"):
                    	if(str(data['visitortype'])=="Basic"):

			    ####################
			    print("Premium VIP")
			    barSignal=1
#			    premiumVipHell(data)
			    ####################
			    break
		    break

		    if (readerid=="Stempaal"):
			data = logStem (readerid, card.uid, "AA")
	#                print data
	#                print ("aantal punten: " + str(data['credits']))
	#                print ("huidige status: ")
	#                cprint(figlet_format(data['visitortype'], font='banner'),'yellow', 'on_red', attrs=['bold'])
	#                print ("naam: " + str(data['name']) )
	#                break
			break
		    if (readerid=="Playfield"):
		    ##############################################################
			post = logPlay(readerid, card.uid, "unique ID")
		    ##############################################################
			screensaverstate = 0
			if post:
			    data = getVistorActions(card.uid)
			    #print data
			    #print ("aantal punten: " + str(data['credits']))
			    #print ("huidige status: ")
			    #cprint(figlet_format(data['visitortype'], font='banner'),'yellow', 'on_red', attrs=['bold'])
			    # print ("naam: " + str(data['name']) )
			    playAudio(str(data['visitortype']), readerid)
			    break
			break
		    if (readerid=="Gili"):
			#post = logAction(readerid, card.uid, "mobilescan")
			post = logGili(readerid, card.uid, "Gili")
			screensaverstate = 0
			if post:
			    data = getVistorActions(card.uid)
	#                    print data
	#                    print ("aantal punten: " + str(data['credits']))
	#                    print ("huidige status: ")
	#                    cprint(figlet_format(data['visitortype'], font='banner'),'yellow', 'on_red', attrs=['bold'])
	#                    print ("naam: " + str(data['name']) )
			    playAudio(str(data['visitortype']), readerid)
			    break
			break
		    if (readerid=="WC"):

			break
		    if (readerid=="Lichtpaal"):
			break
		    if (readerid=="Uitgang"):
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
        
#Make a folder structure with 
def playAudio(userType, location):
    print "playaudio"
    if not mixer.music.get_busy():
#         mixer.init()
        print "first play"
        dir = os.path.dirname(__file__)
        print location
        if "Basic" in userType: 
            filename = os.path.join(dir, 'soundboard/',location,'basic.mp3')       
        else: 
		if "Premium VIP" in userType :
            		filename = os.path.join(dir, 'soundboard/',location,'premium_vip.mp3')
		else: 
                	filename = os.path.join(dir, 'soundboard/',location,'vip.mp3')
        print filename
        mixer.music.load(filename)
        mixer.music.play()
#    else:
#	print("audio already playing")
    return None
       

##setup stuff
# Open the card reader
card = open_reader()
card_info = card.info('cardselect v0.1m')




# Main loop
while 1:
	card_id = listen(card, 0.1)
	listen_remove(card, 0.1, card_id)
#    GPIO.cleanup()    


#Read RFID

#send ID to server


#print stuff

#print when ready for new scan

