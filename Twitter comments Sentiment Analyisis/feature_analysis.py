
import sys,tweepy,csv,re
from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
from textblob import TextBlob
import nltk
from nltk.stem.porter import PorterStemmer
from sklearn import svm
from sklearn.naive_bayes import MultinomialNB
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score


import pandas as pd  
import numpy as np
import matplotlib.pyplot as plt
from tkinter import *
root = Tk()
root.title('Tweets')
root.geometry('1024x724+200+50')
class GUI:
    var_chk = IntVar()
    global Positivecount
    global NegativeCount
    global Neutralcount
           #importing the data set
    col_names= ['text',]
    col_names2= ['label']
    col_names3= ['tweet']
    dataset2= pd.read_csv("preprocess.txt",sep='\t',names = col_names)
    dataset3=  pd.read_csv("preprocesssentiment.txt",sep='\t',names = col_names2)
    dataset3.loc[dataset3['label']=='positive','label']=0
    dataset3.loc[dataset3['label']=='negative','label']=1
    dataset3.loc[dataset3['label']=='neutral','label']=2
       
    tf = TfidfVectorizer(max_df=0.5,ngram_range=(1,2))
    txt_fitted1 = tf.fit_transform(dataset2['text'])
    X_train, X_test, y_train, y_test = train_test_split(txt_fitted1 ,dataset3['label'], test_size=0.33, random_state=42)

    classifier1 = MultinomialNB()
    classifier1.fit(X_train,y_train)
    y_pred=classifier1.predict(X_test)
    ac1=(accuracy_score(y_test, y_pred))*100
    ac1=str(("%.2f" % ac1))+"%"
    
    classifier2 = svm.SVC(kernel='linear', C = 1.0)
    classifier2.fit(X_train,y_train)
    y_pred=classifier2.predict(X_test)
    ac2=(accuracy_score(y_test, y_pred))*100
    ac2=str(("%.2f" % ac2))+"%"
    
    classifier3= LogisticRegression(random_state=0, solver='lbfgs',multi_class='multinomial')
    classifier3.fit(X_train,y_train)
    y_pred=classifier3.predict(X_test)
    ac3=(accuracy_score(y_test, y_pred))*100
    ac3=str(("%.2f" % ac3))+"%"
    
    
    classifier11 = MultinomialNB()
    classifier22 = svm.SVC(kernel='linear', C = 1.0)
    classifier33= LogisticRegression(random_state=0, solver='lbfgs',multi_class='multinomial')
    classifier11.fit(txt_fitted1,dataset3['label'])
    classifier22.fit(txt_fitted1,dataset3['label'])
    classifier33.fit(txt_fitted1,dataset3['label'])
    def __init__(self,API_KEY, API_SECRET_KEY,ACESS_TOKEN_KEY, ACESS_TOKEN_SECRET_KEY):
        self.API_KEY=API_KEY
        self.API_SECRET_KEY=API_SECRET_KEY
        self.ACESS_TOKEN_KEY=ACESS_TOKEN_KEY
        self. ACESS_TOKEN_SECRET_KEY= ACESS_TOKEN_SECRET_KEY
    
    def StatusBar(self,frame1):
        self.status = Label(frame1, text='Twitter sentiment analyser.......',bd=1,relief=SUNKEN,anchor=W,font=("Times New Roman",12,"bold"),bg='#7ed2df',fg='WHITE')
        self.status.pack(side =TOP,expand=YES, fill=X)
    def SearchBar(self,frame2):
        self.status1= Label(frame2, text="Search Tweet",font=("Times New Roman",12,"bold"))
        self.status1.grid(row=0,column=0,sticky=W,padx=(230,70))
        
        self.search1= Entry(frame2)
        self.search1.grid(row=1,column=0,sticky=W,ipadx=(30),padx=(230,70))
        
        self.status2= Label(frame2, text="No of Search Tweet",font=("Times New Roman",12,"bold"))
        self.status2.grid(row=0,column=1,sticky=W)
        
        self.search2= Entry(frame2)
        self.search2.grid(row=1,column=1,sticky=W,ipadx=(10))
        
        
        self.button=Button(frame2,text='Search',command=self.Getsearch)
        self.button.grid(row=1,column=2,sticky=W,padx=20)
        self.TextBox2 = Text(frame2,wrap= WORD,bd=1,width=20,height=3)
        self.TextBox2.grid(row=1,column=3,padx=(100,50))
        sentence1="multinomial ="+str(self.ac1)+"\n"
        sentence2="SVM = "+str(self.ac2)+"\n"
        sentence3="Logistic = "+str(self.ac3)+"\n"
        self.TextBox2.insert(0.0,sentence1)
        self.TextBox2.insert(0.0,sentence2)
        self.TextBox2.insert(0.0,sentence3)
        
        
    
    def multinomialNB(self):
        self.TxtBox.delete(1.0,END)
        mn1="********  MULTINOMIAL NB  ************"
        mn2="********************"+"\n"+"\n"
        dataset4 =  pd.read_csv('tweets.csv',sep='\t',names =self. col_names3)
        txt_fitted2=self. tf.transform(dataset4['tweet'])
        
        y_pred=self.classifier11.predict(txt_fitted2)
        
        self.PositiveCount=0
        self.NegativeCount=0
        self.NeutralCount=0
        for val in y_pred:
            if(val==0):
                self.PositiveCount= self.PositiveCount+1
                
            elif(val==1):
                self.NegativeCount= self.NegativeCount+1
            else:
                self.NeutralCount=self.Neutralount+1
    
        No = int(self.search2.get())
        self.TxtBox.insert(0.0,mn2)
        percent3=(self.NeutralCount/No)*100
        percent3="\n"+"Neutrale tweet Percent="+ str(("%.2f" % percent3))+"%"+"\n"+"\n"
        self.TxtBox.insert(0.0,percent3)
        percent2=(self.NegativeCount/No)*100
        percent2="\n"+"Negative tweet Percent="+ str(("%.2f" % percent2))+"%"+"\n"
        self.TxtBox.insert(0.0,percent2)
        percent1=(self.PositiveCount/No)*100
        percent1="\n"+"Positive tweet Percent="+ str(("%.2f" % percent1))+"%"+"\n"
        self.TxtBox.insert(0.0,percent1)
        self.TxtBox.insert(0.0,mn1)
        
    
    def SVM(self):
        self.TxtBox.delete(1.0,END)
        mn1="********  SVM  ************"
        mn2="********************"+"\n"+"\n"
        dataset4 =  pd.read_csv('tweets.csv',sep='\t',names = self.col_names3)
        txt_fitted2= self.tf.transform(dataset4['tweet'])
        
        y_pred=self.classifier22.predict(txt_fitted2)
        
        self.PositiveCount=0
        self.NegativeCount=0
        self.NeutralCount=0
        for val in y_pred:
            if(val==0):
                self.PositiveCount= self.PositiveCount+1
            elif(val==1):
                self.NegativeCount= self.NegativeCount+1
            else:
                self.NeutralCount=self.NeutralCount+1
            
        No = int(self.search2.get())
        self.TxtBox.insert(0.0,mn2)
        percent3=(self.NeutralCount/No)*100
        percent3="\n"+"Neutrale tweet Percent="+ str(("%.2f" % percent3))+"%"+"\n"+"\n"
        self.TxtBox.insert(0.0,percent3)
        percent2=(self.NegativeCount/No)*100
        percent2="\n"+"Negative tweet Percent="+ str(("%.2f" % percent2))+"%"+"\n"
        self.TxtBox.insert(0.0,percent2)
        percent1=(self.PositiveCount/No)*100
        percent1="\n"+"Positive tweet Percent="+ str(("%.2f" % percent1))+"%"+"\n"
        self.TxtBox.insert(0.0,percent1)
        self.TxtBox.insert(0.0,mn1)
     
    def logistic_regression(self):
        self.TxtBox.delete(1.0,END)
        mn1="********  Logistic Regression  ************"
        mn2="********************"+"\n"+"\n"
        dataset4 =  pd.read_csv('tweets.csv',sep='\t',names = self.col_names3)
        txt_fitted2= self.tf.transform(dataset4['tweet'])
        
        y_pred=self.classifier33.predict(txt_fitted2)
        
        self.PositiveCount=0
        self.NegativeCount=0
        self.NeutralCount=0

        for val in y_pred:
            if(val==0):
                self.PositiveCount= self.PositiveCount+1
            elif(val==1):
                self.NegativeCount= self.NegativeCount+1
            else:
                self.NeutralCount=self.NeutralCount+1  
            
        No = int(self.search2.get())
        self.TxtBox.insert(0.0,mn2)
        percent3=(self.NeutralCount/No)*100
        percent3="\n"+"Neutrale tweet Percent="+ str(("%.2f" % percent3))+"%"+"\n"+"\n"
        self.TxtBox.insert(0.0,percent3)
        percent2=(self.NegativeCount/No)*100
        percent2="\n"+"Negative tweet Percent="+ str(("%.2f" % percent2))+"%"+"\n"
        self.TxtBox.insert(0.0,percent2)
        percent1=(self.PositiveCount/No)*100
        percent1="\n"+"Positive tweet Percent="+ str(("%.2f" % percent1))+"%"+"\n"
        self.TxtBox.insert(0.0,percent1)
        self.TxtBox.insert(0.0,mn1)
                        
    def Getsearch(self):
 
        auth = OAuthHandler(self.API_KEY,self.API_SECRET_KEY )
        auth.set_access_token(self.ACESS_TOKEN_KEY,self.ACESS_TOKEN_SECRET_KEY)
        api = tweepy.API(auth)
        searchTerm = str(self.search1.get())
        NoOfTerms = int(self.search2.get())
        tweets=tweepy.Cursor(api.search, q=searchTerm, lang = "en").items(NoOfTerms)
        fp1 = open("tweets.csv",'w')
        count=1
        xx=[]
        count=1
        for tweet in tweets:
            xx.append(tweet.text)
        for tweet in xx:
            tweet = re.sub('(www\.[^\s]+)','', str(tweet) )# remove url
            tweet = re.sub(r'https?:\/\/.*\/\w*', '', str(tweet))# remove hyperlink
            tweet = re.sub(r'&\w*', '', str(tweet))#remove &amp
            tweet = re.sub('@[^\s]+','',str(tweet))#remove @
            tweet = re.sub(r'#\w*', '',str(tweet))#remove hashtags tweet = re.sub(r'\$\w*', '', str(tweet))   # Remove tickers
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
            
            tweet = re.sub(r'\b\w{1,2}\b', '', str(tweet))# Remove words with 2 or fewer letters
            tweet = re.sub('[\s]+', ' ', str(tweet)) #Remove additional white spaces
            tweet = tweet.strip(' ')#remove white spaces from the front and end of a string
            tweet=tweet.split() 
            ps = PorterStemmer()#removal of suffices, like “ing”, “ly”, “s”, etc
            tweet= str(' '.join(tweet))
            
            tweetx="\n"+tweet+"\n"
            self.TxtBox.insert(0.0,tweetx)
            count=count+1
            fp1.writelines(tweet +'\n') 
        fp1.close()
        
        
       
    def TextBox(self,frame3):
        
        self.TxtBox = Text(frame3, width=70,height=30,wrap= WORD,bd=1)
        self.TxtBox.grid(row=0,column=0,pady=30)
    
        
    def RadioButton(self,frame4):
        
        button1=Button(frame4,text='Multinomial',bd=1,relief=RAISED,anchor=W,font=("Times New Roman",12,"bold"),bg='#7ed2df',fg='WHITE',command=self.multinomialNB)
        button2=Button(frame4,text='SVM',bd=1,relief=RAISED,font=("Times New Roman",12,"bold"),bg='#7ed2df',fg='WHITE',command=self.SVM)
        button3=Button(frame4,text='Logistic Regression',bd=1,relief=RAISED,anchor=W,font=("Times New Roman",12,"bold"),bg='#7ed2df',fg='WHITE',command=self.logistic_regression)
       

        button1.grid(row=0,column=0,padx=20)
        button2.grid(row=0,column=1,ipadx=20)
        button3.grid(row=0,column=2, padx=20)
        
frame1 = Frame(root)
frame1.pack(fill=X)
frame2= Frame(root)
frame2.pack()
frame3= Frame(root)
frame3.pack()
frame4=Frame(root)
frame4.pack()
gui=GUI('8ZvSj9ZbmF5c3J465uWULNfdy','4m9MfNpnVn0KOKBVIYA4ln8Qh5OpEJN8OQmocwtXEbRPhoanD8','1122524987791818752-t1mc65xSFdHTU2WSmZtd63Odw9RQg2' ,'iSXnGfJ4Ug4L0D4lC0tCRKyjF8GV0g8Xgs7lPcl5zkAe4' )

gui.StatusBar(frame1)
gui.SearchBar(frame2)
gui.TextBox(frame3)
gui.RadioButton(frame4)

mainloop()
