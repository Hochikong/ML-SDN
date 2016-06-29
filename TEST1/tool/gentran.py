import shelve
import random

filename = raw_input('Enter the property file: ')
dictname = raw_input('Enter the dictionary file: ')

dic_tmp = shelve.open(dictname)
dic = dic_tmp['DICT']
raw_file = shelve.open(filename)
raw = raw_file['res']
res = {}
random_range = [16,26]

for i in raw:
    tmp = []
    for j in raw[i]:
        if j in dic:
            tmp.append(dic[j])
	else:
            rnum = random.randint(random_range[0],random_range[1])
	    tmp.append(rnum)
    res[i] = tmp
	
savefile = raw_input('Translate have finish,choose a new file to save the result: ')
temp = shelve.open(savefile)
temp['res'] = res
temp.close()

