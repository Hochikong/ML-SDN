import shelve
from sklearn.feature_extraction import FeatureHasher
filename = raw_input('Enter the sample file: ')

f = shelve.open(filename)
sample = f['res']
hash = FeatureHasher(n_features=5, non_negative=True, input_type='string')

res = []
labels = ['RESTAPI', 'SOAPAPI', 'XMLRPC']
res_labels = []

for i in sample:
    if 'application/json' in sample[i]:
        f = hash.transform(sample[i])
        res.append(f.toarray())
        res_labels.append(labels[0])
    if 'SOAPAction' in sample[i]:
        g = hash.transform(sample[i])
        res.append(f.toarray())
        res_labels.append(labels[1])
    if '<methodCall>' in sample[i]:
        h = hash.transform(sample[i])
        res.append(f.toarray())
        res_labels.append(labels[2])

fres = {}
fres['sample'] = res
fres['label'] = res_labels

savefile = raw_input(
    'Translate have finish,choose a new file to save the result: ')
f = shelve.open(savefile)
f['res'] = fres
f.close()
