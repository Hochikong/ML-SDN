import shelve
filename = raw_input('Enter the sample file: ')
dicname = raw_input('Enter the dic file: ')

f = shelve.open(filename)
dic = shelve.open(dicname)
dicdata = dic['DICT']
sample = f['res']

res = []
labels = ['RESTAPI', 'SOAPAPI', 'XMLRPC']
res_labels = []

for i in sample:
    tmp = []
    for x in sample[i]:
        if x in dicdata:
            tmp.append(dicdata[x])
        if x == 'application/json':
            label = labels[0]
            res_labels.append(labels[0])
        if x == 'SOAPAction':
            label = labels[1]
            res_labels.append(labels[1])
        if x == '<methodCall>':
            label = labels[2]
            res_labels.append(labels[2])
    res.append(tmp)

fres = {}
fres['sample'] = res
fres['label'] = res_labels

f = shelve.open('tranres.dat')
f['res'] = fres
f.close()
