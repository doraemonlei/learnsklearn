#!/usr/bin/env python
# -*- coding:utf-8 -*-
'''
@time: 2018/9/10 19:36
@author: Silence
'''
import numpy as np
import pickle as pkl

dic = {}

arr = np.random.randint(1, 100, 50)
for i,j in enumerate(arr):
    dic[i] = j

with open('baocun.pkl', 'wb') as f:
    pkl.dump(dic, f)

with open('baocun1.pkl', 'wb') as f2:
    pkl.dump(arr, f2)

if __name__ == '__main__':
    with open('baocun.pkl', 'rb') as f:
        data = pkl.load(f)
    print(data)

    with open('baocun1.pkl', 'rb') as f2:
        data2 = pkl.load(f2)
    print(data2)