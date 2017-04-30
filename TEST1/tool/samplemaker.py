import shelve
import numpy

filename = raw_input('Enter the feature file: ')
featurefile = shelve.open(filename)

featuredata = featurefile['res']

print('Now choose the application class you want to set: ')
type = []
lines = {}

while True:
    name = raw_input("Enter the name of application(Enter 'halt' to finish): ")
    if name == 'halt':
        break
    else:
        type.append(name)
        lines[name] = []

for name in type:
    while True:
        samplelines = raw_input("Enter the flow number of '%s' (Enter 'halt' to finish): " % name)
        if samplelines == 'halt':
            break
        else:
            lines[name].append(int(samplelines))

data = {}
data['label'] = []
tmp = []
for i in lines:
    tmpvalue = len(lines[i])
    for t in range(tmpvalue):
        data['label'].append(i)
    for s in lines[i]:
        tmp.append(featuredata[s])

data['sample'] = numpy.vstack(tmp)

print('Samples have maked')
name = raw_input("Please use a new file to save it: ")
save = shelve.open(name)
save['res'] = data
save.close()







