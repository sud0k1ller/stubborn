#!/usr/bin/python3
#[Access] SSH authorized_keys
#USER,no,Username to whom keys will be added
#KEY_PATH,no,Path to generated SSH key
#END
import os

def generate_ssh_key(): #Generates new ssh key and stores it in /tmp
    ssh_key_file_path="/tmp/"
    return ssh_key_file_path

def find_available_auth_files(): #Looks for authorized_keys in /home subdirectories
    pass

def copy_key_to_auth_file(auth_file_path, ssh_key_file_path):
    pass


def main(arguments):
    if arguments[1] == "" #No custom SSH key given
        arguments[1] = generate_ssh_key()

    if arguments[0] == "": #No username given
        if available_auth_file = find_available_auth_file():
            copy_key_to_auth_file(available_auth_file, arguments[1])
        else:
            pass
    else:
        pass
