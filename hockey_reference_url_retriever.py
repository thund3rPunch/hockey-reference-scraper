from bs4 import BeautifulSoup
import requests

PREPEND_URL = 'https://www.hockey-reference.com'


class HockeyReferenceUrlRetriever:
    def __init__(self, player):
        self.player = player
        self.url = None

    def get_player(self):
        return self.player

    def get_url(self):
        if not self.url:
            player_url = "+".join(self.player.split(" "))
            search_url = f'https://www.hockey-reference.com/search/search.fcgi?&search={player_url}'
            response = requests.get(search_url)
            new_url = response.url
            if "search.fcgi" in new_url:
                soup = BeautifulSoup(response.content, 'html.parser')
                result = soup.find(class_="search-item-name")
                res2 = result.find('a', href=True)['href']
                self.url = PREPEND_URL + res2
            else:
                self.url = new_url
        return self.url