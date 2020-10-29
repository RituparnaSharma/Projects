
# Importing The Libraries
import numpy as np 
import matplotlib.pyplot as plt
import pandas as pd
from textblob import TextBlob
import nltk
from nltk.stem.porter import PorterStemmer


#importing the data set
col_names= ['label','text',]
dataset= pd.read_csv('tweets.csv',sep='\t',names = col_names)

x = dataset.iloc[:, 1:2].values
y = dataset.iloc[:, :-1].values




fp1 = open("preprocess.txt",'w')
fp2= open("preprocesssentiment.txt",'w')
# Data preprocessing
import re
count = 0

def preprocessing(tweet,sentiment):
    
    global count
    tweet = re.sub('(www\.[^\s]+)','', str(tweet)) # remove url
    tweet = re.sub(r'https?:\/\/.*\/\w*', '', str(tweet))# remove hyperlink
    tweet = re.sub(r'&\w*', '', str(tweet))#remove &amp
    tweet = re.sub('@[^\s]+','',tweet)#remove @
    tweet = re.sub(r'#\w*', '',str(tweet))#remove hashtags
    tweet = re.sub(r'\$\w*', '', str(tweet))   # Remove tickers
    tweet = tweet.strip(' ')#remove white spaces from the front and end of a string
    tweet= tweet.lower() # remove upper case
    negations_dic = {"isn't":"is not", "aren't":"are not", "wasn't":"was not", "weren't":"were not",
                "haven't":"have not","hasn't":"has not","hadn't":"had not","won't":"will not",
                "wouldn't":"would not", "don't":"do not", "doesn't":"does not","didn't":"did not",
                "can't":"can not","couldn't":"could not","shouldn't":"should not","mightn't":"might not",
                "mustn't":"must not"}
    t =re.compile(r'\b(' + '|'.join(negations_dic.keys()) + r')\b')
    tweet = t.sub(lambda x: negations_dic[x.group()],str(tweet))
    tweet = re.sub('[^a-zA-Z]',' ', str(tweet)) # take alphabet only
    tweet=TextBlob(tweet).correct()
    tweet = re.sub('[\s]+', ' ', str(tweet) ) #Remove additional white spaces
    tweet = tweet.strip(' ')#remove white spaces from the front and end of a string
    tweet=tweet.split() 
    ps = PorterStemmer()#removal of suffices, like “ing”, “ly”, “s”, etc
    tweet= ' '.join(tweet)
    
    length = len(tweet.split())

    if length!=0:
        
         fp2.writelines(sentiment +'\n')   
         fp1.writelines(tweet +'\n')
        
        
    
    
for i in range(0,10):
    preprocessing(x[i][0],y[i][0])    
fp1.close()
fp2.close()
    

            





