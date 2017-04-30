from scapy.all import *
import shelve

pcap = raw_input("Enter pcap file path: ")
file = rdpcap(pcap)
lines = []

while True:
    l = raw_input(
        "Enter the line you want to extract,enter 'enough' to extract: ")
    if l == 'enough':
        break
    else:
        lines.append(int(l) - 1)

raw_pkt = {}
for i in lines:
    raw_pkt[i] = file[i]

proto_keys = ['POST /getname', 'POST / HTTP', 'POST /RPC2 HTTP']
payload_keys = ['application/json', 'SOAPAction', '<methodCall>']

propertys = {}
for i in lines:
    propertys[i + 1] = []
    propertys[i + 1].append(raw_pkt[i].src)
    propertys[i + 1].append(raw_pkt[i][IP].src)
    propertys[i + 1].append(raw_pkt[i].dst)
    propertys[i + 1].append(raw_pkt[i][IP].dst)
    propertys[i + 1].append(str(raw_pkt[i].dport))
    if Raw not in raw_pkt[i]:
        propertys[i + 1].append('unknown')
        propertys[i + 1].append('unknown')
    if Raw in raw_pkt[i]:
        tmp = str(raw_pkt[i][Raw].load)
        for x in proto_keys:
            if x in tmp:
                propertys[i + 1].append(x)
                break
        if len(propertys) == 5:
            propertys[i + 1].append('unknown')
        for x in payload_keys:
            if x in tmp:
                propertys[i + 1].append(x)
                break
        if len(propertys) == 6:
            propertys[i + 1].append('unknown')

print('Extraction have finished')
name = raw_input("Please use a new file to save it: ")
save = shelve.open(name)
save['res'] = propertys
save.close()
