from bs4 import BeautifulSoup
import requests


class WebScraper:
    def __init__(self, url):
        self.url = url
        self.response = requests.get(self.url)
        self.soup = BeautifulSoup(self.response.content, 'html.parser')

    def get_player_stats_for_year(self, stat, year):
        statValue = 0
        id_selector = f'stats_basic_plus_nhl.{year}'
        result = self.soup.find(id=id_selector)
        try:
            most_recent_stats = result.find_all('td')
            for col in most_recent_stats:
                if stat in str(col):
                    statValue = col.text
        except Exception as e:
            print(f"Failed to find player: {e}")
        
        return statValue