#!/usr/bin/python3
#SUID file
#PATH,yes,Set path to file
#END
import os

def main(arguments):
        os.system('chmod +s ' + arguments[0])
