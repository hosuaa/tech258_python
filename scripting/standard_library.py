# Python standard library

# Modules that were so useful they were added to python by default

import random
import math
import os
import sys
import datetime
import builtins
import requests

# print(random.random()) # float between 0 and 1
# print(random.randrange(1, 10)) # int between 1 and 9

# num_float = 23.66
# print(math.ceil(num_float)) # round up
# print(math.floor(num_float)) # round down
# print(math.pi) # pi
# print(f"Remainder from 1/5: {math.remainder(1, 5)}")

working_dir = os.getcwd()
print(f"Current working directory: {working_dir}")

user = os.environ.get("USERNAME") or os.environ.get("USER")
print(f"Username: {user}")

cpu_cores = os.cpu_count()
print(f"Num of cores: {cpu_cores}")

os.mkdir("test_dir")
os.rmdir("test_dir")

# print(f"Current path: {sys.path}")
# print(f"Current python version: {sys.version}")

# print(f"Today's date is: {datetime.datetime.today()}")

# builtins are basically functions like print(), round()... (different to keywords like or, and...)
# for name in dir(builtins):
#     if name[0].islower():
#         print(name)

# request_bbc = requests.get("https://www.bbc.co.uk")
# print(request_bbc.status_code) # 200 -> Ok
# print(request_bbc.content)

