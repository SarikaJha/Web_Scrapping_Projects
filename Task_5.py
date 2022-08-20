import requests
import json
from bs4 import BeautifulSoup

url_list=[]
with open('1_movies_data.json','r') as f:
    a=json.load(f)
for i in a:
    url_list.append(i['link'])

b=url_list[:250]
# print(b)
list=[]
for j in b :
    r=requests.get(j)
    soup=BeautifulSoup(r.content,"html.parser")
    c=soup.find('script',type='application/ld+json').text
    h=json.loads(c)
    dic={}
    for k in h:
        dic['name']=h['name']
        dic['director']=h['director'][0]['name']
        dic['image']=h['image']
        dic['description']=h['description']
        dic["language"]=h['review']['inLanguage']
        dic['genre']=h['genre']
        dic['Runtime']=h['duration']
        dic['country']='india'
    list.append(dic)

with open('Task5.json','w') as file:
    json.dump(list,file,indent=4)