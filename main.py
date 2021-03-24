import sys

from web_scraper import WebScraper
from hockey_reference_url_retriever import HockeyReferenceUrlRetriever


def main(year, skaterFilePath):
    #goalieFile = open(goalieFilePath)
    
    with open(skaterFilePath, 'r') as file:
        for line in file:
            player = line.strip('\n')
            print(f"Getting skater stats for {player}")
            url_retriever = HockeyReferenceUrlRetriever(player)
            url = url_retriever.get_url()
            if url:
                scraper = WebScraper(url)
                points = scraper.get_player_stats_for_year('points', year)
                print(f"{player} had {points} points in {year}")

def printUsage():
    print("USAGE: python3 main.py <year> <skaterFile> <goalieFile>")
    print("- year: Last hockey year of the season to get for (e.g. 2020-21 season would be 2021)")
    print("- skaterFile: List of skaters, split by endlines, to get points")
    print("- goalieFile: List of goalies, split by endlines, to get wins and shutouts")
    sys.exit()

if __name__ == "__main__":
    args = sys.argv[1:]
    if len(args) < 2:
        print("Invalid number of arguments!")
        printUsage()
    if 'help' in args[0]:
        printUsage()

    main(args[0], args[1])
    