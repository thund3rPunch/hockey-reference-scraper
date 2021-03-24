from bs4 import BeautifulSoup
import requests

class HockeyReferenceUrlRetriever:
    def __init__(self, player):
        self.player = player
        self.url = None

    def get_url(self):
        return self.url