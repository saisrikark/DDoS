"""
This part will create a DDoS attack object
most of the simple parameters will be placed here
to change the attack object
"""

from scapy.all import *

class base_attack_class():
    
    def __init__(self, script_args):
        self.packets = []
        self.script_args = script_args
        
    def construct_empty_packets(self):
        src_ip = self.script_args["src"]
        dest_ip = self.script_args["dest"]
        print(src_ip, dest_ip)
        packet_dict = {
            "IP" : IP(src=src_ip,dst=dest_ip),
            "TCP" : IP(src=src_ip,dst=dest_ip)/TCP(),
            "UDP" : IP(src=src_ip,dst=dest_ip)/UDP(),
            "ICMP" : IP(src=src_ip,dst=dest_ip)/ICMP()
        }
        protocol = self.script_args["protocol"]
        required_base_packet = packet_dict[protocol]
        self.packets.append(required_base_packet)

    def add_base_packet_parameters(self):
        # Whatever base parameters are required, will go here
        # And will be added to the packets list
        # Hard coded
        protocol = self.script_args["protocol"]
        for name in self.script_args.keys():
            value = self.script_args[name]
            print(name, value)
            if(name == "dport" and protocol == "TCP"):
                self.packets[0][TCP].dport = value
            elif(name == "dport" and protocol == "UDP"):
                self.packets[0][UDP].dport = value
            elif(name == "sport" and protocol == "TCP"):
                self.packets[0][TCP].sport = value
            elif(name == "sport" and protocol == "UDP"):
                self.packets[0][UDP].sport = value

def create_ddos_attack_object(script_args):
    base_attack_object = base_attack_class(script_args)
    base_attack_object.construct_empty_packets()
    base_attack_object.add_base_packet_parameters()
    return base_attack_object