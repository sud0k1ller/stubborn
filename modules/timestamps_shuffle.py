#!/usr/bin/python3
#Timestamps Shuffler
#Directories,yes,Add multiple directories separating them with semicolon (example: /bin;/home;/etc)
#END

import os
import time
import subprocess
import random

def randomize_file_timestamps(filename, start_time):
    btime = get_files_btime(filename)
    mtime = random.randint(btime, start_time)
    atime = random.randint(btime, start_time)
    ctime =  random.randint(btime, start_time)
    set_fake_time(ctime)
    os.system('touch -m -d @' + str(mtime) + ' ' + filename)
    os.system('touch -a -d @' + str(atime) + ' ' + filename)

def set_fake_time(global_time):
    os.system("date +%s -s @" + str(global_time) + " > /dev/null")

def get_files_btime(filename):
    btime = subprocess.check_output("stat " + filename +  "| grep Birth", shell = True)
    btime = btime.decode('utf-8').split()[1] + " " + btime.decode('utf-8').split()[2] 
    btime = subprocess.check_output("date -d '" + btime + "' +%s", shell = True)
    return int(btime.decode('utf-8'))

def touch_every_file_in_directory(directory, start_time):
    for filename in os.listdir(directory):
        randomize_file_timestamps(directory + "/" + filename, start_time)

def shuffle(directories, start_time):
    directories_list = directories.split(';')
    for directory in directories_list:
        touch_every_file_in_directory(directory, start_time)

def main(arguments):
    start_time = int(time.time())
    shuffle(arguments[0], start_time)
    os.system('date +%s -s @' + str(int(start_time)) + ' > /dev/null')

#main(["/tmp/test2"])
