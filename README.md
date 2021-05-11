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
  * [add_user.py] tested on:
      - [Debian] Linux debian 4.19.0-16-amd64 #1 SMP Debian 4.19.181-1 (2021-03-19) x86_64 GNU/Linux
      - [Fedora] Linux fedora 5.8.15-301.fc33.x86_64 #1 SMP Thu Oct 15 16:58:06 UTC 2020 x86_64 x86_64 x86_64 GNU/Linux
  * [suid_binary.py] tested on:
      - [Debian] Linux debian 4.19.0-16-amd64 #1 SMP Debian 4.19.181-1 (2021-03-19) x86_64 GNU/Linux
      - [Fedora] Linux fedora 5.8.15-301.fc33.x86_64 #1 SMP Thu Oct 15 16:58:06 UTC 2020 x86_64 x86_64 x86_64 GNU/Linux

## TODO
[ ] Multidistro testing

[ ] Windows version

[ ] Bash version

[X] No GUI version
