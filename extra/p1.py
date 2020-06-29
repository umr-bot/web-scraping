import requests
import json
import numpy as np
from datetime import datetime
def jprint(obj):
    # create a formatted string of the Python JSON object
    text = json.dumps(obj, sort_keys=True, indent=4)
    print(text)

reviews0 = requests.get( "https://api.nytimes.com/svc/movies/v2/reviews/search.json?api-key=jIYu5Trdj40I8456lQkJI2uFWiG4XtX9")
results = reviews0.json()['results']

r = results                 
r_popped = []
dictlist = [dict() for x in range(1)]
rng = len(results)
cnt = 0
for i in range(0,len(r)):
    #print(i-cnt)
    if(str(results[i-cnt]['opening_date']) == 'None'):
        dictlist.append(r.pop(i-cnt))
        cnt = cnt + 1
        #print("None %d" , i-cnt)
r.sort(key = lambda x: datetime.strptime(x['opening_date'],'%Y-%m-%d'),reverse=True)  
for j in range(1,len(dictlist)): 
    r.insert(0,dictlist[j])
r_sorted_by_opening = r.copy()
dictlist = [dict() for x in range(1)]
#r_popped = []
cnt = 0
for i in range(0,len(results)):
    if(str(r[i-cnt]['date_updated']) == 'None'):
        dictlist.append(r.pop(i-cnt))
        cnt  = cnt + 1
r.sort(key = lambda x: datetime.strptime(x['date_updated'],'%Y-%m-%d %H:%M:%S'),reverse=True)  
for j in range(1,len(dictlist)): 
    r.insert(0,dictlist[j])

r_sorted_by_date_modified = r[0:15]

#Get review author and full review
#r_sorted_by_date_modified[x]['byline'] x an int
#scrape1.py to get full review
