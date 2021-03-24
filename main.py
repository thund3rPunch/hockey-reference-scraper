import sys

from web_scraper import WebScraper
from hockey_reference_url_retriever import HockeyReferenceUrlRetriever


def main(year, skaterFilePath, goalieFilePath, goalsFilePath, assistFilePath, pimFilePath):
    with open("output.txt", 'w') as output:
        with open(skaterFilePath, 'r') as file:
            for line in file:
                player = line.strip('\n')
                output.writelines(f"{_get_stat(player, 'points', year)}\n")

        output.writelines("---------------------------------\n")

        with open(goalieFilePath, 'r') as file:
            for line in file:
                player = line.strip('\n')
                output.writelines(f"{_get_stat(player, 'wins_goalie', year)}\t{_get_stat(player, 'shutouts', year)}\n")

        output.writelines("---------------------------------\n")

        with open(goalsFilePath, 'r') as file:
            for line in file:
                player = line.strip('\n')
                output.writelines(f"{_get_stat(player, 'goals', year)}\n")

        output.writelines("---------------------------------\n")

        with open(assistFilePath, 'r') as file:
            for line in file:
                player = line.strip('\n')
                output.writelines(f"{_get_stat(player, 'assists', year)}\n")

        output.writelines("---------------------------------\n")

        with open(pimFilePath, 'r') as file:
            for line in file:
                player = line.strip('\n')
                output.writelines(f"{_get_stat(player, 'pen_min', year)}\n")

def _get_stat(player, stat, year):
    url_retriever = HockeyReferenceUrlRetriever(player)
    scraper = WebScraper(url_retriever.get_url())
    return scraper.get_player_stats_for_year(f'{stat}', year)

def printUsage():
    print("USAGE: python3 main.py <year> <skaterFile> <goalieFile>")
    print("- year: Last hockey year of the season to get for (e.g. 2020-21 season would be 2021)")
    print("- skaterFile: List of skaters, split by endlines, to get points")
    print("- goalieFile: List of goalies, split by endlines, to get wins and shutouts")
    sys.exit()

if __name__ == "__main__":
    args = sys.argv[1:]
    if len(args) < 6:
        print("Invalid number of arguments!")
        printUsage()
    if 'help' in args[0]:
        printUsage()

    main(args[0], args[1], args[2], args[3], args[4], args[5])
    