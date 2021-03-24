from bs4 import BeautifulSoup
import requests

class WebScraper:
    def __init__(self, url):
        self.url = url
        self.response = requests.get(self.url)
        self.soup = BeautifulSoup(self.response.content, 'html.parser')

    def get_stats_for_year(self, statistic, year):
        id_selector = f'stats_basic_plus_nhl.{year}'
        result = self.soup.find(id=id_selector)
        most_recent_stats = result.find_all('td')
        for col in most_recent_stats:
            print(col)
            print(type(col))

url = 'https://www.hockey-reference.com/players/m/mcdavco01.html'
ws = WebScraper(url)
ws.get_stats_for_year('points', '2021')