#!/usr/bin/python3
"""
7-add_itme module

Script that adds all arguments to a Python list, and then
save them to a file.
"""
import json
import sys
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

sysArgv = sys.argv[1:]
filename = "add_item.json"
loaded_json = []


json_data = load_from_json_file(filename)
loaded_json.append(json_data)
loaded_json.append(sysArgv)
save_to_json_file(loaded_json, filename)
