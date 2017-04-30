from sklearn.feature_extraction import FeatureHasher
import numpy as np
import shelve

inputfile = raw_input("Enter the raw feature file: ")
rawfile = shelve.open(inputfile)
rawdata = rawfile['res']
res = {}

h = FeatureHasher(n_features=5, non_negative=True, input_type='string')

for i in rawdata:
    f = h.transform(rawdata[i])
    if len(f.toarray()) < 7:
        res[i] = (f.toarray()).reshape(1, len(f.toarray())*5)
    if len(f.toarray()) == 7:
        res[i] = (f.toarray()).reshape(1, 35)

savefile = raw_input(
    'Translate have finish,choose a new file to save the result: ')
temp = shelve.open(savefile)
temp['res'] = res
temp.close()
