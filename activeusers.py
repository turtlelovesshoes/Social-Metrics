import json
import unicodedata
#import datatime
from datetime import datetime
#data stores
active = []
answers = {}
solutions = {}

with open("users.json") as tweetfile:
   pyresponse = json.loads(tweetfile.read())


for i in pyresponse['results']:
    if i['is_active'] == True:
       active.append(i)
##I tried to store the date time, but it is stored as unicode
for i in active:
    x = i['date_joined']
    datetime.strptime(x, '%Y-%m-%dT%H:%M:%SZ')

#store users with solutions
for i in active:
    if i['solution_count']>=1:
       solution[i['username']]= i['solution_count']

#Store number of answers for users with answers
for i in active:
    if int(i['answer_count']) >=1:
       answers[i['username']]= i['answer_count']

#right now these are empty - dicts and unicode?
# research left off with https://stackoverflow.com/questions/956867/how-to-get-string-objects-instead-of-unicode-from-json
print "Users with solutions:\n"
print solutions
print "Users with answers:\n"
print answers
