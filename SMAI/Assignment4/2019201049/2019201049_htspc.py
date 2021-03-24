#!/usr/bin/env python
# coding: utf-8

# In[533]:


# Importing Libraries 
import pandas as pd
import numpy as np
import re
import matplotlib.pyplot as plt
import seaborn as sns
import nltk
import warnings 
warnings.filterwarnings("ignore", category=DeprecationWarning)


# In[618]:


# Loading Data
train_df = pd.read_csv("./train1.csv")
test_df = pd.read_csv("./test1.csv")


# Training Data Set - has 3 columns ID, Label & Tweet. Tweet columns has tweets writen by users & Label columns contains binary values 1 & 0. 

# In[ ]:





# In[619]:


test_df.head(10)


# In[620]:


#Training Data Set
train_df.head(10)


# In[621]:


#Testing Data Set
test_df.head()
print('Testing data set has no Label column')
print(test_df.head(10))


# In[622]:


# Training Data Set Information
print("Training Data Set Info - Total Rows | Total Columns | Total Null Values")
print(train_df.info())


# In[623]:


# Testing Data Set Information
print("Test Data Set Info - Total Rows | Total Columns | Total Null Values")
print(test_df.info())


# We can see in above tweet column in both data sets Training & Testing tweets are unstructured, for better analysis we first need to structure the tweets, remove the unwanted words, replace the misspelled words with the correct ones, replace the abriviation with full words

# In[624]:


# Merging both the data sets as tweets in both the data set is unstructured
combine_df = train_df
combine_df.head()


# In[625]:


# Combine (Merged) Data Set Information
print("Combine Data Set Info - Total Rows | Total Columns | Total Null Values")
print(combine_df.info())


# We can see above, ID & Tweet column has 49159 has values where as Label column has 31962 values.

# ## Data processing & cleaning
# * Step C : Changing all the tweets into lowercase 
# * Step D : Apostrophe Lookup Not done due reduce in accuracy
# * Step E : Short Word Lookup Not done
# * Step F : Emoticon Lookup
# * Step H : Replacing Special Characters with space
# * Step I : Replacing Numbers (integers) with space
# * Step J : Removing words whom length is 1 not done due to reduce in accuracy

# ### Step C : Changing all the tweets into lowercase 

# In[626]:


combine_df['clean_tweet'] = combine_df['text'].apply(lambda x: x.lower())
combine_df.head(10)


# In[627]:


test_df['clean_tweet'] = test_df['text'].apply(lambda x: x.lower())
test_df.head(10)


# ### Step D : Apostrophe Lookup

# ### Step F : Emoticon Lookup

# In[628]:


for i in range(combine_df.shape[0]):
  combine_df['clean_tweet'][i] = combine_df['clean_tweet'][i].encode('ascii', 'ignore').decode('ascii')


# In[629]:


for i in range(test_df.shape[0]):
  test_df['clean_tweet'][i] = test_df['clean_tweet'][i].encode('ascii', 'ignore').decode('ascii')


# ### Step G : ReplacingPunctuations with space

# In[630]:


combine_df['clean_tweet'] = combine_df['clean_tweet'].apply(lambda x: re.sub(r'[^\w\s]',' ',x))
combine_df.head(10)


# In[631]:


#test_df['clean_tweet'] = test_df['clean_tweet'].apply(lambda x: re.sub(r'[^\w\s]',' ',x))
#test_df.head(10)


# ### Step I : Replacing Numbers (integers) with space

# In[632]:


combine_df['clean_tweet'] = combine_df['clean_tweet'].apply(lambda x: re.sub(r'[^a-zA-Z]',' ',x))
combine_df.head(10)


# In[633]:


test_df['clean_tweet'] = test_df['clean_tweet'].apply(lambda x: re.sub(r'[^\w\s]',' ',x))
test_df.head(10)


# In[634]:


# Spelling correction is a cool feature which TextBlob offers, we can be accessed using the correct function as shown below.
blob = TextBlob("Why are you stting on this bech??") # Scentence with two errors
print(blob.correct()) # Correct function giave us the best possible word simmilar to "gret"


# In[635]:


# we can see all the similar matches our first error along with the probability score.
blob.words[3].spellcheck()


# ### Applying TextBlob on our data set - Spelling correction

# In[636]:


# Not cleaning the just showing the spelling check as its take lot of time to process all these tweets
## Shown sample how its must done
#combine_df['clean_tweet'] = combine_df['clean_tweet'][0:10].apply(lambda x: str(TextBlob(x).correct()))
#combine_df.head()


# In[637]:


# Not cleaning the just showing the spelling check as its take lot of time to process all these tweets
## Shown sample how its must done
text = combine_df['clean_tweet'][0:10].apply(lambda x: str(TextBlob(x).correct()))
text


# In[638]:


# Importing stop words from NLTK coupus and word tokenizer
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize


# In[639]:


# Creating token for the clean tweets
combine_df['tweet_token'] = combine_df['clean_tweet'].apply(lambda x: word_tokenize(x))

## Fully formated tweets & there tokens
combine_df.head(10)


# In[640]:



test_df['tweet_token'] = test_df['clean_tweet'].apply(lambda x: word_tokenize(x))

## Fully formated tweets & there tokens
test_df.head(10)


# In[641]:


# Importing stop words from NLTK corpus for english language

import nltk
nltk.download('stopwords')
stop_words = set(stopwords.words('english'))
stop_words


# In[642]:


# Created new columns of tokens - where stop words are being removed
combine_df['tweet_token_filtered'] = combine_df['tweet_token'].apply(lambda x: [word for word in x if not word in stop_words])

## Tokens columns with stop words and without stop words
combine_df[['tweet_token', 'tweet_token_filtered']].head(10)


# In[643]:


test_df['tweet_token_filtered'] = test_df['tweet_token'].apply(lambda x: [word for word in x if not word in stop_words])

## Tokens columns with stop words and without stop words
test_df[['tweet_token', 'tweet_token_filtered']].head(10)


# ## We will create 2 new columns
# * One For Stemming
# * Second For Lemmatization
# 
# The difference between stemming and lemmatization is, lemmatization considers the context and converts the word to its meaningful base form, whereas stemming just removes the last few characters, often leading to incorrect meanings and spelling errors.

# ### Stemming - Stemming refers to the removal of suffices, like “ing”, “ly”, “s”, etc. by a simple rule-based approach.

# In[644]:


# Importing library for stemming
from nltk.stem import PorterStemmer
stemming = PorterStemmer()


# In[645]:


# Created one more columns tweet_stemmed it shows tweets' stemmed version
combine_df['tweet_stemmed'] = combine_df['tweet_token_filtered'].apply(lambda x: ' '.join([stemming.stem(i) for i in x]))
combine_df['tweet_stemmed'].head(10)


# In[646]:


test_df['tweet_stemmed'] = test_df['tweet_token_filtered'].apply(lambda x: ' '.join([stemming.stem(i) for i in x]))
test_df['tweet_stemmed'].head(10)


# ### Lemmatization - Lemmatization is the process of converting a word to its base form.

# In[647]:


# Importing library for lemmatizing
from nltk.stem.wordnet import WordNetLemmatizer
lemmatizing = WordNetLemmatizer()


# In[648]:


# Created one more columns tweet_lemmatized it shows tweets' lemmatized version
combine_df['tweet_lemmatized'] = combine_df['tweet_token_filtered'].apply(lambda x: ' '.join([lemmatizing.lemmatize(i) for i in x]))
combine_df['tweet_lemmatized'].head(10)


# In[649]:


test_df['tweet_lemmatized'] = test_df['tweet_token_filtered'].apply(lambda x: ' '.join([lemmatizing.lemmatize(i) for i in x]))
test_df['tweet_lemmatized'].head(10)


# In[650]:


# Our final dataframe - Fully formatted, Processed, Noise less, Cleaned, ready to analyse
## for further analysis we consider 2 columns i.e. "tweet_stemmed" & "tweet_lematized"
### We are using 2 columns to see which of them give us better score.
combine_df.head(10)




# ## B - TF-IDF Features

# In[651]:


# Importing library
from sklearn.feature_extraction.text import TfidfVectorizer
tfidf_vectorizer = TfidfVectorizer(max_df=0.90, min_df=1, max_features=1000, stop_words='english')
tfidf_vectorizer


# ## B.1 TF-IDF feature matrix - For columns "combine_df['tweet_stemmed']"

# In[652]:


TF-IDF feature matrix - For columns "combine_df['tweet_stemmed']"
combine_df.head(3)
tfidf_stem3 = tfidf_vectorizer.fit_transform(combine_df['tweet_stemmed'])
tfidf_stem3


# In[653]:


tfidf_stem2 = tfidf_vectorizer.fit_transform(test_df['tweet_stemmed'])
tfidf_stem2


# ## B.2 TF-IDF feature matrix - For columns "combine_df['tweet_lemmatized']"

# In[654]:


# TF-IDF feature matrix - For columns "combine_df['tweet_lemmatized']"
tfidf_lemm1 = tfidf_vectorizer.fit_transform(combine_df['tweet_lemmatized'])
tfidf_lemm1


# In[655]:


# TF-IDF feature matrix - For columns "combine_df['tweet_lemmatized']"
tfidf_lemm2 = tfidf_vectorizer.fit_transform(test_df['tweet_lemmatized'])
tfidf_lemm2


# # Logistic Regression Model Building: Twitter Sentiment Analysis

# In[656]:


# Importing Libraries




# B.2 For columns "combine_df['tweet_lemmatized']"
train_tfidf = tfidf_lemm1[:5266,:]
test_tfidf = tfidf_lemm[5266:,:]




from sklearn.metrics import f1_score

from sklearn.svm import SVC
clf = SVC(kernel='linear')
clf.fit(tfidf_lemm1,combine_df['labels'])
prediction3 = clf.predict(tfidf_lemm2)
print('done')





y_pred=pd.DataFrame(data=prediction3,columns=['labels']);
print(y_pred)
y_pred.to_csv("./submissionmodig6.csv",index=True)





