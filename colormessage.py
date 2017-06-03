##via http://stackoverflow.com/questions/9632995/ddg#9638532

import sys

from colorama import init
init(strip=not sys.stdout.isatty()) # strip colors if stdout is redirected
from termcolor import cprint 
from pyfiglet import figlet_format

cprint(figlet_format('missile!', font='starwars'),
       'yellow', 'on_red', attrs=['bold'])
