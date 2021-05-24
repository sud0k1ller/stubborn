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
ToDo

## Requirements
The main goal is to keep requirements as low as it is possible, so this list will be hopefuly shortened and stripped to the bone.

**Python version:**
* python3
* git
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

Other modules can still work in unexpected way on distros other than Kali Linux. 

## TODO
[ In progress ] Multidistro testing

[ ] Windows version

[ ] Bash version

[X] No GUI version
