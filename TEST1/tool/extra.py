from scapy.all import *
import shelve

pcap = raw_input("Enter pcap file path: ")
file = rdpcap(pcap)
lines = []

while True:
    l = raw_input("Enter the line you want to extract,enter 'enough' to extract: ")
    if l == 'enough':
        break
    else:
	lines.append(int(l)-1)
	    
raw_pkt = {}
for i in lines:
    raw_pkt[i] = file[i]

proto_keys = ['POST /getname','POST / HTTP','POST /RPC2 HTTP']
payload_keys = ['application/json','SOAPAction','<methodCall>']

propertys = {}
for i in lines:
    propertys[i] = []
    propertys[i].append(raw_pkt[i].src)
    propertys[i].append(raw_pkt[i][IP].src)
    propertys[i].append(raw_pkt[i].dst)
    propertys[i].append(raw_pkt[i][IP].dst)
    propertys[i].append(str(raw_pkt[i][IP].dport))
    tmp = str(raw_pkt[i][Raw].load)
    for x in proto_keys:
        if x in tmp:
            propertys[i].append(x)
            break
    for x in payload_keys:
	if x in tmp:
	    propertys[i].append(x)
            break

print('Extraction have finished')
name = raw_input("Please use a new file to save it: ")
save = shelve.open(name)
save['res'] = propertys
save.close()
