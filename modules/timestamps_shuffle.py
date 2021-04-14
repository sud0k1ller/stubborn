#!/usr/bin/python3
#Timestamps Shuffler
#Directories,yes,Add multiple directories separating them with semicolon (example: /bin;/home;/etc)
#END

import os

def touch_every_file_in_directory(directory):
    for filename in os.listdir(directory):
        os.system('touch -d SATURDAY ' + directory + "/" + filename)

def shuffle(directories):
    directories_list = directories.split(';')
    for directory in directories_list:
        touch_every_file_in_directory(directory)

def main(arguments): #arguments is an array
	shuffle(arguments[0])

arguments = ["/tmp/test1;/tmp/test2"]
main(arguments)
