#Note Dataset should  already be filtered by AoA and Help Me
#this also assumes that you have gone through the tags and triagged the corrections (ex CEO properly labeled)


import csv
import pandas as pd
from collections import Counter
import numpy as np
import matplotlib.pyplot as plt

#save csv dump as dataframes
with open("firstweekHelpMeAoA.csv") as file:
        df = pd.read_csv(file)

#how many product tweets were identfied
#Tag - Firefox iOS, Android, Firefox Focus, Rocket
num_of_prod = df.tags.apply(lambda x: 'Firefox for Android' if "Android" in str(x) else x).reset_index()
num_of_prod.tags.apply(lambda x: 'Firefox for iOS' if "iOS" in str(x) else x).reset_index()
num_of_prod.tags.apply(lambda x: 'Firefox Focus' if 'focus' in str(x) else x).reset_index()
num_of_prod.tags.apply(lambda x: "Firefox" if "Firefox" not in str(x) else x).reset_index()

##start over
#split the tags to many columns where 'none' is default
#   0 1 2 3
#0  EN None none
#1  AoA Solved DNE
#2
num = df.tags.str.split(',',expand=True).apply(Counter)
#now the rows are each counter objects that need to be combined
a = num[0]
b = num[1]
c = num[2]
d = num[3]
e = num[4]
f = num[5]
final = a+b+c+d+e+f
final
 #plot user issues
labels = final.keys()
plt.bar(range(len(final)), final.values())
plt.xticks(range(len(final)), labels, rotation= "vertical")
plt.xlabel("User Issue Categories")
plt.ylabel("Conversations about that User Issue")
plt.title("User Issue Categories Firefox 61 Release Week 1")
plt.show()


categories = {}
#Grab all the Categories for Defined user issues:
for x,y in final.items():
    if (x == 'Crashes') or (x == 'slow') or (x == 'cookies') or (x == "Add-ons") or (x =='Webdev') or (x =='RAM') or (x =='Video') or (x =='Bookmarks'):
       categories.update({x:y})
    if (x == 'Cert Issues') or (x == 'Sync') or (x == 'feature request') or (x == 'update') or (x == 'HSTS') or (x=='How') or (x =='Form') or (x == 'Bookmark'):
        categories.update({x:y})
    if (x== 'Hang') or (x == 'youtube') or (x == 'tab'):
        categories.update({x:y})
#New tags and trends created for release or during
new_release_categories = {}
for x,y in final.items():
    if (x == 'VPN') or (x == 'DoH' ) or (x == 'New Release') or (x == 'Support release') or (x == 'Bug') or (x == 'playlistLive'):
      new_release_categories.update({x,y})

## Plot two subplots for trends
plt.subplots()

plt.subplot(2,1,1)
ax1 = plt.subplot(2,1,1)
labels1 = categories.keys()
plt.bar(range(len(categories)), categories.values())
ax1.set_xticklabels( labels1)
plt.xlabel("User Issue Categories")
plt.ylabel("# Support Conversations")
plt.title("User Issue Categories Firefox 61 Release Week 1")

plt.subplot(2,1,2)
ax = plt.subplot(2,1,2)
labels = new_release_categories.keys()
plt.bar(range(len(new_release_categories)), new_release_categories.values())
ax.set_xticklabels( labels, rotation= "vertical")
plt.xlabel("New User Issue Categories")
plt.ylabel("# Support Conversations")
plt.title("New User Issue Categories Firefox 61 Release Week 1")

plt.subplots_adjust(left=None, bottom=20, right=None, top=100, wspace=None, hspace=200)

plt.show()

#Grab all Help Me - count instances of other tags
#Dataset is already filtered by AoA and Help Me

#Grab all Language counts
#EN, ES, CS, TR, FR, PT_BR, NL
lang = {}
for x,y in final.items():
    if (x == 'EN') or (x =='ES') or (x =='CZ') or (x =='TR') or (x =='FR') or (x == 'DE') or (x == 'PT-BR'):
       lang.update({x:y})
#plot languages
labels = lang.keys()
 plt.bar(range(len(lang)), lang.values())
 plt.xticks(range(len(lang)), labels, rotation= "vertical")
 plt.xlabel("User Issue Languages")
 plt.ylabel("Number of Conversations in Language")
 plt.title("User Issue Languages Supported Firefox 61 Release Week 1")
 plt.show()


#Show all non-help me tags by language

#Grab A0A volume vs total #help me with response time
