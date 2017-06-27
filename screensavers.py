from random import randint
from asciimatics.screen import Screen


def datascreen(screen):
    global screensaverstate
    screensaverstate = 1
    while True:
        screensaverstate = randint(0,150)
        if (screensaverstate == 1):
            screen.close()
            return
        elif (screensaverstate == 0):
            screen.print_at('data',
                        randint(0, screen.width), randint(19, screen.height),
                        colour=randint(0, screen.colours - 1),
                        bg=randint(0, screen.colours - 1))
        else:
             screen.print_at('kamp',
                        randint(0, screen.width), randint(0, 18),
                        colour=randint(0, screen.colours - 1),
                        bg=randint(0, screen.colours - 1))
        ev = screen.get_key()
        if ev in (ord('Q'), ord('q')):
            exit()
        screen.refresh()


