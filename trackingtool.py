import sys, getopt
from config import *

from lib.alert.sms import *
from lib.alert.email import email
from lib.alert.alertcenter import alertcenter


from lib.ddos.checkddos import *

from lib.general.time_work import *
from lib.general.time_log import *

from  lib.deface.checkdeface import *
from urlparse import urlparse

from lib.khoitaodoc.khoitao import *



from controller.trackingController import *


        
      
banner="""






 /$$      /$$           /$$    /$$$$$$$$                           /$$       /$$                    
| $$  /$ | $$          | $$   |__  $$__/                          | $$      |__/                    
| $$ /$$$| $$  /$$$$$$ | $$$$$$$ | $$  /$$$$$$  /$$$$$$   /$$$$$$$| $$   /$$ /$$ /$$$$$$$   /$$$$$$ 
| $$/$$ $$ $$ /$$__  $$| $$__  $$| $$ /$$__  $$|____  $$ /$$_____/| $$  /$$/| $$| $$__  $$ /$$__  $$
| $$$$_  $$$$| $$$$$$$$| $$  \ $$| $$| $$  \__/ /$$$$$$$| $$      | $$$$$$/ | $$| $$  \ $$| $$  \ $$
| $$$/ \  $$$| $$_____/| $$  | $$| $$| $$      /$$__  $$| $$      | $$_  $$ | $$| $$  | $$| $$  | $$
| $$/   \  $$|  $$$$$$$| $$$$$$$/| $$| $$     |  $$$$$$$|  $$$$$$$| $$ \  $$| $$| $$  | $$|  $$$$$$$
|__/     \__/ \_______/|_______/ |__/|__/      \_______/ \_______/|__/  \__/|__/|__/  |__/ \____  $$
                                                                                           /$$  \ $$
                                                                                          |  $$$$$$/
                                                                                           \______/       


                                                                      


"""
banner+="[+] TRACKINGTOOL\n[+] Author: truongtn \n[+] Home:https://truongtn.wordpress.com/\n[+] Since:2015\n\n\n\n\n"


                                                             
                                                             


print banner
trackingController()

