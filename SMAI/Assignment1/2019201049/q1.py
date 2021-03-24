#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np


# In[2]:


def unpickle(file):
    import pickle
    with open(file, 'rb') as fo:
        dict = pickle.load(fo, encoding='bytes')
    return dict


# In[5]:


data1=unpickle('/home/gsmodi/Music/OneDrive_1_29-02-2020/Datasets/Question-1/cifar-10-batches-py/data_batch_1')


# In[6]:


data2=unpickle('/home/gsmodi/Music/OneDrive_1_29-02-2020/Datasets/Question-1/cifar-10-batches-py/data_batch_2')


# In[ ]:


data3=unpickle('/content/drive/My Drive/cifar-10-batches-py/data_batch_2')


# In[ ]:


data4=unpickle('/content/drive/My Drive/cifar-10-batches-py/data_batch_4')


# In[ ]:


data5=unpickle('/content/drive/My Drive/cifar-10-batches-py/data_batch_5')


# In[8]:


n1=list(data1.items())
n1=np.asarray(n1)


# In[9]:


labels=n1[1,1]
print(labels)
color_code=n1[2,1]
print(color_code)


# In[10]:


from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(color_code,labels, test_size=0.2,random_state=42)


# In[11]:


from sklearn import svm
from sklearn.metrics import accuracy_score
def svm_linear(c):
  clf = svm.SVC(probability=False ,kernel='linear',C=c,gamma = 'auto')
  clf.fit(x_train,y_train)
  
  y_pred = clf.predict(x_test)
  print(accuracy_score(y_test, y_pred))


# In[12]:


c=[0.1]
for i in c:
  svm_linear(i)  


# In[ ]:


#from matplotlib import pyplot as plt
#data=x_train[132].reshape(32,32,3)

#plt.imshow(data)


# In[ ]:


from sklearn.decomposition import PCA
pca = PCA(n_components=200)
x_train=pca.fit_transform(x_train)


# In[ ]:


from sklearn.decomposition import PCA
pca = PCA(n_components=200)
x_test=pca.fit_transform(x_test)


# In[ ]:


print(x_train.shape)
print(x_test.shape)


# In[ ]:


#c_svm_linear = [2,10,100]
c_svm_linear = [0.1]
for c in c_svm_linear:
  svm_linear(c)


# In[ ]:




