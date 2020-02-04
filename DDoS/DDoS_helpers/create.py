"""
This part will create a DDoS attack object
most of the simple parameters will be placed here
to change the attack object
"""

from scapy.all import IP, TCP, UDP, ICMP, send

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
        pass

def create_ddos_attack_object(script_args):
    base_attack_object = base_attack_class(script_args)
    base_attack_object.construct_empty_packets()
    base_attack_object.add_base_packet_parameters()
    return base_attack_object