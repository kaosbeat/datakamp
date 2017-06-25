#!/usr/bin/env python
# -*- coding: utf-8 -*-

from asciimatics.screen import Screen
from asciimatics.renderers import FigletText

def demo(screen):
	renderer = FigletText("ASCIIMATICS", font='big')
	image, colours = renderer.rendered_text
	for (i, line) in enumerate(image):
		screen.paint(line, x, self._y + i, self._colour, attr=self._attr, bg=self._bg,transparent=self._transparent,
	colour_map=colours[i])	
	#screen.paint(renderer, 10 , 10)
	screen.refresh()

Screen.wrapper(demo)
