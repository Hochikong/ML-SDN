from sklearn import svm
import time
import shelve

sample = raw_input('Enter the sample file: ')
expdata = raw_input('Enter the experience data: ')

digt_sample = shelve.open(sample)
digt_expdata = shelve.open(expdata)

sample_data = digt_sample['res']['sample']
sample_label = digt_sample['res']['label']

start = time.clock()

clf = svm.SVC()
clf.fit(sample_data, sample_label)

SOAP = 0
REST = 0
XMLRPC = 0
MISS = 0

SOAPlines = []
RESTlines = []
XMLRPClines = []

for i in digt_expdata['res']:
    if digt_expdata['res'][i].size == 35:
        if clf.predict(digt_expdata['res'][i])[0] == 'SOAPAPI':
            SOAP += 1
            SOAPlines.append(i)
        if clf.predict(digt_expdata['res'][i])[0] == 'XMLRPC':
            XMLRPC += 1
            XMLRPClines.append(i)
        if clf.predict(digt_expdata['res'][i])[0] == 'RESTAPI':
            REST += 1
            RESTlines.append(i)
    else:
        MISS += 1

end = time.clock()

print("SOAP flows: ", SOAP, "Lines: ", SOAPlines)
print("REST flows: ", REST, "Lines: ", RESTlines)
print("XMLRPC flows: ", XMLRPC, "Lines: ", XMLRPClines)
print("Cannot identify: ", MISS)
print("Cost: %f seconds") % (end - start)
