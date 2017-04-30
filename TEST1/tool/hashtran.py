import numpy as np
import shelve

inputfile = raw_input("Enter the raw feature file: ")
print('Auto load ../data/newdict.dat ....')

rawfile = shelve.open(inputfile)
rawdata = rawfile['res']
dictfile = shelve.open('../data/newdict.dat')
dict = dictfile['DICT']

res = {}

for i in rawdata:
    tmp = []
    if len(rawdata[i]) == 7:
        for x in rawdata[i]:
            if x in dict:
                tmp.append(dict[x])
            if x not in dict:
                tmp.append(dict['unknown'])
        tmp1 = np.vstack(tuple(tmp))
        res[i] = tmp1.reshape(1, 35)
    if len(rawdata[i]) < 7:
        for x in rawdata[i]:
            if x in dict:
                tmp.append(dict[x])
            if x not in dict:
                tmp.append(dict['unknown'])
        for t in range(7 - len(tmp)):
            tmp.append(dict['unknown'])
        tmp1 = np.vstack(tuple(tmp))
        res[i] = tmp1.reshape(1, 35)

savefile = raw_input(
    'Translate have finish,choose a new file to save the result: ')
temp = shelve.open(savefile)
temp['res'] = res
temp.close()
