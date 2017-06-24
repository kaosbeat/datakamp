#!/usr/bin/env python
# -*- coding: utf-8 -*-

from asciimatics.screen import Screen
from asciimatics.renderers import FigletText
from asciimatics.effects import Cycle
from asciimatics.widgets import Frame, ListBox, Layout, Divider, Text, Button, TextBox, Widget

frame = Frame(screen, 80, 20, has_border=False)
layout = Layout([1, 1, 1, 1])
frame.add_layout(layout)


def demo(screen):
	renderer = FigletText("ASCIIMATICS", font='big')
	screen.paint(renderer, 10 , 10)
	screen.refresh()

Screen.wrapper(demo)