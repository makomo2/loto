import numpy as np
import pandas as pd

from sklearn import preprocessing

x_column = 5

def get_num_classes(kind):
    return 37 if kind == 'loto7' else (43 if kind == 'loto6' else 31)

def get_x_data(data, index):
    ret = []
    for i in range(x_column):
        ret += data[index - x_column + i].numbers.split(',')
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