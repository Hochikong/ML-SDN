import shelve
import numpy as np
filename = raw_input('Enter the sample file: ')
print('Auto load ../data/newdict.dat ....')

f = shelve.open(filename)
dictfile = shelve.open('../data/newdict.dat')
dict = dictfile['DICT']

sample = f['res']

res = []
labels = ['RESTAPI', 'SOAPAPI', 'XMLRPC']
res_labels = []

for i in sample:
    tmp = []
    for x in sample[i]:
        if x in dict:
            tmp.append(dict[x])
        if x == 'application/json':
            res_labels.append(labels[0])
        if x == 'SOAPAction':
            res_labels.append(labels[1])
        if x == '<methodCall>':
            res_labels.append(labels[2])
    res.append(tmp)

tmp1 = []
for i in range(3):
    tmp1.append(np.vstack(tuple(res[i])))

tmp2 = []
for i in tmp1:
    tmp2.append(i.reshape(1, 35))

final = np.vstack(tuple(tmp2))

fres = {}
fres['sample'] = final
fres['label'] = res_labels

savefile = raw_input(
    'Translate have finish,choose a new file to save the result: ')
f = shelve.open(savefile)
f['res'] = fres
f.close()
