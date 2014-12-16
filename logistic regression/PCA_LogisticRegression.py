# -*- coding: utf-8 -*-
"""
Created on Fri Dec  5 22:16:13 2014

@author: windream
"""

from sklearn.linear_model import LogisticRegression
import numpy as np

ftrx = np.load("train_sampled_10_features_pca.npy",mmap_mode='r')
ftry = open("label","r")
ftex = np.load("test_features_pca.npy",mmap_mode='r')
fteid = open("test_ID","r")
ftw = open("testPredict","w")

y = np.loadtxt(ftry)
clf=LogisticRegression(penalty='l2', dual=False, tol=0.0001, C=1.0, fit_intercept=True, 
                       intercept_scaling=1, class_weight=None, random_state=None)
clf.fit(ftrx,y)
test_label = clf.predict_proba(ftex)
print(len(test_label))

ftw.write('id,click\n')
for predict in test_label:
    id = fteid.readline().strip()
    ftw.write(str(id)+","+str(predict[1])+"\n")
ftw.close()
