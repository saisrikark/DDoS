import pyshark

capture = pyshark.LiveCapture(interface = 'wlp19s0')
capture.sniff(timeout = 50)
no_of_packets = len(capture)
fp = open("packets.log", "a")
for i in range(no_of_packets):
    try:
        packet_log = str(i) + " " + "timestamp=" + str(capture[i].sniff_timestamp) + " "
        packet_log = packet_log + "src_mac_addr=" +  capture[i]['eth'].src + " " + "dst_mac_addr=" + capture[i]['eth'].dst + " " 
        packet_log = packet_log + "src_port=" + capture[i][capture[i].transport_layer.lower()].srcport + " " + "dst_port=" + capture[i][capture[i].transport_layer.lower()].dstport + " "
        if("ip" in capture[i]):
            packet_log = packet_log + "src_ip=" + capture[i]['ip'].src + " " + "dst_ip=" + capture[i]['ip'].dst + " "
        else:
            packet_log = packet_log + "src_ip=" + capture[i]['ipv6'].src + " " +"dst_ip=" +  capture[i]['ipv6'].dst + "\t\n"
        fp.write(packet_log)
    except:
        pass
fp.close()

        


    



