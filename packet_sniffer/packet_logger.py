import pyshark

capture = pyshark.LiveCapture(interface = 'wlp19s0')
capture.sniff(timeout = 50)
no_of_packets = len(capture)
fp = open("packets.log", "a")
for i in range(no_of_packets):
    try:
        packet_log = str(i) + " " + str(capture[i].sniff_timestamp) + " "
        packet_log = packet_log + capture[i]['eth'].src + " " + capture[i]['eth'].dst + " " 
        packet_log = packet_log + capture[i][capture[i].transport_layer.lower()].srcport + " " + capture[i][capture[i].transport_layer.lower()].dstport + " "
        if("ip" in capture[i]):
            packet_log = packet_log + capture[i]['ip'].src + " " + capture[i]['ip'].dst + " "
        else:
            packet_log = packet_log + capture[i]['ipv6'].src + " " + capture[i]['ipv6'].dst + "\n"
        fp.write(packet_log)
    except:
        pass
fp.close()

        


    



