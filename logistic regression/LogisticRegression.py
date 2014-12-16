# -*- coding: utf-8 -*-
"""
Created on Tue Nov 25 14:56:54 2014

@author: windream
"""

from sklearn.linear_model import LogisticRegression
import numpy as np
import scipy.sparse as sp

ftrx = open("/Users/windream/Desktop/project/trainCombine","r")
ftry = open("/Users/windream/Desktop/project/label","r")
ftex = open("/Users/windream/Desktop/project/testCombine","r")
fteid = open("/Users/windream/Desktop/project/test_ID","r")
ftw = open("/Users/windream/Desktop/project/testPredict","w")

print('train')
r = []
c = []
d = []
colnum = int(ftrx.readline().strip())
rownum = 4042896
print('rowline')
rowline = ftrx.readline().strip().split(' ')
for i in range(len(rowline)):
    r.append(int(rowline[i]))
rowline = []

print('colline')
colline = ftrx.readline().strip().split(' ')
for i in range(len(colline)):
    c.append(int(colline[i]))
colline = []

print('dataline')
dataline = ftrx.readline().strip().split(' ')
for i in range(len(dataline)):
    d.append(int(dataline[i]))
dataline = []

print(max(r))
print(len(r))
print(rownum)
print(max(c))
print(len(c))
print(colnum)

X = sp.coo_matrix((d,(r,c)), shape=(rownum,colnum))
y = np.loadtxt(ftry)
clf=LogisticRegression(penalty='l1', dual=False, tol=0.0001, C=1.0, fit_intercept=True, 
                       intercept_scaling=1, class_weight=None, random_state=None)
#==============================================================================
# penalty='l2', dual=False, tol=0.0001, C=1.0, fit_intercept=True, intercept_scaling=1, class_weight=None, random_state=None
#==============================================================================
#==============================================================================
# penalty : string, ‘l1’ or ‘l2’
# Used to specify the norm used in the penalization.
# 
# dual : boolean
# Dual or primal formulation. Dual formulation is only implemented for l2 penalty. Prefer dual=False when n_samples > n_features.
# 
# C : float, optional (default=1.0)
# Inverse of regularization strength; must be a positive float. Like in support vector machines, 
# smaller values specify stronger regularization.
# 
# fit_intercept : bool, default: True
# Specifies if a constant (a.k.a. bias or intercept) should be added the decision function.
# 
# intercept_scaling : float, default: 1
# when self.fit_intercept is True, instance vector x becomes [x, self.intercept_scaling], i.e. 
# a “synthetic” feature with constant value equals to intercept_scaling is appended to the 
# instance vector. The intercept becomes intercept_scaling * synthetic feature weight Note! the 
# synthetic feature weight is subject to l1/l2 regularization as all other features. To lessen 
# the effect of regularization on synthetic feature weight (and therefore on the intercept) 
# intercept_scaling has to be increased
# 
# class_weight : {dict, ‘auto’}, optional
# Over-/undersamples the samples of each class according to the given weights. If not given, all 
# classes are supposed to have weight one. The ‘auto’ mode selects weights inversely proportional 
# to class frequencies in the training set.
# 
# random_state: int seed, RandomState instance, or None (default) :
# The seed of the pseudo random number generator to use when shuffling the data.
# 
# tol: float, optional :
# Tolerance for stopping criteria.
#==============================================================================




clf.fit(X,y)
print(clf.classes_)

print('test')
r = []
c = []
d = []
colnum = int(ftex.readline().strip())
rownum = 4577464

print('rowline')
rowline = ftex.readline().strip().split(' ')
for i in range(len(rowline)):
    r.append(int(rowline[i]))
rowline = []

print('colline')
colline = ftex.readline().strip().split(' ')
for i in range(len(colline)):
    c.append(int(colline[i]))
colline = []

print('dataline')
dataline = ftex.readline().strip().split(' ')
for i in range(len(dataline)):
    d.append(int(dataline[i]))
dataline = []

print(max(r))
print(len(r))
print(rownum)
print(max(c))
print(len(c))
print(colnum)


X = sp.coo_matrix((d,(r,c)), shape=(rownum,colnum))
test_label = clf.predict_proba(X)
print(len(test_label))

ftw.write('id,click\n')
for predict in test_label:
    id = fteid.readline().strip()
    #print(predict)
    #ftw.write(str(id)+","+str(predict[0])+"\n")
    ftw.write(str(id)+","+str(predict[1])+"\n")
ftw.close()
    

