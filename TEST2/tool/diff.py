import shelve
import pydot
from sklearn import tree
from sklearn.externals.six import StringIO


train_sample = raw_input("Enter the train sample data path: ")
pcap_metadata = raw_input("Enter the sample metadata path: ")

train_data = shelve.open(train_sample)
metadata = shelve.open(pcap_metadata)

sample = train_data['res'][0]
labels = train_data['res'][1]

pcap_meta = metadata['res']

#train 
clf = tree.DecisionTreeClassifier(criterion='entropy')
clf.fit(sample,labels)

#generate pdf 
dot_data = StringIO()
tree.export_graphviz(clf,out_file=dot_data)
graph = pydot.graph_from_dot_data(dot_data.getvalue())

#classify
metadata_length = len(pcap_meta)
index = 0
tmp = []

def classifier(data,clf):
    answer = clf.predict(data)
    if answer[0] == 'TARGET':
        return 'one'
    else:
        return 'next'

while index < metadata_length:
    result = classifier(pcap_meta[index],clf)
    if result == 'one':
        tmp.append(index+4)
        index = index + 3
    else:
        index = index + 1

result_length = len(tmp)
keys = range(result_length)

 
print('The target packet location is lines: ',tmp)
print('The decision tree pdf is tree.pdf')
graph.write_pdf('tree.pdf')

