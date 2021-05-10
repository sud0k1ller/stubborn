#!/usr/bin/python3

import argparse
from os import listdir as listdir
from itertools import islice as islice
from importlib import import_module as import_module
from sys import argv as argv
from stubborn_modules import *


def get_modules_list():
    modules_list = listdir('./modules')
    modules_list = [element for element in modules_list if '.py' in element ]
    modules_list = [element for element in modules_list if not element.startswith('\.')]
    modules_list.remove('__init__.py')
    return modules_list

def print_available_modules_list():
    modules_list = get_modules_list()
    print("Available modules:\n")
    for module in modules_list:
        print("\t - " + module ) 
    exit(0)

def print_modules_info(module_name):
    try:
        module_info_file = open('./modules/' + module_name[:-3] + '.info' )
        for line in module_info_file.readlines():
            print(line, end='')
    except:
        print("Module has no info file or info file opening failed")
        exit(1)

def execute_module():
    if not args.module_name:
        print("No module set!")
        exit(1)
  
    options_values = {}
    for option_value in args.module_options:
        options_values.update({option_value.split('=')[0]:option_value.split('=')[1]})
  
    end = False
    processed_line = 3
    options_dictionary = {}
    while not end:
        line = [element for element in islice(open('./modules/' + args.module_name), processed_line-1, processed_line)]
        if line[0][1:].strip() == 'END':
            end = True
        else:
            if line[0].split(',')[1] == 'yes':
                options_dictionary.update({line[0].split(',')[0][1:]:True})
            else:
                options_dictionary.update({line[0].split(',')[0][1:]:''})
    
        processed_line += 1
    
    [options_dictionary.update({key:options_values.get(key)}) for key in options_values.keys() if key in options_dictionary.keys()]    
    
    required_missed = False
    arguments = []
    for option in options_dictionary:
        arguments.append(options_dictionary.get(option))
        if options_dictionary.get(option) == True:
            print("Required option " + option + " was not set!")
    if required_missed:        
        exit(1)
    
    #module = import_module("stubborn_modules." + args.module_name[:-3])
    #arguments = []
    #module.main(arguments)
    
    print(options_dictionary)
    print(arguments)

def main():
    if len(argv) < 2:
        parser.print_help()
    #--list-modules
    if args.list_boolean:
        print_available_modules_list()
    #--info
    if args.info_module:
        print_modules_info(args.info_module)
    #--execute        
    if args.execute_boolean:
        execute_module()

parser = argparse.ArgumentParser(description='stubborn - set of script to gain persistency on Linux-based systems', epilog='by sud0k1ller (2021)')

parser.add_argument('-l', '--list-modules',     action='store_true',    dest='list_boolean',        help='List all available modules')
parser.add_argument('-i', '--info',             action='store',         dest='info_module',         help='Print information about given module')
parser.add_argument('-m', '--module',           action='store',         dest='module_name',         help='Set module to be used')
parser.add_argument('-s', '--set',              action='store',         dest='module_options',      help='Set module\'s options. Example: --set OPTION_NAME=VALUE', nargs='+')
parser.add_argument('--execute',                action='store_true',    dest='execute_boolean',     help='Execute choosen module with given options')

args = parser.parse_args()

main()

