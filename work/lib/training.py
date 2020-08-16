import numpy as np
import pandas as pd

from sklearn import preprocessing

x_column = 5

def get_num_classes(kind):
    return 37 if kind == 'loto7' else (43 if kind == 'loto6' else 31)

def get_x_data(data, index):
    ret = []
    num_classes = get_num_classes(data[0].kind)
    for i in range(x_column):
        d = data[index - x_column + i].numbers.split(',')
        d = list(map(int,d))

        even = list(filter(lambda x: x % 2 == 0, d))
        odd  = list(filter(lambda x: x % 2 != 0, d))

        plus  = [x + 1 for x in d]
        plus = [num_classes if p > num_classes else p for p in plus]
        
        minus = [x - 1 for x in d]
        minus = [1 if m < 1 else m for m in minus]

        ret += d
        ret += [len(even), len(odd)]
        ret += plus
        ret += minus
    return ret

def fit_transform(x):
    mm = preprocessing.MinMaxScaler()
    return mm.fit_transform(x)

# データ準備
def prepare_data(f1, f2 = ''):
    
    X = []
    Y = []
    
    if f1:
        X = pd.read_csv(f1,encoding = "utf-8", header=None)
        
    if f2:
        Y = pd.read_csv(f2,encoding = "utf-8", header=None)
        
    return np.array(X), np.array(Y)