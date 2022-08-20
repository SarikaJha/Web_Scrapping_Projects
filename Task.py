from bs4 import BeautifulSoup
import requests
import json

try:
    source=requests.get("https://www.imdb.com/india/top-rated-indian-movies/")  
    source.raise_for_status()    
    
    soup=BeautifulSoup(source.text,'html.parser')
    
    movies=soup.find('tbody',class_='lister-list').find_all('tr')
    list=[]

    for movie in movies:
        data={"movie":"","rank":"","rating":"","year":"","link":""}
        name=movie.find('td',class_="titleColumn").a.text  
        year=movie.find('td',class_="titleColumn").span.text.strip("()")
        rank=movie.find('td',class_="titleColumn").get_text(strip=True).split('.')[0]  
        rating=movie.find('td',class_="ratingColumn imdbRating").strong.text

        url=movie.find('td',class_="titleColumn").a["href"]
        movie_url="https://www.imdb.com"+url
        data["movie"]=name
        data["rank"]=rank
        data["rating"]=rating
        data["year"]=year
        data["link"]=movie_url
        list.append(data)
        print(rank,name,year,rating)

    with open("1_movies_data.json","w") as f:
        json.dump(list,f,indent=4)
        
except Exception as e:
    print(e)
