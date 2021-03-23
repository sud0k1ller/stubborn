#!/usr/bin/python3
#[PrivEsc] Create New User
#username,no,Username for created user
#password,no,Password for created user
#uid,no,UID for created user
#system,no,Create system user (yes/no)
#END

import os

def main(arguments):
    command_string = "adduser "
    if arguments[0] == "":
        command_string += "systemd-pipe "
    if arguments[1] != "":
        pass
        #TODO command_string += ""
    if arguments[2] != "":
        command_string += "--uid=" + str(arguments[2]) + " "
    if arguments[3] == "yes":
        command_string += "--system "

    os.system(command_string)

