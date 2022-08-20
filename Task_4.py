from bs4 import BeautifulSoup
import requests
import json

with open("1_movies_data.json","r") as f:
    a=json.load(f)
    i=0
    url=[]
    while i<len(a):
        print(i+1,":",a[i]["movie"])
        url.append(a[i]["link"])
        i=i+1
    user=int(input("enter the movie sl.No"))-1
    x=url[user]
    b=requests.get(x)
    soup=BeautifulSoup(b.text,"html.parser")
    c=soup.find('script',type='application/ld+json').text
    a=json.loads(c)
    with open("try.json","w") as f:
        json.dump(a,f,indent=4)
    with open("try.json","r") as k:
        r=json.load(k)
    dic={}
    for j in r:
        dic['Movie']=r['name']
        dic['Director']=[r['director'][0]['name']]
        dic['Country']='india'
        dic["Language"]=r['review']['inLanguage']
        dic['Image']=r['image']
        dic['Description']=r['description']
        dic['Runtime']=r['duration']
        dic['Genre']=r['genre']
        
    with open("forth_task.json","w") as k:
        json.dump(dic,k,indent=4)