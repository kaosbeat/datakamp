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
import RPi.GPIO as GPIO
# import CHIP_IO.GPIO as GPIO
# from colorama import init
# init(strip=not sys.stdout.isatty()) # strip colors if stdout is redirected
# from termcolor import cprint 
# from pyfiglet import figlet_format
from RFIDapi import *
# from screensavers import *
from pygame import mixer
from random import randint


import config_RPi as config

# readerprofile = [0,3]  #action items are only the ones listed in the readerprofile
# state = 0 
# screensaverstate = 0
barSignal = 0

readerid = config.settings['readerID']
################################################################################    
def premiumVipHell(data):
    while barSignal:
        print ("premiumVipHell "+str(barSignal))
        playAudio(str(data['visitortype']), readerid)
        GPIO.output(4,1)
#   time.sleep(4)
################################################################################  
def stopHell(channel):
    print "button pressed!"
    GPIO.output(4,0)    
    global barSignal
    barSignal =0
    


#GPIO Config RPi#
GPIO.setmode(GPIO.BCM)
GPIO.setup(21, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) #input for button, connected to 3.3V so pull down resistor
GPIO.setup(4, GPIO.OUT) #output for relay
GPIO.add_event_detect(21, GPIO.FALLING, callback=stopHell, bouncetime=300)
mixer.init()
mixer.pre_init(44100, 16, 2, 4096) #frequency, size, channels, buffersize
# mixer.Sound.set_volume(1)
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

def playConfirmation():
    if not mixer.music.get_busy():
        dir = os.path.dirname(__file__)
        filename = os.path.join(dir, 'soundboard/Mobile/vip.mp3')
        mixer.music.load(filename)
        mixer.music.play()

def listen(card, interval):
    """ Listens for a card to be placed on the reader """
    while 1:
#       print("now is the time to exit the program by CTRL-C")
        if card.select():
            print readerid
            playConfirmation()
#           if "Ingang" in readerid:
            if readerid=="Ingang1" or readerid=="Ingang2":
                post = logAction(readerid, card.uid, "A00")
                if post:
                    data = getVistorActions(card.uid)
                    buzzer(str(data['visitortype']))
                    break
                break
            # TBD    
            if readerid=="Premium1" or readerid=="Premium2" or readerid=="Premium3":
            #tbd
                break
            #KASSA geluid (en licht?) afspelen bij succes via POST
            if readerid=="Kassa1" or readerid=="Kassa2":
                post = logAction(readerid, card.uid,"ADK")
            # screensaverstate = 0
                if post:
                    data = getVistorActions(card.uid)
                    buzzer(str(data['visitortype']))
                    break
                break
            #BAR geluid en licht tot GPIO input gegeven via POST
            if readerid=="Bar1" or readerid=="Bar2":
                print "in Bar"
                data = getVistorActions(card.uid)
                print(str(data['visitortype']))
                if(str(data['visitortype'])=="Premium VIP"):
                    print "premiumVipHell"
                    global barSignal
                    barSignal=1 
                    premiumVipHell(data)    
                    break
                else:
                    playAudio(str(data['visitortype']), readerid)
                    break

                break

            if  readerid=="Stempaal1" :
                post = logAction (readerid, card.uid, "AA")
                if post:
                    data = getVistorActions(card.uid)
                    buzzer(str(data['visitortype']))
                    break
                break
            if  readerid=="Stempaal2" :
                post = logAction (readerid, card.uid, "AB")
                if post:
                    data = getVistorActions(card.uid)
                    buzzer(str(data['visitortype']))
                    break
                break
            if  readerid=="Stempaal3" :
                post = logAction (readerid, card.uid, "AC")
                if post:
                    data = getVistorActions(card.uid)
                    buzzer(str(data['visitortype']))
                    break
                break
#           if (readerid=="Playfield"):
#                 ##############################################################
#                   post = logAction(readerid, card.uid, "unique ID")
#                 ##############################################################
#                   if post:
#                           data = getVistorActions(card.uid)
#                           playAudio(str(data['visitortype']), readerid)
#                           break
#               break
            if (readerid=="WCuit"):
            #Gili is WC uitgang vanaf !
                post = logAction(readerid, card.uid, "AWX")
                if post:
                    data = getVistorActions(card.uid)
                    playAudio(str(data['visitortype']), readerid)
                    break
                break
            
            if (readerid=="WC"):
                post = logAction(readerid, card.uid, "AWC")
                if post:
                    data = getVistorActions(card.uid)
                    playAudioWC(str(data['visitortype']), readerid)
                    break
                break
            if (readerid=="Lichtpaal"):
                data = getVistorActions(card.uid)
                # INSERT DMX CODE HERE KASPER
                break
            if (readerid=="Uitgang"):
                post = logAction(readerid, card.uid, "A99")
                if post:
                    data = getVistorActions(card.uid)
                    buzzer(str(data['visitortype']))
                    break
                break

        #print 'Waiting: Card Placement'
        time.sleep(interval)
        #return card.uid

def listen_remove(card, interval, card_id):
    """ Listens for a card to be placed on the reader """
    while 1:
        # screensaverstate = 1
        if not card.select():
            break
        #print "Waiting: Card Removal"
        # time.sleep(interval)
        
# Make a folder structure with 
def playAudioWC(userType, location):
    print "play WC"
    for x in xrange(1,5): 
        print ("checking if sound busy try: " + str(x)  )
        if not mixer.music.get_busy():
            dir = os.path.dirname(__file__)
            print location
            if "Basic" in userType: 
                filename = os.path.join(dir, 'soundboard/WC/basic/',str(randint(1,6) )+'.mp3')       
            else: 
                if "Premium VIP" in userType :
                            filename = os.path.join(dir, 'soundboard/WC/premium_vip/1.mp3')
                else: 
                            filename = os.path.join(dir, 'soundboard/WC/vip/',str(randint(1,2))+'.mp3')
            print filename
            mixer.music.load(filename)
            mixer.music.play()
            #time.sleep(2)
            #mixer.stop
            break
        time.sleep(0.3)
    return None

def playAudio(userType, location):
    print "playaudio" +userType+" "+location
    for x in xrange(1,5): 
        print ("checking if sound busy try: " + str(x)  )
        if not mixer.music.get_busy():
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
            break
        time.sleep(0.3)
    return None

def buzzer(userType):
    for x in xrange(1,5): 
        print ("checking if sound busy try: " + str(x)  )
            
        if not mixer.music.get_busy():
            dir = os.path.dirname(__file__)
            if "Basic" in userType: 
                filename = os.path.join(dir, 'soundboard/buzzer/basic.mp3')       
            else: 
                if "Premium VIP" in userType :
                            filename = os.path.join(dir, 'soundboard/buzzer/premium_vip.mp3')
                else: 
                            filename = os.path.join(dir, 'soundboard/buzzer/vip.mp3')
            mixer.music.load(filename)
            mixer.music.play()
            break
        time.sleep(0.3)
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
    GPIO.cleanup()
# except:
#   print "exception!"
#         GPIO.cleanup()
       


#Read RFID

#send ID to server


#print stuff

#print when ready for new scan

