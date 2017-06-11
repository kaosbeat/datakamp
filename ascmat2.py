from random import randint
from asciimatics.screen import Screen


def demo(screen):
    state = 0
    while True:
        if (state == 0):
            screen.print_at('data',
                        randint(0, screen.width), randint(19, screen.height),
                        colour=randint(0, screen.colours - 1),
                        bg=randint(0, screen.colours - 1))
        elif (state == 1):
             screen.print_at('kamp',
                        randint(0, screen.width), randint(0, 18),
                        colour=randint(0, screen.colours - 1),
                        bg=randint(0, screen.colours - 1))
        ev = screen.get_key()
        if (ev == ord('0')):
            state = 0
        elif (ev == ord('1')):
            state = 1
        elif (ev == ord('2')):
            state = 2
        elif ev in (ord('Q'), ord('q')):
            return
        screen.refresh()

Screen.wrapper(demo)