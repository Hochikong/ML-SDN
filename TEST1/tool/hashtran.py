from sklearn.feature_extraction import FeatureHasher
import shelve

inputfile = raw_input("Enter the raw feature file: ")
rawfile = shelve.open(inputfile)
rawdata = rawfile['res']
res = {}

h = FeatureHasher(n_features=5, non_negative=True, input_type='string')

for i in rawdata:
    f = h.transform(rawdata[i])
    res[i] = f.toarray()

savefile = raw_input(
    'Translate have finish,choose a new file to save the result: ')
temp = shelve.open(savefile)
temp['res'] = res
temp.close()
