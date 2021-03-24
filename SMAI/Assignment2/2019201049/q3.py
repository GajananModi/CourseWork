#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb  1 03:34:31 2020

@author: gsmodi
"""

import numpy as np
import pandas as pd

import numpy as np
from numpy import log2 as log
import pandas as pd
from sklearn import tree, preprocessing
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
from sklearn.metrics import mean_squared_error
from statistics import mean 

eps = np.finfo(float).eps

class DecisionTree:
	def train(self,URl):
		df0  = pd.read_csv('train_with_labels.csv')
		df0.drop(['Alley','PoolQC','FireplaceQu','MiscFeature','Fence','Utilities','Condition2','PoolArea','BsmtHalfBath','GarageQual'],inplace='True',axis = 1 )
		df0.replace(to_replace ="NA", value =np.nan,inplace='True')
		df0 = df0.drop(df0.columns[0],axis=1)

		df0['LotFrontage'].fillna(df0['LotFrontage'].mean(), inplace=True)
		df0['MasVnrArea'].fillna(df0['MasVnrArea'].mean(), inplace=True)
		df0['GarageYrBlt'].fillna(df0['GarageYrBlt'].mean(), inplace=True)
		df0['BsmtQual'].fillna(df0['BsmtQual'].mode()[0], inplace=True)
		df0['BsmtCond'].fillna(df0['BsmtCond'].mode()[0], inplace=True)
		df0['BsmtExposure'].fillna(df0['BsmtExposure'].mode()[0], inplace=True)
		df0['BsmtFinType1'].fillna(df0['BsmtFinType1'].mode()[0], inplace=True)
		df0['BsmtFinType2'].fillna(df0['BsmtFinType2'].mode()[0], inplace=True)
		df0['Electrical'].fillna(df0['Electrical'].mode()[0], inplace=True)
		df0['MasVnrType'].fillna(df0['MasVnrType'].mode()[0], inplace=True)
		df0["GarageCond"].fillna(df0["GarageCond"].mode()[0], inplace=True)
		df0["GarageType"].fillna(df0["GarageType"].mode()[0], inplace=True)
		df0["GarageFinish"].fillna(df0["GarageFinish"].mode()[0], inplace=True)
		




	def mse_calculate(self,a,b):
    	       	return  mean_squared_error(a,b,squared='True')

	def feature_mse(self,df, feature):
    	     	class_label = df.keys()[-1]
   	       	target_variables = df[class_label].unique()
    		variables = df[feature].unique()
  		return abs(mse)

	def class_mse(self,df):
    		class_label = df.keys()[-1]
    		class_mse = 0
    		values = df[class_label].unique()
    		list_mse=[]
   	        for val in values:
                temp_mse=[]
                df1=df.loc[df[class_label] == val,'sales_Price']
                price=df1.values.tolist()
                mean_price=mean(price)
                a=[]
                a.append(mean_price)
                b=df['SalesPrice'].values.tolist()
                a=a*len()
                class_mse = mse_calculate(b,a)
        	temp_mse.append(class_mse)
        	temp_mse.append(val)
        	list_mse.append(temp_mse)
        
    		list_mse.sort()
        
        
   	        return list_mse[0]

	def feature_to_select(self,df):
    		gain = []
   	 	for key in df.keys()[:-1]:
       		gain.append(class_mse(df))
   		return df.keys()[:-1][np.argmax(gain)]


class Node:
    
    def __init__(self,feature,positive=0,negative=0):
        self.feature=feature
        self.split_pos=0
        self.mse=0.0
        self.key=0
        self.left=None
        self.right=None
        
    def build_Tree(df):
    	if len(df.columns)==1:
         return None
    
    	split_node = feature_to_select(df)
    	root = Node(split_node)
   	 root.positive=len(df[df['left']==1]['left'])
    	root.negative=len(df[df['left']==0]['left'])
    
    
    
    	if len(counts_right)>1:
        	root.right=build_Tree(subtable_right)
        
    	return root




