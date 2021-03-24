# -*- coding: utf-8 -*-
"""q3.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1z20-FanE4L0h-6vKL8GifFODowf4pLnM
"""

!conda install -y -c rdkit rdkit;
!pip install pandas==0.23.0

!wget -c https://repo.continuum.io/miniconda/Miniconda3-latest-Linux-x86_64.sh
!chmod +x Miniconda3-latest-Linux-x86_64.sh
!time bash ./Miniconda3-latest-Linux-x86_64.sh -b -f -p /usr/local
!time conda install -q -y -c conda-forge rdkit

!pip install git+https://github.com/samoturk/mol2vec;

import matplotlib.pyplot as plt
import sys
import os
















sys.path.append('/usr/local/lib/python3.7/site-packages/')

import rdkit as chem

import numpy as np
import pandas as pd
import seaborn as sns

import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings("ignore")

#Load the dataset and extract target values
mdf= pd.read_csv('/content/drive/My Drive/q3/train.csv')
mtest=pd.read_csv('/content/drive/My Drive/q3/test.csv')
t1=pd.read_csv('/content/drive/My Drive/q3/test.csv')
mdf.head()
mtest.head()

target = mdf['Binding Affinity']
mdf.drop(columns='Binding Affinity',inplace=True)
mtest.drop(columns='Binding Affinity',inplace=True)

mdf.head()

target.head()

#Importing Chem module
from rdkit import Chem 
mdf['mol'] = mdf['SMILES sequence'].apply(lambda x: Chem.MolFromSmiles(x))

from rdkit import Chem 
mtest['mol'] = mtest['SMILES sequence'].apply(lambda x: Chem.MolFromSmiles(x))

mdf.head()

mtest.head()

from gensim.models import word2vec
model = word2vec.Word2Vec.load('/content/drive/My Drive/q3/model_300dim.pkl')

from mol2vec.features import mol2alt_sentence, mol2sentence, MolSentence, DfVec, sentences2vec
from gensim.models import word2vec
print('Molecular sentence:', mol2alt_sentence(mdf['mol'][1], radius=1))
print('\nMolSentence object:', MolSentence(mol2alt_sentence(mdf['mol'][1], radius=1)))
print('\nDfVec object:',DfVec(sentences2vec(MolSentence(mol2alt_sentence(mdf['mol'][1], radius=1)), model, unseen='UNK')))

!conda install rdkit

from rdkit import Chem
from rdkit.Chem import DataStructs
from rdkit.Chem import AllChem
from rdkit.Chem import RDConfig
from rdkit import rdBase
from rdkit.Chem.Draw import IPythonConsole

mdf['sentence'] = mdf.apply(lambda x: MolSentence(mol2alt_sentence(x['mol'], 1)), axis=1)

mtest['sentence'] = mtest.apply(lambda x: MolSentence(mol2alt_sentence(x['mol'], 1)), axis=1)

mdf['mol2vec'] = [DfVec(x) for x in sentences2vec(mdf['sentence'], model, unseen='UNK')]
X = np.array([x.vec for x in mdf['mol2vec']])
y = target.values

X.shape



mtest['mol2vec'] = [DfVec(x) for x in sentences2vec(mtest['sentence'], model, unseen='UNK')]
Xtest = np.array([x.vec for x in mtest['mol2vec']])

Xtest.shape

from sklearn.model_selection import train_test_split



X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=.1, random_state=1)

!pip install searchgrid

from sklearn.svm import SVR
from sklearn.model_selection import learning_curve, GridSearchCV
import numpy as np
param_grid = {'C':[22], 'gamma': [0.0007],'kernel': ['rbf'],'epsilon':[1.3]}
svr = SVR()
grid = GridSearchCV(SVR(),param_grid,refit=True,verbose=2)
grid.fit(X,y)
print(grid.best_estimator_)

y1 = grid.predict(Xtest)
print(y1[2])
df_pred = pd.DataFrame(data = [[x,y] for x,y in zip(t1,y1)], columns=["SMILES sequence","Binding Affinity"])
#df_pred["Binding Affinity"] = y1.reshape(len(y1),1)
df_pred.to_csv("/content/drive/My Drive/submissionfinal.csv", sep=',',index=False)
print(np.shape(mtest), np.shape(y1))

from sklearn.metrics import mean_squared_error
mean_squared_error(y_test, y1)

!pip  install optunity

import math
import itertools
import optunity
import optunity.metrics
import sklearn.svm
import matplotlib.pylab as plt
import time

def svr_tuned_predictions(x_train, y_train, x_test, y_test):
    @optunity.cross_validated(x=x_train, y=y_train, num_iter=2, num_folds=5)
    def tune_cv(x_train, y_train, x_test, y_test, C, gamma):
        model = sklearn.svm.SVR(C=C, gamma=gamma).fit(x_train, y_train)
        predictions = model.predict(x_test)
        return optunity.metrics.mse(y_test, predictions)

    optimal_pars, _, _ = optunity.minimize(tune_cv, 200, C=[0, 20],
                                           gamma=[0, 10], pmap=optunity.pmap)
    tuned_model = sklearn.svm.SVR(**optimal_pars).fit(x_train, y_train)
    return tuned_model.predict(x_test).tolist()

import pandas as pd
pd.set_option("display.precision", 17)
ans=pd.DataFrame(y1)

ans.head()
#ans['Binding Affinity']=pd.DataFrame(y1)
print(ans.shape)
ans.to_csv('/content/drive/My Drive/submission_28.csv',index=False)

np.savetxt("/content/drive/My Drive/submissiont.csv", y1,fmt="%11.9f",header ="Binding Affinity",comments='', delimiter=",")

float_format='%.16g'




