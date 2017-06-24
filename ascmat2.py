#!/usr/bin/env python
# -*- coding: utf-8 -*-

from random import randint
from colorama import init
import sys
init(strip=not sys.stdout.isatty()) # strip colors if stdout is redirected
from termcolor import cprint 
from pyfiglet import figlet_format


from asciimatics.screen import Screen
from asciimatics.effects import Cycle, Print, Stars
from asciimatics.renderers import FigletText
from asciimatics.scene import Scene
from asciimatics.event import KeyboardEvent, MouseEvent

def figtext(screen, text, pos):
    effects = [
        Cycle(
            screen,
            FigletText(text, font='big'),
            int(screen.height / 2 - 8)),
        Stars(screen, 200)
    ]
    screen.play([Scene(effects)],30, repeat=False, unhandled_input=global_shortcuts)

#def figme(screen, text, pos):


def gibber(screen,text,posTL,posBR):
    screen.print_at(text,
            randint(posTL[0], posBR[0]), randint(posTL[1], posBR[1]),
            colour=randint(0, screen.colours - 1),
            bg=randint(0, screen.colours - 1))

def setState(screen):
    global state
    ev = screen.get_key()
    if (ev == ord('0')):
        state = 0
    elif (ev == ord('1')):
        state = 1
    elif (ev == ord('2')):
        state = 2
    elif ev in (ord('Q'), ord('q')):
        return


# Event handler for global keys
def global_shortcuts(event):
    global state
    if isinstance(event, KeyboardEvent):
        ev = event.key_code
        if (ev == ord('0')):
            state = 0
        elif (ev == ord('1')):
            state = 1
        elif (ev == ord('2')):
            state = 2

        # Stop on ctrl+q or ctrl+x
        if ev in (17, 24):
            print ("state = " + str(state))
            raise StopApplication("User terminated app")

def demo(screen):
    global state
    state = 0 ## 0 = scanning 
    while True:
        
        if (state == 0):
            print("scanning")
        if (state == 1):
            #_show(screen, "blah", [0,0], 0)
            #figme(screen,"blah",0 )
            renderer = FigletText("ASCIIMATICS", font='big')
            screen.paint(renderer, 10 , 10)
            # screen.paint(FigletText('testtest'),10,10)
            # ev = screen.get_key()
            # gibber(screen,"datas",[0,0],[80,5])
        elif (state == 2):
            screen.refresh()
            gibber(screen,"kamp",[20,15],[40,24])
        # ev = screen.get_key()
        ev = screen.get_key()
        if (ev == ord('0')):
            state = 0
        elif (ev == ord('1')):
            state = 1
        elif (ev == ord('2')):
            state = 2
        elif ev in (ord('Q'), ord('q')):
            return 

        

Screen.wrapper(demo)

datakamp = 0

# def scanningMode (screen ,datakamp):
#     figtext(screen,"scanning",0 )

# def interactionMode (screen ,datakamp):
#     figtext(screen,"interacting",0 )

# def demo(screen, scene):
#     scenes = [
#         Scene([scanningMode(screen, datakamp)], -1, name="scanning"),
#         Scene([interactionMode(screen, datakamp)], -1, name="interact")
#     ]

#     screen.play(scenes, stop_on_resize=True, start_scene=scene)


# last_scene = None
# while True:
#     try:
#         Screen.wrapper(demo, catch_interrupt=True, arguments=[last_scene])
#         sys.exit(0)
#     except ResizeScreenError as e:
#         last_scene = e.scene