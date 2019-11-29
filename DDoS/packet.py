'''
    Purpose of this code?
    Easily construct a packet.
    Customize it easily.
    Now we have a packet which we can use.
    This makes it easy to send an attack.
'''

from scapy.all import send
from scapy.layers.inet import IP, UDP

class packet():

    def generate_packet(self,protocol):
        protocol_dict = {
            
        }
        self.mac_src = self.spoof_mac()
        self.ip_src = self.spoof_ipv4()
        return 1
    
    def spoof_mac(self):
        # Write some code to spoof mac address
        return "00:00:00:00:00:00"

    def spoof_ipv4(self):
        # Write some code to spoof ipv4 address
        return "192.168.0.1"

    def spoof_ipv6(self):
        # Write some code to spoof ipv6 address
        return "2001:0db8:85a3:0000:0000:8a2e:0370:7334"

    def __init__(self, protocol):
        self.protocol = property
        print(property)
        #self.packet = self.generate_packet(protocol)

### Testing part ###
