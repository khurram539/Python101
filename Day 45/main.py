from bs4 import BeautifulSoup

with open ("website.html") as file:
    contents = file.read()   
    
soup = BeautifulSoup(contents, "html.parser")
# print(soup.title)
# print(soup.title.string)
# print(soup.prettify())
# print(soup.a)

soup.find_all(name="a")
print(all_anchor_tags)