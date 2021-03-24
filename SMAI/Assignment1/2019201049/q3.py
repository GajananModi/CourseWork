#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split 
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score,mean_absolute_error,mean_squared_error
import sys

class Airfoil:
    def __init__(self):
        self.X_test=None
        self.g=None
    
    def gradient_decent(X_train,Y_train,theta,learning_rate,iterations):
        for i in range(iterations):
            theta = theta - (learning_rate/len(X_train)) * np.sum(X_train * (X_train @ theta.T - Y_train), axis=0)
        return theta       
        
        
        
    def train(self,path):
        df=pd.read_csv(path,header=None)
        X=df.drop(labels=[5],axis=1)
        Y=df[5]
        X = (X - X.mean())/X.std()
        X= pd.concat([X,Y],axis=1)
        ones = np.ones([X.shape[0],1])
        Y = X.iloc[:,5:6].values
        X = X.iloc[:,0:5]
        X = np.concatenate((ones,X),axis=1)
        learning_rate = 0.01
        iterations = 1000
        theta = np.zeros([1,6])
        self.g = self.gradient_decent(X,Y,theta,learning_rate,iterations)
        self.g = self.g[0]
        
        
        
    def predict(self,path):
        X_test=pd.read_csv(path,header=None)
        X_test= (X_test - X_test.mean())/X_test.std()
        y_pred = []
        for index,rows in X_test.iterrows():
            y = 0
            rows = list(rows)
            for i in range(len(rows)):
                y = y + rows[i]*self.g[i+1]
            y = y + self.g[0]
            y_pred.append(y)
        return y_pred
        
        
        
        
        
        
        