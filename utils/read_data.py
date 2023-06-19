'''
Read data from csv file
One csv file, each row represents one sample with values across each of the columns of features
Use first row as headers.
for each row with m samples and n features:
 2nd row : <external variable of sample 1>, <value 1>, <value 2> ... <value n>
 3rd row : <external variable of sample 2>, <value 1>, <value 2> ... <value n>
 ...
 m+1th row: <external variable of sample m>, <value 1>, <value 2> ... <value n>

'''
from sklearn.model_selection import train_test_split

def floatizer(lst, num, scale):
    for i in range(len(lst)):
        lst[i] = round(float(lst[i]), num)*scale
    return lst

def read_data(data):
    X = []
    y = []
    lines = open(data, 'r').readlines()
    for i in range(len(lines)):
        if i == 0:
            continue
        else:
            templine = lines[i].rstrip().split(',')
            X.append(floatizer(templine[1:], 6, 100))
            y.append(float(templine[0]))

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size =0.33)
    allData = [X_train, y_train, X_test, y_test]
    return allData

def getData(data, phase):
    dataset = read_data(data)

    if phase == 'train':
        return dataset[0], dataset[1]
    elif phase == 'test':
        return dataset[2], dataset[3]

