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


sysArgs = sys.argv[1:]
filename = "add_item.json"
loaded_json = []

try:
    with open(filename, 'r') as json_read:
        loaded_json.extend(json.load(json_read))
        loaded_json.extend(sysArgs)
except (json.JSONDecodeError, FileNotFoundError):
    pass

with open(filename, 'w') as json_write:
    json.dump(loaded_json, json_write)
