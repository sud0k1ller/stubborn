#!/usr/bin/python3
#Timestamps Shuffler
#Directories,yes,Add multiple directories separating them with semicolon (example: /bin;/home;/etc)
#END

import os
import time
import subprocess
import random


def randomize_file_timestamp(filename):
    btime = get_files_btime(filename)
    print("START: " + str(btime))
    print("RAND: " + str(random.randint(btime, start_time)))
    print("END: " + str(start_time))
        #For ctime, mtime, atime:
    #Randomly select timestamp between now and birth of file
    #set timestamp
    pass


def get_files_btime(filename):
    btime = subprocess.check_output("stat " + filename +  "| grep Birth", shell = True)
    btime = btime.decode('utf-8').split()[1] + " " + btime.decode('utf-8').split()[2] 
    btime = subprocess.check_output("date -d '" + btime + "' +%s", shell = True)
    return int(btime.decode('utf-8'))

def touch_every_file_in_directory(directory):
    for filename in os.listdir(directory):
        randomize_file_timestamp(directory + "/" +filename)

def shuffle(directories):
    directories_list = directories.split(';')
    for directory in directories_list:
        touch_every_file_in_directory(directory)

def main(arguments): #arguments is an array
	shuffle(arguments[0])


start_time = int(time.time())
arguments = ["/tmp/test1;/tmp/test2"]
main(arguments)
os.system('date +%s -s @' + str(int(start_time) - 120))
