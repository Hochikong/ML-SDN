from scapy.all import *
import shelve

def extra(obj):
    """
    Extra the metadata from pcap file

    """

    lines = []
    tcp = 10
    udp = 20
    others = 30
    index = [1,2,3]
    
    file_length = len(obj)
 
    for i in range(file_length):
        tmp = []
        if TCP in obj[i]:
            tmp.append(tcp)
            tmp.append(obj[i][TCP].flags)
            for c in index:
                if TCP in obj[i+c]:
                    tmp.append(obj[i+c][TCP].flags)
                else:
                    tmp.append(0)
            lines.append(tmp)
            continue
        elif UDP in obj[i]:
            tmp.append(udp)
            tmp.extend([0,0,0,0])
            lines.append(tmp)
            continue
        else:
            tmp.append(others)
            tmp.extend([0,0,0,0])
            lines.append(tmp)
            continue

    return lines

if __name__ == "__main__":
    file = raw_input("Enter the pcap file: ")
    obj = rdpcap(file)
    result = extra(obj)
    save_path = raw_input("Enter the save path: ")
    save = shelve.open(save_path)
    save['res'] = result
    save.close()
