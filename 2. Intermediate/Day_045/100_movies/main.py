import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

# Write your code below this line 👇

response = requests.get(URL)
resp_text = response.text

soup = BeautifulSoup(resp_text, features='html.parser')

all_title = soup.find_all(name = "h3", class_ = "title")
movies_list = []

for title in all_title:
    text = title.getText()
    # Extract rank (assumes format like "100) Movie Title")
    rank_str = text.split(")")[0]
    try:
        rank = int(rank_str)
    except ValueError:
        rank_str = text.split(")")[0].split(":")[0]
        rank = int(rank_str)
        text = text.replace(":", ")")
    movies = {
        'name': text,
        'rank': rank
    }
    movies_list.append(movies)

# Solution 2
# movies_title = [movie.getText() for movie in all_title]
# movies = movies_title[::-1]

with open("Intermediate/Day_045/100_movies/movies.txt", "w", encoding="utf-8") as file:
    for movie in reversed(movies_list):
        file.write(f"{movie['name']}\n")
        
        # Solution 2
        # file.write(f"{movie}\n")