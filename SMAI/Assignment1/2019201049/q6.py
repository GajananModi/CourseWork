#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar  5 14:52:14 2020

@author: gsmodi
"""
import pandas as pd
import numpy as np
import random as rd
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from sklearn.cluster import KMeans
from sklearn.feature_extraction.text import TfidfVectorizer
import math
import os
from random import randint

class Cluster:
    def __init__(self):
      self.g=0  
    def euclidean_distance(self,x,y):
        return np.sum((x - y)**2)
    def cluster(self,path):
        files = []
# r=root, d=directories, f = files
        for r, d, f in os.walk(path):
                for file in f:
                        if '.txt' in file:
                                files.append(os.path.join(r, file))
        bagofwords=[]
        for f in files:
            fptr=open(f,'rb')
            filedata=fptr.read().decode('utf-8','ignore')
            bagofwords.append(filedata)  
        
        vectorizer = TfidfVectorizer(stop_words = 'english', lowercase = 'true')
        X = vectorizer.fit_transform(bagofwords)
        X1=X.toarray()
        df=pd.DataFrame(X1)
        c1=self.kmeans(5,df)
        return c1
        
    def kmeans(self,K,df):
    
            d = df.shape[1] 
            n = df.shape[0]
            Max_Iterations = 20
            i = 0
        
            cluster = [0] * n
        
            cluster_centers = [df.iloc[randint(0,n)] for _ in range(K) ]  #rd.choice(df)  
        
            while(i < Max_Iterations):
                i += 1
                
                for p in range(n):
                    min_dist = float("inf")
                    for c in range(K):
                        dist =self.euclidean_distance(df.iloc[p],cluster_centers[c])
                        if (dist < min_dist):
                            min_dist = dist  
                            cluster[p] = c+1
                
                new_center = [[0.0]*d] * K
                members = [0]*K
                for p in range(n):
                    new_center[cluster[p]-1] = np.add(new_center[cluster[p]-1], df.iloc[p])
                    members[cluster[p]-1] += 1
                
                for j in range(K):
                        if members[j] != 0:
                            new_center[j] = new_center[j] / float(members[j]) 
                        else: 
                            new_center[j] = df.iloc[randint(0,n)] #rd.choice(df)
                
                cluster_centers = new_center.copy()
            return cluster

        