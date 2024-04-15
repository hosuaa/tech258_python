# take a json file, and output it's contents to a new file that is valid YAML

import sys, os, json, yaml

if len(sys.argv) > 1:  # do we have more than 1 argument (is an argument given since the first is always the file name)
    if os.path.exists(sys.argv[1]):  # is the first filename passed actually present
        # file = open(sys.argv[1], "r")
        # json = json.load(file) # get json data into variable
        # with open("")
        #yaml_file = "output.yaml"
        with open("example.json", "r") as jsonfile:
            json_data = json.load(jsonfile)
            # print(json_data)
            with open('output.yml', 'w') as yaml_file:
                yaml.dump(json_data, yaml_file, default_flow_style=False)

        print("JSON is valid!")
    else:
        print(f"{sys.argv[1]} not found")
else:
    print("Usage: python check_json.py <file>")