import xlrd
import shelve

def translate(obj,sample_sheet,dic_sheet):
    """
    obj:a xlrd object 
    xxx_sheet:a index of sheet

    """
    labels = []
    sample = []

    #Get the raw sample
    raw_sample = []
    sample_table = obj.sheets()[sample_sheet-1]
    sample_rows = sample_table.nrows
    for i in range(sample_rows):
        if i == 0:
            continue
	else:
            raw_sample.append(sample_table.row_values(i))

    #Get the labels
    for i in raw_sample:
    	labels.append(i[-1])
    	del i[-1]
    

    #Get the flags and its value 
    dic = []
    dic_table = obj.sheets()[dic_sheet-1]
    dic_rows = dic_table.nrows
    for i in range(dic_rows):
    	if i == 0:
    		continue
    	else:
    	    dic.append(dic_table.row_values(i))
    dic = dict(dic)

    #Translate the sample
    for i in raw_sample:
    	tmp = []
    	for x in i:
    		tmp.append(dic[x])
    	sample.append(tmp)
    	
    return sample, labels

if __name__ == "__main__":
    file = raw_input("Enter the xlsx file: ")
    obj = xlrd.open_workbook(file)
    sample_sheet = input("Enter the sample sheet number: ")
    dic_sheet = input("Enter the dictionary sheet number: ")
    result = translate(obj,sample_sheet,dic_sheet)
    save_path = raw_input("Enter the save path: ")
    save = shelve.open(save_path)
    save['res'] = result
    save.close()
