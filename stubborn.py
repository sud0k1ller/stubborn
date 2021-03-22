#!/bin/python3

import curses
import os

def get_modules_files_list():
    modules_list = os.listdir('./modules')
    for filename in modules_list: 
        if '.info' in filename: 
            modules_list.remove(filename) 
    return modules_list

def get_modules_properties_list(modules_list):
    modules_properties_list = []
    for index in range(0, len(modules_list)):
        #module_properties = [<filename>, <module_name>, <"opt1_name", "req", "desc">, <"opt2_name", "req", "desc">, ... ]
        this_module_properties = []
        this_module_options = []
        option = []
        this_module_properties.append(modules_list[index]) # Add module's filename to the list
        modules_file = open('./modules/' + modules_list[index])
        this_module_properties.append(modules_file.readline()[1:]) #Add module's name to the list
        while option != "END\n":
            option = modules_file.readline()[1:]
            this_module_properties.append(option)
        modules_properties_list.append(this_module_properties[:-1])

    return modules_properties_list

def print_generic_help(prompt_win):
    prompt_win.addstr(4, 3, "Help")
    prompt_win.addstr(6, 3, "Stubborn is simple post-exploitation persistency automation tool.") 
    prompt_win.addstr(7, 3, "It is not and was not meant to be rocket science.")
    prompt_win.addstr(9, 3, "Your path with this script is very simple:")
    prompt_win.addstr(11, 10, "Step 1. Choose module")
    prompt_win.addstr(12, 15 ,"[+] Use 'list' command to get list of all available modules.")
    prompt_win.addstr(13, 15 ,"[+] Use 'use <module_number>' command to select module.")
    prompt_win.addstr(15, 10, "Step 2. Set options")
    prompt_win.addstr(16, 15 ,"[+] Use 'options' to list all module options.")
    prompt_win.addstr(17, 15 ,"[+] Use 'set <option_name> <option_value>' command to set options for selected module.")
    prompt_win.addstr(18, 15, "[+] Use 'info' command to get detailed info about selected module")
    prompt_win.addstr(20, 10, "Step 3. Execute")
    prompt_win.addstr(21, 15 ,"[+] Type 'execute' to perform action")

    prompt_win.refresh()

def print_contextual_help(side_win, context, selected_module_number, modules_properties_list):
    side_win.clear()
    side_win.box()
    side_win.addstr(0, 14, "Context Tips")
    
    if context == "initial":
        side_win.addstr(2, 1, "Welcome to Stubborn!")
        side_win.addstr(4, 1, "Suggested commands:")
        side_win.addstr(5, 4, "> exit")
        side_win.addstr(6, 4, "> list")
        side_win.addstr(7, 4, "> help - for more help")
        side_win.refresh()
    elif context == "generic_help":
        side_win.addstr(2, 1, "You are in Help Text")
        side_win.addstr(4, 1, "Suggested commands:")
        side_win.addstr(5, 4, "> exit")
        side_win.addstr(6, 4, "> list")
        side_win.refresh()
    elif context == "list_modules":
        side_win.addstr(2, 1, "You are in Module Listing")
        side_win.addstr(4, 1, "Suggested commands:")
        side_win.addstr(5, 4, "> exit")
        side_win.addstr(6, 4, "> use <module_number>")
        side_win.addstr(7, 4, "> help - for more help")
        side_win.refresh()
    elif context == "module":
        side_win.addstr(2, 1, "You are in Module Options Setting Mode")
        side_win.addstr(4, 1, "Suggested commands:")
        side_win.addstr(5, 4, "> exit")
        side_win.addstr(6, 4, "> list")
        side_win.addstr(7, 4, "> info")
        side_win.addstr(8, 4, "> options")
        side_win.addstr(9, 4, "> set <option_name> <value>")
        side_win.addstr(10, 4, "> execute")
        side_win.addstr(11, 4, "> help - for more help")
        side_win.refresh()
    elif context == "execute":
        side_win.addstr(2, 1, "You are in Module Execution Mode")
        side_win.addstr(4, 1, "Suggested comamands:")
        side_win.addstr(5, 4, "> exit")
        side_win.addstr(6, 4, "> list")
        side_win.addstr(7, 4, "> help - for more help")
        side_win.refresh()    
    else:
        side_win.clear()
        side_win.box()
        side_win.addstr(0, 14, "Context Tips")
        side_win.addstr(2, 1, "Are you lost?")
        side_win.addstr(4, 1, "Suggested commands:")
        side_win.addstr(5, 4, "> exit - close script")
        side_win.addstr(6, 4, "> help - for more help")
        side_win.refresh()

    if selected_module_number != 0:
        side_win.addstr(15, 4, "Selected module:")
        side_win.addstr(16, 8, modules_properties_list[selected_module_number - 1][1])
        side_win.box()
        side_win.addstr(0, 14, "Context Tips")
        side_win.refresh()

def print_modules_list(prompt_win, modules_properties_list):
    prompt_win.addstr(4, 3, "Modules list:")
    for module, index in zip(modules_properties_list, range(0,len(modules_properties_list))):
        prompt_win.addstr(5+index, 6, str("[" + str(index + 1) + "] " + module[1]))
    prompt_win.refresh()

def init_screen():
    stdscr = curses.initscr()
    stdscr.keypad(True)
    curses.nocbreak()
    curses.echo

    return stdscr

def define_windows():
    # HEADER_WINDOW
    header_win = curses.newwin(10, 105, 1, 3)
    # PROMPT_WINDOW 
    prompt_win = curses.newwin(44, 105, 11, 3)
    # SIDE_WINDOW
    side_win = curses.newwin(54, 40, 1, 109)
    # FOOTER_WINDOW
    footer_win = curses.newwin(1, 146, 55, 3)

    return header_win, prompt_win, side_win, footer_win

def print_footer_and_header(header_win, footer_win):
    header_win.box()
    print_logo(header_win)
    footer_win.box()
    footer_win.addstr(0,1, "sud0k1ller, 2021")
    header_win.refresh()
    footer_win.refresh()

def print_initial_prompt(prompt_win):
    prompt_win.box()
    prompt_win.refresh()

def print_logo(header_win):
    pass

def print_initial_screen(stdscr, header_win, prompt_win, side_win, footer_win, modules_properties_list):
    stdscr.refresh()
    print_footer_and_header(header_win, footer_win)
    print_contextual_help(side_win, "initial", 0, modules_properties_list)
    print_initial_prompt(prompt_win)

def exit_script():
    curses.endwin()
    exit()

def clear_prompt_output(prompt_win):
    prompt_win.move(3,1)
    prompt_win.clrtobot()

def use_command(prompt_win, side_win, selected_module_number, modules_properties_list):
    selected_module_options_values = []
    print_contextual_help(side_win, "module", selected_module_number, modules_properties_list)
    clear_prompt_output(prompt_win)
    for option in modules_properties_list[selected_module_number - 1][2:]:
        if option.split(",")[1] == "yes": #IS REQUIRED?
            selected_module_options_values.append([option.split(",")[0], "", True])
        else: 
            selected_module_options_values.append([option.split(",")[0], "", False])
    return selected_module_options_values

def invalid_command(prompt_win, side_win, selected_module_number, modules_properties_list):
    clear_prompt_output(prompt_win)
    print_contextual_help(side_win, "invalid", selected_module_number, modules_properties_list)
    prompt_win.addstr(4, 3, "Invalid command")
    prompt_win.refresh()

def help_command(side_win, prompt_win, selected_module_number, modules_properties_list):
    print_contextual_help(side_win, "generic_help", selected_module_number, modules_properties_list)
    clear_prompt_output(prompt_win)
    print_generic_help(prompt_win)

def list_command(side_win, prompt_win, selected_module_number, modules_properties_list):
    print_contextual_help(side_win, "list_modules", selected_module_number, modules_properties_list)
    clear_prompt_output(prompt_win)
    print_modules_list(prompt_win, modules_properties_list)


def list_modules_options(prompt_win, option, offset, selected_module_options_values):
    prompt_win.addstr(7, 5, '{:<15}'.format("OPTION") + '{:<10}'.format("REQUIRED") + '{:<50}'.format("DESCRIPTION") + '{:<15}'.format("VALUE"))
    index =  [element[0] for element in selected_module_options_values].index(option.split(",")[0])
    if selected_module_options_values[index][1] != "":
        option_parts = option.split(",")
        prompt_win.addstr(9+offset, 5, '{:<15}'.format(option_parts[0]) + '{:<10}'.format(option_parts[1]) + '{:<50}'.format(option_parts[2][:-1]) + '{:<15}'.format(selected_module_options_values[index][1]))
    else:
        option_parts = option.split(",")
        prompt_win.addstr(9+offset, 5, '{:<15}'.format(option_parts[0]) + '{:<10}'.format(option_parts[1]) + '{:<50}'.format(option_parts[2][:-1]))

def options_command(prompt_win, side_win, selected_module_number, modules_properties_list, selected_module_options_values):
    print_contextual_help(side_win, "module", selected_module_number, modules_properties_list)
    clear_prompt_output(prompt_win)
    prompt_win.addstr(4, 4, "Module Options")
    prompt_win.addstr(5, 4, "Module Name: " + str(modules_properties_list[selected_module_number - 1][1]))
    for option, offset in zip(modules_properties_list[selected_module_number - 1][2:], range(0, len(modules_properties_list[selected_module_number - 1][2:]))):
        list_modules_options(prompt_win, option, offset, selected_module_options_values)
    prompt_win.refresh()

def info_command(prompt_win, side_win, selected_module_number, modules_properties_list):
    print_contextual_help(side_win, "module", selected_module_number, modules_properties_list)
    clear_prompt_output(prompt_win)
    prompt_win.addstr(4, 4, "Module Info")
    try:
        module_info_file = open('./modules/' + modules_properties_list[selected_module_number - 1][0].split('.')[0] + ".info")
        prompt_win.move(6,4)
        offset = 1
        for line in module_info_file:
            prompt_win.addstr(6 + offset, 4, line)
            offset += 1
        prompt_win.refresh()
    except:
        prompt_win.addstr(6, 4, "No module info file found!")
        prompt_win.refresh()

def set_command(prompt_win, side_win, command, selected_module_options_values, selected_module_number, modules_properties_list):
    if len(command.split()) != 3:
        invalid_command(prompt_win, side_win, selected_module_number, modules_properties_list)
    else:
        try:
            index = [element[0] for element in selected_module_options_values].index(command.split()[1])
            selected_module_options_values[index][1] = command.split()[2]
        except:
            prompt_win.addstr(4, 4, "No such option")

def handle_prompt_input(prompt_win, modules_properties_list):
    selected_module_number = 0
    selected_module_options_values = []
    while 1:
        prompt_win.addstr(2, 1, "stubborn_> ")
        prompt_win.clrtoeol()
        prompt_win.box()
        prompt_win.refresh()
        command = prompt_win.getstr().decode("utf-8")
        if command == 'exit':
            exit_script()
        elif command == 'help':
            help_command(side_win, prompt_win, selected_module_number, modules_properties_list)
        elif command == 'list':
            list_command(side_win, prompt_win, selected_module_number, modules_properties_list)
        elif command.startswith('use '):
            if len(command.split()) == 2 and 0 < int(command.split()[1]) <= len(modules_properties_list):
                selected_module_number = int(command.split()[1])
                selected_module_options_values = use_command(prompt_win, side_win, selected_module_number, modules_properties_list)
            else:
                invalid_command(prompt_win, side_win, selected_module_number, modules_properties_list)
        elif command.startswith('set ') or command == "options" or command == "info":
            if selected_module_number == 0:
                clear_prompt_output(prompt_win)
                prompt_win.addstr(4, 4, "No module was selected! Type 'use <module_number> to select module.")
            else:
                print_contextual_help(side_win, "module", selected_module_number, modules_properties_list)
                clear_prompt_output(prompt_win)
                if command == "options":
                    options_command(prompt_win, side_win, selected_module_number, modules_properties_list, selected_module_options_values)
                elif command == "info":
                    info_command(prompt_win, side_win, selected_module_number, modules_properties_list)
                elif 'set ' in command:
                    set_command(prompt_win, side_win, command, selected_module_options_values, selected_module_number, modules_properties_list)
        elif command == 'execute':
            print_contextual_help(side_win, "execute", selected_module_number, modules_properties_list)
            clear_prompt_output(prompt_win)
            prompt_win.addstr(4, 4, "EXECUTION IN PROGRESS!") #TODO execute_option()
        else:
            invalid_command(prompt_win, side_win, selected_module_number, modules_properties_list)
           
        prompt_win.move(1,0)
        prompt_win.clrtoeol()
        prompt_win.box()
        prompt_win.addstr(1,1, "stubborn_> " + str(command))
        prompt_win.refresh()

# =====    MAIN     =====
modules_properties_list = get_modules_properties_list(get_modules_files_list())

# ===== INIT SCREEN =====
stdscr = init_screen()
header_win, prompt_win, side_win, footer_win = define_windows()
print_initial_screen(stdscr, header_win, prompt_win, side_win, footer_win, modules_properties_list)

# ===== MAIN FUNCTIONAL FUNCTION =====
handle_prompt_input(prompt_win, modules_properties_list)

