import requests
from bs4 import BeautifulSoup

response = requests.get("https://news.ycombinator.com/news")
resp_text = response.text
soup = BeautifulSoup(resp_text, features='html.parser')

posts = soup.select("span.titleline a")
scores = soup.select("span.score")
for i in range(0,5):
    title = posts[i*2].text
    url = posts[i*2]['href']
    score = scores[i].text
    print(f"{title}, {url}, {score}")