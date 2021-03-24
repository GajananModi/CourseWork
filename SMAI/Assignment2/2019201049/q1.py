#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb  1 02:55:31 2020

@author: gsmodi
"""

import numpy as np
import pandas as pd
import csv
import heapq as hq
from sklearn.preprocessing import StandardScaler
import operator
import random

class KNNClassifier:
    
   
    
    def __init__(self):
        self.x_train=None
        self.x_test = None
        self.y_train = None 	
        self.test = None
        self.k = 5
    
    def distance(self,a,b):
        res=np.sqrt(np.sum((a-b)**2,axis=1))
        return res        
    def train(self,train_url):
        train_df = pd.read_csv(train_url,header=None)
        train_labels = train_df[train_df.columns[0]]
        train_df = train_df.drop(train_df.columns[0],axis=1)
        train_df_list = train_df.values.tolist()
        self.x_train = np.asarray(train_df_list)
        self.y_train = train_labels.values.tolist()
    
    
    def predict(self,test_url):
        test_df = pd.read_csv(test_url,header = None)
        test_df_list = test_df.values.tolist()
        self.test = np.asarray(test_df_list)
        test_predictions = self.knn(self.x_train,self.y_train,self.test,self.k)
        return test_predictions
        
    def knn(self,x_train,y_train,x_test,k):
        res=[]
        ytrain=np.array(y_train).flatten()
        pnt1=np.array(x_train)
        for rowtest in x_test:
            dist= self.distance(pnt1,rowtest)
      
            dist1=dist.flatten()
            a = np.concatenate((dist1.reshape(-1,1),ytrain.reshape(-1,1)),axis=1)
       	    a = a[a[:,0].argsort()]
     
             
            classes= set(y_train)
            d={}
            for c in classes:
                d[c]=0
            for i in range(k):
                label= a[i][1]
                d[label] = d[label]+1
            maxv=0
            for i in d:
                if(d[i]>maxv):
                    maxv=d[i]
                    key=i
            res.append(key)

        return res



