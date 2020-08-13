import numpy as np
import pandas as pd
import os
import tensorflow as tf
import logging

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'
tf.get_logger().setLevel('INFO')
tf.get_logger().setLevel(logging.ERROR)

from sklearn import preprocessing

h5_file     = 'h5/loto.h5'
num_classes = 43
before_num  = 5

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