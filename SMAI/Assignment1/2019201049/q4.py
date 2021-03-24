import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split 
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score,mean_absolute_error,mean_squared_error
from sklearn.preprocessing import OneHotEncoder
from sklearn.preprocessing import MinMaxScaler
from sklearn import preprocessing


class Weather:
    def __init__(self):
        self.i=0
        self.g=None
        
    def gradient_decent(self,X_train,Y_train,theta,learning_rate,iterations):
        for i in range(iterations):
            theta = theta - (learning_rate/len(X_train)) * np.sum(X_train * (X_train @ theta.T - Y_train), axis=0)
        return theta
        
    def train(self,path):
        df=pd.read_csv(path)
        df=df.drop(columns=['Formatted Date','Daily Summary'])
        df = df.dropna()
        df1=df.drop(columns=['Summary','Precip Type'])
        
        
        enc = OneHotEncoder(handle_unknown='ignore')
        enc_df = pd.DataFrame(enc.fit_transform(df[['Summary','Precip Type']]).toarray())
        df1=df.drop(columns=['Summary','Precip Type'])
        X=df1.drop(df1.columns[1],axis=1)
        Y=df1.iloc[:,1]
        X = (X - X.mean())/X.std()
        X = X.join(enc_df)
        X = X.join(Y)
        X.isna().sum()
        X = X.dropna()
        Y = X.iloc[:,-1]
        X = X.iloc[:,:-1]
        X = pd.concat([X,Y],axis=1)
        ones = np.ones([X.shape[0],1])
        Y_train = X.iloc[:,34:35].values
        X_train = X.iloc[:,0:34]
        X_train = np.concatenate((ones,X_train),axis=1)
        learning_rate = 0.1
        iterations = 10000
        # theta = np.zeros(8) # 7 is the number of features
        theta = np.zeros([1,35])
        self.g = self.gradient_decent(X_train,Y_train,theta,learning_rate,iterations)
        self.g = self.g[0]
        
        
        
    def predict(self,path):
        df=pd.read_csv(path)
        y_pred = []
        df=df.drop(columns=['Formatted Date','Daily Summary'])
        df = df.dropna()
        df1=df.drop(columns=['Summary','Precip Type'])
        enc = OneHotEncoder(handle_unknown='ignore')
        enc_df = pd.DataFrame(enc.fit_transform(df[['Summary','Precip Type']]).toarray())
        df1=df.drop(columns=['Summary','Precip Type'])
        X_test=df1
        X_test = (X_test - X_test.mean())/X_test.std()
        X_test = X_test.join(enc_df)
        X_test = X_test.dropna()
        
        for index,rows in X_test.iterrows():
            y = 0
            rows = list(rows)
            for i in range(len(rows)):
                y = y + rows[i]*self.g[i+1]
            y = y + self.g[0]
    
            y_pred.append(y)    
        return y_pred