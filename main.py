import sys
from web_scraper import WebScraper
from hockey_reference_url_retriever import HockeyReferenceUrlRetriever

def main(year, skaterFilePath, goalieFilePath):
    skaterFile = open(skaterFilePath)
    #goalieFile = open(goalieFilePath)
    
    for fileLine in skaterFile.readline():
        print(f"Getting skater stats for {str(fileLine)}")
        url_retriever = HockeyReferenceUrlRetriever(fileLine)
        url = url_retriever.get_url()
        scraper = WebScraper(url)
        points = scraper.get_player_stats_for_year('points', year)
        print(f"{str(fileLine)} had {points} in {year}")

def printUsage():
    print("Hockey Reference Webscraper for Data")
    print("USAGE: python3 main.py <year> <skaterFile> <goalieFile>")
    print("- <year>: Last hockey year of the season to get for (e.g. 2020-21 season would be 2021)")
    print("- <skaterFile>: List of skaters, split by endlines, to get points for")
    print("- <goalieFile>: List of goalies, split by endlines, to get wins and shutouts for")
    sys.exit()

if __name__ == "__main__":
    args = sys.argv[1:]
    if 'help' in args[0]:
        printUsage()
    if len(args) < 3:
        print("Invalid number of arguments!")
        printUsage()
    main(args[0], args[1], args[2])
    