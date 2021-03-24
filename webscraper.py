from bs4 import BeautifulSoup
import requests

url = 'https://www.hockey-reference.com/players/m/mcdavco01.html'
response = requests.get(url)

content = BeautifulSoup(response.content, 'html.parser')



print(content)