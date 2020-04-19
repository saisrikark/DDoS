"""
Each requirement will be represented as a function
create.py will call all these functions and the DDoS object will
be modified.
"""

from scapy.all import *

def generate_spoofed_mac_address(uaa=False, multicast=False, oui=None, separator=':', byte_fmt='%02x'):
   mac = [random.randrange(256) for _ in range(6)]
   if oui:
      if type(oui) == str:
         oui = [int(chunk) for chunk in oui.split(separator)]
         mac = oui + [random.randrange(256) for _ in range(6-len(oui))]
   else:
      if multicast:
         mac[0] |= 1 # set bit 0
      else:
         mac[0] &= ~1 # clear bit 0
      if uaa:
         mac[0] &= ~(1 << 1) # clear bit 1
      else:
         mac[0] |= 1 << 1 # set bit 1
   return separator.join(byte_fmt % b for b in mac)

def generate_spoofed_ip_address():
   return ".".join(map(str, (random.randint(0, 255) for _ in range(4))))

def spoof_mac_address(ddos_attack_object):
   for index in range(len(ddos_attack_object.packets)):
      ddos_attack_object.packets[index][Ether].src = generate_spoofed_mac_address()

def spoof_ip_address(ddos_attack_object):
   for index in range(len(ddos_attack_object.packets)):
      ddos_attack_object.packets[index][IP].src = generate_spoofed_ip_address()

def modify_ddos_attack_object(ddos_attack_object, script_args):
   #spoof_mac_address(ddos_attack_object)
   #spoof_ip_address(ddos_attack_object)
   return ddos_attack_object
