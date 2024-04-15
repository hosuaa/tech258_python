# Check JSON

import sys, os, json

if len(sys.argv) > 1:  # do we have more than 1 argument (is an argument given since the first is always the file name)
    if os.path.exists(sys.argv[1]):  # is the first filename passed actually present
        file = open(sys.argv[1], "r")
        json.load(file)
        file.close()
        print("JSON is valid!")
    else:
        print(f"{sys.argv[1]} not found")
else:
    print("Usage: python check_json.py <file>")
