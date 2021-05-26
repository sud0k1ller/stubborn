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

## Overview and usage
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
**IMPORTANT!** This version was made just for fun and was not tested on all distros, is not developed any more and has many bugs a.k.a unexpected features. 

Run './stubborn_gui.py' and, if you are lucky you will see this:
![stubborn_gui_main](https://user-images.githubusercontent.com/54325660/119637523-078a6380-be16-11eb-8fbe-4f5ba93583f4.png)
Main window contains two interactive parts 'Interpreter' part and 'Context Tips' part.

In order to list modules use 'list' command in interpreter part:
![stubborn_gui_list](https://user-images.githubusercontent.com/54325660/119639502-f5a9c000-be17-11eb-93ae-393434a94a80.png)

Module is choosen by number with 'use' command:
![stubborn_gui_use](https://user-images.githubusercontent.com/54325660/119639476-f0e50c00-be17-11eb-9509-2f1fd4692b7e.png)

If module is choosen 'info' or 'options' commands can be used to get additional information:
![stubborn_gui_info](https://user-images.githubusercontent.com/54325660/119639595-0c501700-be18-11eb-9cfd-8cfc4f8d7aa1.png)
![stubborn_gui_options](https://user-images.githubusercontent.com/54325660/119639604-0f4b0780-be18-11eb-93ec-436881901568.png)

To set options 'set' command is used (syntax: "set OPT_NAME OPT_VALUE"):
![stubborn_gui_set](https://user-images.githubusercontent.com/54325660/119639734-2db10300-be18-11eb-854e-bfe5aa13db65.png)

If any option is set, its value is shown in 'options' screen:
![stubborn_gui_options_set](https://user-images.githubusercontent.com/54325660/119639784-3acdf200-be18-11eb-9c6a-890d298522a5.png)

After choosing module and setting choosen options values 'execute' is used to launch module:
![stubborn_gui_exe](https://user-images.githubusercontent.com/54325660/119640401-dcedda00-be18-11eb-9508-316e7af79253.png)

More help can be obtained with 'help' command:
![stubborn_gui_help](https://user-images.githubusercontent.com/54325660/119639950-618c2880-be18-11eb-821e-cb84195c31e1.png)

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
