import pandas as pd


def loadtxt(file):
    f = open(file, 'r', encoding='utf-8')
    lines = f.readlines()
    dataset_m = []
    for line in lines:
        temp1 = line.strip('\n')
        if temp1[:2] == '201' or temp1 == '':
            continue
        else:
            dataset_m.append(temp1)
    return dataset_m


def write_csv(datalist):
    f = pd.DataFrame(data=datalist)
    f.to_csv('./record.csv', encoding='utf-8')
    return f


file_txt = 'record.txt'
file = loadtxt(file_txt)
write_csv(file)
