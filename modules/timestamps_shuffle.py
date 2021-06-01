#!/usr/bin/python3
#Timestamps Shuffler
#DIRS,yes,Add multiple directories separating them with semicolon (example: /bin;/home;/etc)
#END

import os
import time
import subprocess
import random

def randomize_file_timestamps(filename, start_time):
    btime = get_files_btime(filename)
    mtime = random.randint(btime*1000000000, start_time*1000000000)
    atime = random.randint(btime*1000000000, start_time*1000000000)
    ctime =  random.randint(btime, start_time)
    set_fake_time(ctime)
    time.sleep(random.random())
    os.utime(filename, ns=(atime, mtime))

def set_fake_time(global_time):
    os.system("date +%s -s @" + str(global_time) + " > /dev/null")

def get_files_btime(filename):
    inode = subprocess.check_output("stat -c %i " + filename, shell = True)
    inode = inode.decode('utf-8').strip()
    fs = subprocess.check_output("df %s --output=source | tail -1 " % (filename), shell = True)
    fs = fs.decode('utf-8').strip()
    if '/' not in fs:
         fs = '/' + fs
    fs_type = subprocess.check_output("PATH='${PATH}:/sbin' /sbin/fsck -N %s" % (fs), shell = True)
    fs_type = fs_type.decode('utf-8').strip()
    if 'ext4' in fs_type:
        btime = subprocess.check_output("/sbin/debugfs -R 'stat <%s>' %s | grep crtime | awk 'BEGIN{FS=\"--\"} {print $2}'" % (inode, fs), shell = True)
        btime = btime.decode('utf-8')
        btime = subprocess.check_output("date -d'"+ btime +"' +%s", shell = True)
        return int(btime)
    else:
        #return 0
        return random.randint(0, int(time.time())) # return pseudrandom value from the past
    
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
