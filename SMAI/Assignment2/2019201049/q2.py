#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 24 11:50:26 2020

@author: aj
"""

#Importing the libraries
#import statistics 
from statistics import mode 
import numpy as np;
import pandas as pd;
from scipy.spatial import distance

from sklearn.metrics import accuracy_score,recall_score,precision_score,f1_score
from sklearn.model_selection import train_test_split

class KNNClassifier:
    
    x_train=None
    x_test = None
    y_train = None
    y_test=None

    k = 5   
    def __init__(self):
        pass
    
    
    def train(self,train_url):
        train_df = pd.read_csv(train_url,header=None)
        train_labels = train_df[train_df.columns[0]]
        train_df = train_df.drop(train_df.columns[0],axis=1)
        train_df.replace('?', np.nan)
        for column in train_df.columns:
            train_df[column].fillna(train_df[column].mode()[0], inplace=True)   
        train_df_list  = train_df.values.tolist()
        for i in range(len(train_df_list)):
            for j in range(len(train_df_list[i])):
                train_df_list[i][j] = ord(train_df_list[i][j])
        self.x_train = np.asarray(train_df_list)
        self.y_train = train_labels.values.tolist()
        
        
        
    def predict(self,test_url):
        test_df = pd.read_csv(test_url,header=None)
        test_df.replace('?', np.nan)
        for column in test_df.columns:
            test_df[column].fillna(test_df[column].mode()[0], inplace=True)
        test_df_list = test_df.values.tolist()
        for i in range(len(test_df_list)):
            for j in range(len(test_df_list[i])):
                test_df_list[i][j] = ord(test_df_list[i][j])
        self.x_test = np.asarray(test_df_list)
        self.x_test=self.x_test.tolist()
        test_predictions = self.knn_classifier(self.x_train,self.y_train,self.x_test,self.k)
        return test_predictions
        
        
        
    def knn_classifier(self,x,y_train,xtest,k):
        res=[]
        for rowtest in xtest:
            c1=0
            
            
            l=[]
            for row in x:
            
                
            
                d2=[]
                dist=distance.euclidean(row,rowtest)
                d2.append(dist)
                d2.append(c1)
                c1=c1+1
                l.append(d2)	
            l.sort()    #[[dist,index],[..],[..]]
            classes= set(y_train)
            d={}
            for c in classes:
                d[c]=0
            for i in range(k):
                ind= l[i][1]
                label = y_train[ind]
                d[label] = d[label]+1
            maxv=0
            for i in d:
                if(d[i]>maxv):
                    maxv=d[i]
                    key=i
            res.append(key)
        return res
  

'''
# Importing the dataset
dataset = pd.read_csv('/home/gsmodi/2SMAI/Assignment1 Dataset/Datasets/q2/train.csv')
y = dataset.iloc[:, 0].values             #dependent variables
dataset=dataset.replace('?',np.NaN)
dataset['?'].fillna(dataset['?'].mode()[0],inplace=True)
# Splitting the dataset into the Training set and Validation set

rows=len(dataset.index)
for r in range (0,rows):
    for row,col in enumerate(dataset):
        dataset.iloc[r][col]=ord(dataset.iloc[r][col])
x=dataset.iloc[:,1:22]
from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.25)
y_test=y_test.tolist()


# Fitting K-NN to the Training set and # Predicting the Test set results
y_pred=knn_classifier(x_train,y_train,x_test,5)


# Making the Confusion Matrix
from sklearn.metrics import confusion_matrix
cm = confusion_matrix(y_test, y_pred)
print(accuracy_score(y_test,y_pred))
print(recall_score(y_test, y_pred, pos_label='p'))
print(precision_score(y_test,y_pred))
print(f1_score(y_test,y_pred))

'''
