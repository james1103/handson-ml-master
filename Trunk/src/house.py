'''
Created on 19 Jun. 2018

@author: njwgc
'''
# import libraries
import sys
import ConfigParser
import time
import getpass
import json
import base64
from tkMessageBox import ABORTRETRYIGNORE


# ##
# log 
# ##
def log(pMsg):
    print time.strftime("%Y-%b-%d %H:%M:%S") + ": " + pMsg + "\n"
    sys.stdout.flush()


# ##
# process - process procedure
# ##
def process():

    try:
        print time.strftime("%Y-%b-%d %H:%M:%S") + ": Process start \n\n"
        print "\n\n" + time.strftime("%Y-%b-%d %H:%M:%S") + ": process completed."
 
    except Exception, e:
        if str(e) != "Locking error.":
            log("ERROR: " + str(e))


# ##
# main - main procedure
# ##
def main(*args, **kwargs):
    try:
        print time.strftime("%Y-%b-%d %H:%M:%S") + ": Main start\n\n"
   
        process()
        
        print "\n\n" + time.strftime("%Y-%b-%d %H:%M:%S") + ": Main completed."
        sys.exit()
 
    except Exception, e:
        if str(e) != "Locking error.":
            log("ERROR: " + str(e))
     
        sys.exit()


if __name__ == '__main__':
    main(sys.argv)
