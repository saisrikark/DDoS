"""
The main controller will call all the necessary file
First the create.py
Second modify.py
The send.py
"""

import argparse
from create import *
from modify import *
from send import *

def retrieve_arguments():
    ap = argparse()
    pass

def perform_attack():
    script_args = retrieve_arguments()
    ddos_attack_obj = create_ddos_attack_object(script_args)
    modified_ddos_attack_obj = modify_ddos_attack_obj(
        ddos_attack_obj, script_args)
    send_ddos_attack_obj(modified_ddos_attack_obj, script_args)
