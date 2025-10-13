import requests

response = requests.get("https://api.github.com")
print(response.status_code)


from bs4 import BeautifulSoup

html = "<h1>Hello Lakshan!</h1>"
soup = BeautifulSoup(html, "html.parser")
print(soup.h1.text)
