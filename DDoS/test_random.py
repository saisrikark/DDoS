from scapy.all import *
p = IP(src="1.1.1.1",dst="127.0.0.1")/UDP()
send(p, count=100)
