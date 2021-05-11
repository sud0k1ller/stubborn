#!/usr/bin/python3

import argparse
from os         import listdir          as listdir
from itertools  import islice           as islice
from importlib  import import_module    as import_module
from sys        import argv             as argv
from modules    import *

def print_available_modules_list():
    modules_list = [element for element in listdir('./modules') if '.py' in element and not (element.startswith('\.') or element.startswith('__'))]
    print("\nAvailable modules:\n")
    for module in modules_list:
        print("\t - " + module ) 
    exit(0)

def print_modules_info(module_name):
    try:
        print(open('./modules/' + module_name[:-3] + '.info').read())
    except:
        print("Module has no info file or info file opening failed")
        exit(1)

def execute_module():
    if not args.module_name:
        print("No module set!")
        exit(1)
  
    options_values, options_dictionary, end, processed_line, required_missing = {}, {}, True, 3, False

    try:
        line = [element for element in islice(open('./modules/' + args.module_name), processed_line-1, processed_line)]
        while not line[0][1:].strip() == 'END':
            options_dictionary.update({line[0].split(',')[0][1:]:''})
            if line[0].split(',')[1] == 'yes':
                options_dictionary.update({line[0].split(',')[0][1:]:True})
            processed_line += 1
            line = [element for element in islice(open('./modules/' + args.module_name), processed_line-1, processed_line)]
    except:
        print("Getting module's options from " + args.module_name + " file failed")        
        exit(1)

    if not args.module_options == None:
        for option_value in args.module_options:
            options_values.update({option_value.split('=')[0]:option_value.split('=')[1]})        
        [options_dictionary.update({key:options_values.get(key)}) for key in options_values.keys() if key in options_dictionary.keys()]    
            
    if True in options_dictionary.values():
        print("Required option  was not set!")
        exit(1)
    try:
        module = import_module("modules." + args.module_name[:-3])
        module.main(list(options_dictionary.values()))
    except:
        print("Module does not exist or module execution failed")
        exit(1)

parser = argparse.ArgumentParser(description='stubborn - set of script to gain persistency on Linux-based systems', epilog='by sud0k1ller (2021)')
parser.add_argument('-l', '--list-modules',     action='store_true',    dest='list_boolean',        help='List all available modules')
parser.add_argument('-i', '--info',             action='store',         dest='info_module',         help='Print information about given module')
parser.add_argument('-m', '--module',           action='store',         dest='module_name',         help='Set module to be used')
parser.add_argument('-s', '--set',              action='store',         dest='module_options',      help='Set module\'s options. Example: --set OPTION_NAME=VALUE', nargs='+')
parser.add_argument('--execute',                action='store_true',    dest='execute_boolean',     help='Execute choosen module with given options')
args = parser.parse_args()

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
