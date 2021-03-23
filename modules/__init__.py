#!/usr/bin/python3
import os

file_list = os.listdir('./modules')
file_list = [ filename[:-3] for filename in file_list if ".py" in filename ]
file_list.remove("__init__")
		
__all__ = file_list
#print(__all__)
