from bs4 import BeautifulSoup
# import lxml <- if html parser not working

with open("Intermediate/Day_045/beautiful_soup/website.html") as file:
    contents = file.read()

soup = BeautifulSoup(contents, features='html.parser')
soup.title.string

# soup.prettify()
# soup.p

all_anchor_tag = soup.find_all(name="a")

for tag in all_anchor_tag:
    print(tag.getText())
    print(tag.get("href"))

heading = soup.find(name="h1", id="name")
print(heading.getText())

section_heading = soup.find(name="h3", class_="heading")
print(section_heading.getText())

name = soup.select_one(selector="#name")
print(name.getText())

headings = soup.select(".heading")
print(headings)