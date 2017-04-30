from sklearn.naive_bayes import MultinomialNB
import time
import shelve

sample = raw_input('Enter the sample file: ')
expdata = raw_input('Enter the experience data: ')

digt_sample = shelve.open(sample)
digt_expdata = shelve.open(expdata)

sample_data = digt_sample['res']['sample']
sample_label = digt_sample['res']['label']

start = time.clock()

clf = MultinomialNB()
clf.fit(sample_data, sample_label)

SOAP = 0
REST = 0
XMLRPC = 0
MISS = 0

for i in digt_expdata['res']:
    if len(digt_expdata['res'][i]) == 7:
        if clf.predict(digt_expdata['res'][i])[0] == 'SOAPAPI':
            SOAP += 1
        if clf.predict(digt_expdata['res'][i])[0] == 'XMLRPC':
            XMLRPC += 1
        if clf.predict(digt_expdata['res'][i])[0] == 'RESTAPI':
            REST += 1
    else:
        MISS += 1

end = time.clock()

print("SOAP flows: ", SOAP)
print("REST flows: ", REST)
print("XMLRPC flows: ", XMLRPC)
print("Cannot identify: ", MISS)
print("Cost: %f seconds") % (end - start)
