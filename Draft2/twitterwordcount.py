from matplotlib import pyplot as plt
import csv
import pandas as pd
from collections import Counter


#constants and dataframes

#function to open data dump and read into dataframe
def open_twitter(file):
    with open(file) as csvDataFile:
      df = pd.read_csv(csvDataFile)
    return df

def count_word(df):
    results = []
    checked = []
    count1= {}
    s=""
    df['text'].str.split(" ").apply(results.append)
    for e in results:
        for i in str(e):
           if i not in checked:
              checked.append(e)
              count1[str(i)]=1
           else:
              count1[str(i)]=count1[str(i)]+1
    return count1

#def tag_count(df):
#    return tags
def count_word2(df):
    df=pd.DataFrame(r1,columns=['text'])
    df.text.apply(lambda x: pd.value_counts(x.split(" "))).sum(axis = 0)
    return results
def count_word3(df):
    help = {}
    help = df.text

    print help.dtypes(i, 0)
    print(type(help))
    #print help.value_counts()

df1 = open_twitter("inboundunanswered.csv")
#print df1
count = []
count = count_word3(df1)

#count = count_word2(df1)


#Count words
#ax = plt.subplot()
#plt.bar(range(len(count),count)
#graph words

#count tags
#graph tags in bars
