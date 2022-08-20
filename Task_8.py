import json

with open("1_movies_data.json","r") as f1:
    a=json.load(f1)
i=0
while i<len(a)-1:
    l=a[i]["link"]
    x=l[-10:-1]
    i=i+1
    with open(x+".json","w") as f:
        json.dump(a[i],f,indent=4)