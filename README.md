# stubborn
Stubborn is an orchestrator for a small set of scripts that can be used to obtain persistency on machines (Linux-based at the moment) that were compromised and owned.


## Why?
Normally, here is how the adventure ends:
```
$ whoami
root
```
Post exploitation is sadly underrated, especially at the beginning of cybersecurity learning path - gaining root access is simply more exciting and satisfying.

Creating this tool is my way of gaining some knowledge about Linux systems from administrators perspective, security mechanisms, building software from sources and automating tasks.

## Usage
### stubborn_arg.py - version using argparser library
----
To check available modules, simply use '--list':
![stubborn_1](https://user-images.githubusercontent.com/54325660/119622774-c12e0800-be07-11eb-8524-aff6ac41849f.png)

After choosing module use '--info' to get brief module description and all used parameters:
![stubborn_2](https://user-images.githubusercontent.com/54325660/119622804-c8551600-be07-11eb-8104-32cdc4d37789.png)

To execute module use '--module module_name' with '--set OPT1=OPT_VALUE OPT2=OPT2_VALUE' and '--execute'. Hit ENTER and done!
![stubborn_3](https://user-images.githubusercontent.com/54325660/119622816-cb500680-be07-11eb-82f8-c5d213dacf09.png)

Generic help is available with '--help':
![stubborn_help](https://user-images.githubusercontent.com/54325660/119622980-03574980-be08-11eb-8f7c-756143f0b2d7.png)

### stubborn_gui.py - version using curses library
ToDo

## Requirements
The main goal is to keep requirements as low as it is possible, so this list will be hopefuly shortened and stripped to the bone.

**Python version:**
* python3
* git (just in experimental modules)
* curses (only for stubborn_gui.py)
* gcc, gnulib autotools and many more tools for sources building (just in experimental modules)

## Modules testing
Modules were initially wriiten on Kali Linux but at the moment they are tested on distributions listed below:
- [Debian] Linux debian 4.19.0-16-amd64 #1 SMP Debian 4.19.181-1 (2021-03-19) x86_64 GNU/Linux
- [Fedora] Linux fedora 5.8.15-301.fc33.x86_64 #1 SMP Thu Oct 15 16:58:06 UTC 2020 x86_64 x86_64 x86_64 GNU/Linux
- [CentOS] Linux localhost.localdomain 4.18.0-240.el8.x86_64 #1 SMP Fri Sep 25 19:48:47 UTC 2020 x86_64 x86_64 x86_64 GNU/Linux
- [Ubuntu] Linux ubuntu 5.8.0-53-generic #60~20.04.1-Ubuntu SMP Thu May 6 09:52:46 UTC 2021 x86_64 x86_64 x86_64 GNU/Linux
- [Kali]   Linux kali 5.10.0-kali5-amd64 #1 SMP Debian 5.10.24-1kali1 (2021-03-23) x86_64 GNU/Linux

Modules that are already tested:
- add_user.py
- setcap_suid_file.py
- suid_binary.py
- ssh_auth_keys.py

Other modules can still work in unexpected way on distros other than Kali Linux. 

## TODO
[ In progress ] Multidistro testing

[ ] Windows version

[ ] Bash version
