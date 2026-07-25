import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

# Write your code below this line 👇


response = requests.get(URL)
yc_webpage = response.text

soup = BeautifulSoup(yc_webpage, 'html.parser')

top_movies = []   

movies = soup.find_all(name='h3', class_ = 'title')

for i in movies:
    top_movies.append(i.getText())
    
# movie_titles = [movie.getText() for movie in movies]

top_movies.reverse()

print(top_movies)

with open ("movies.txt" , mode='w')as file:
    for i in top_movies:
        file.write(f"{i}\n")