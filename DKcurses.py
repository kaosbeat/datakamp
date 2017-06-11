import sys
import termcolor
import curses
from colorama import init
init(strip=not sys.stdout.isatty()) # strip colors if stdout is redirected
from termcolor import cprint 
from pyfiglet import figlet_format


def main(stdscr):
    while 1:
        c = stdscr.getch()
        if c == ord('p'):
            stdscr.addstr("Pretty text", curses.color_pair(1))
            stdscr.refresh()
        elif c == ord('o'):
            cprint(figlet_format('test 123', font='banner'),'green', 'on_red', attrs=['bold'])
        elif c == ord('q'):
            break  # Exit the while()
        elif c == curses.KEY_HOME:
            x = y = 0



if __name__=='__main__':
    try:
        stdscr=curses.initscr()
        curses.noecho() 
        curses.cbreak()  
        curses.start_color()
        curses.init_pair(1, curses.COLOR_RED, curses.COLOR_WHITE)
        stdscr.addstr(0,0, "RED ALERT!", curses.color_pair(1))
        stdscr.keypad(1)
        main(stdscr)            # Enter the main loop
    finally:
        stdscr.erase()
        stdscr.refresh()
    stdscr.keypad(0)
    curses.echo() ; curses.nocbreak()
    curses.endwin()         # Terminate curses


if __name__=='__main__':
    curses.wrapper(main)


