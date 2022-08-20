import json

f=open("2_Movie_year.json")
year=json.load(f)
def group_by_decade():
    year_1=1955
    dict={}
    for i in range(year_1,2022,10):
        movies_list=[]
        for j in year:
            if year_1<int(j) and int(j)<(year_1+10):
                movies_list.append(year[j])
        dict[year_1]=movies_list  
        year_1+=10
    with open ("Task3.json","w") as f1:
        json.dump(dict,f1,indent=5)
    # print(dict)
group_by_decade()