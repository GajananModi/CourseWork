#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar  5 16:40:26 2020

@author: gsmodi
"""

import pandas as pd
import numpy as np
from sklearn.svm import LinearSVC
from sklearn.metrics import confusion_matrix, classification_report,accuracy_score,f1_score
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn import svm



class AuthorClassifier:
    def __init__(self):
        self.classifier=None
    	self.x=None
    
    def train(self,path):
        dataset = pd.read_csv(path)

        X=dataset.iloc[:,1].values
        y=dataset.iloc[:,2].values
        y=np.asarray(y)
        vectorizer = TfidfVectorizer()
        self.x = vectorizer.fit(text)
	xt = self.x.transform(text)
        classifier = LinearSVC(dual=False, random_state = 0)
	classifier.fit(Xt,y)



    def predict(self,path):
        classifier = svm.SVC(robability=False, kernel='linear',C=0.1,gamma='auto')
        test = pd.read_csv(path)
	x_test=self.x.transform(test)
        test=np.asarray(x_test)
        y_pred = self.classifier.predict(test)
        return y_pred



  
