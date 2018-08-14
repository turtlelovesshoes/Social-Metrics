#import raw tweets and count word buckets
from matplotlib import pyplot as plt
import pandas as pd
import csv
from collections import Counter


twitterwords = []
final = ''
with open('inboundunanswered.csv', 'rb') as csvDataFile:
  csvReader = csv.reader(csvDataFile, delimiter =',')
  for row in csvReader:
    twitterwords.append(row[3].split('" "'))
if(isinstance(twitterwords,list)==True):
    for i in twitterwords:
        for x in i:
            final = final + x

Countdict = Counter(final.split(" """))

#plt.plot()
key = Countdict.keys()

df = pd.DataFrame(Countdict,index=key)
df.drop(df.columns[1:], inplace=True)

df.plot(kind='bar')

plt.show()
plt.savefig("saveinbound.png")

## now for the outbound
twitterwords = []
final = ''
with open('inboundunanswered.csv', 'rb') as csvDataFile:
  csvReader = csv.reader(csvDataFile, delimiter =',')
  for row in csvReader:
    twitterwords.append(row[3].split('" "'))
if(isinstance(twitterwords,list)==True):
    for i in twitterwords:
        for x in i:
            final = final + x

Countdict = Counter(final.split(" """))

#plt.plot()
key = Countdict.keys()

df = pd.DataFrame(Countdict,index=key)
df.drop(df.columns[1:], inplace=True)

df.plot(kind='bar')

plt.show()
plt.savefig("outbound.png")
