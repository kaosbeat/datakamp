#!/usr/local/bin/python
# -*- coding: utf-8 -*-


#
# RFID Read
#

import os,sys
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

def confirmationDMX():
    global dmxuniverse
    print ("trying to confirm!")
    dmxdata = array.array('B', [61, 0, 0, 0 ,0])
    SendDmx(dmxuniverse, dmxdata)
    time.sleep(1)
    dmxdata = array.array('B', [0, 0, 0, 0 ,0])
    SendDmx(dmxuniverse, dmxdata)


def RedDMX():
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

def YellowDMX():
    global dmxuniverse
    dmxdata = array.array('B', [19, 0, 0, 0 ,0])
    SendDmx(dmxuniverse, dmxdata)
    
def GreenDMX():
    global dmxuniverse
    dmxdata = array.array('B', [13, 0, 0, 0 ,0])
    SendDmx(dmxuniverse, dmxdata)

def p20DMX(vtype):
    global dmxuniverse
    dmxdata = array.array('B', [7, 0, 0, 0 ,0])
    SendDmx(dmxuniverse, dmxdata)
    time.sleep(1)
    dmxdata = array.array('B', [0, 0, 0, 0 ,0])
    SendDmx(dmxuniverse, dmxdata)



def p40DMX(vtype):
    global dmxuniverse
    dmxdata = array.array('B', [32, 0, 0, 0 ,0])
    SendDmx(dmxuniverse, dmxdata)
    time.sleep(1)
    dmxdata = array.array('B', [0, 0, 0, 0 ,0])
    SendDmx(dmxuniverse, dmxdata)   
def p60DMX(vtype):
    global dmxuniverse
    dmxdata = array.array('B', [26, 0, 0, 0 ,0])
    SendDmx(dmxuniverse, dmxdata)
    time.sleep(1)
    dmxdata = array.array('B', [0, 0, 0, 0 ,0])
    SendDmx(dmxuniverse, dmxdata)   
def p80DMX(vtype):
    global dmxuniverse
    dmxdata = array.array('B', [14, 0, 0, 0 ,0])
    SendDmx(dmxuniverse, dmxdata)
    time.sleep(1)
    dmxdata = array.array('B', [0, 0, 0, 0 ,0])
    SendDmx(dmxuniverse, dmxdata)
def p100DMX(vtype):
    global dmxuniverse
    dmxdata = array.array('B', [200, 0, 0, 0 ,0])
    SendDmx(dmxuniverse, dmxdata)
    time.sleep(3)
    dmxdata = array.array('B', [0, 0, 0, 0 ,0])
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
            confirmationDMX()
            # print readerid
            data = getVistorActions(card.uid)
            print data
            if (data['percentile'] <= 20):
                # INSERT DMX CODE HERE KASPER
                p20DMX(data['visitortype'])
                break
            elif (data['percentile'] <= 40):
                p40DMX(data['visitortype'])
                break
                
            elif (data['percentile'] <= 60):
                p60DMX(data['visitortype'])
                break
            elif (data['percentile'] <= 80):
                p60DMX(data['visitortype'])
                break
            else:
                p100DMX(data['visitortype'])
                break

  

def listen_remove(card, interval, card_id):
    """ Listens for a card to be placed on the reader """
    # Screen.wrapper(datascreen)
    while 1:
        screensaverstate = 1
        if not card.select():
            # data = json.dumps({"card_info":
            #   [{"card_id": card_id}, {"timedate": get_time()}, {"action": "Removed"}]})
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


