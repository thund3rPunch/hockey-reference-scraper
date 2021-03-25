import sys

from web_scraper import WebScraper
from hockey_reference_url_retriever import HockeyReferenceUrlRetriever


def main(year, skater_file_path, goalie_file_path, goals_file_path, assists_file_path, pim_file_path):
    skater_stats = []
    skaters = _file_read(skater_file_path)
    for skater in skaters:
        points = _get_stat(skater, 'points', year)
        skater_stats.append([skater, points])

    goalie_stats = []
    goalies = _file_read(goalie_file_path)
    for goalie in goalies:
        wins = _get_stat(goalie, 'wins_goalie', year)
        shutouts = _get_stat(goalie, 'shutouts', year)
        goalie_stats.append([goalie, wins, shutouts])

    goal_stats = []
    goalPlayers = _file_read(goals_file_path)
    for skater in goalPlayers:
        goals = _get_stat(skater, 'goals', year)
        goal_stats.append([skater, goals])

    assist_stats = []
    assist_players = _file_read(assists_file_path)
    for skater in assist_players:
        assists = _get_stat(skater, 'assists', year)
        assist_stats.append([skater, assists])

    pim_stats = []
    pim_players = _file_read(pim_file_path)
    for skater in pim_players:
        pim = _get_stat(skater, 'pen_min', year)
        pim_stats.append([skater, pim])

    _output_to_file(skater_stats, goalie_stats, goal_stats, assist_stats, pim_stats)

def _file_read(filePath):
    player_list = []
    with open(filePath, 'r') as file:
        for line in file:
            player_list.append(line.strip('\n'))
    return player_list
            

def _get_stat(player, stat, year):
    url_retriever = HockeyReferenceUrlRetriever(player)
    scraper = WebScraper(url_retriever.get_url())
    return scraper.get_player_stats_for_year(f'{stat}', year)

def _output_to_file(skater_stats, goalie_stats, goal_stats, assistStats, pim_stats):
    with open("output.txt", 'w') as output:
        _output_single_stat(output, skater_stats)
        output.writelines("---------------------------------\n")
        _output_double_stat(output, goalie_stats)
        output.writelines("---------------------------------\n")
        _output_single_stat(output, goal_stats)
        output.writelines("---------------------------------\n")
        _output_single_stat(output, assistStats)
        output.writelines("---------------------------------\n")
        _output_single_stat(output, pim_stats)

def _output_single_stat(output, statistic):
    for stat in statistic:
        output.writelines(f"{stat[0]}\t{stat[1]}\n")

def _output_double_stat(output, statistic):
    for stat in statistic:
        output.writelines(f"{stat[0]}\t{stat[1]}\t{stat[2]}\n")

def printUsage():
    print("USAGE: python3 main.py <year> <skaterFile> <goalieFile> <goalsFile> <assistsFile> <pimFile>")
    print("- year: Last hockey year of the season to get for (e.g. 2020-21 season would be 2021)")
    print("- skaterFile: List of skaters, split by endlines, to get points")
    print("- goalieFile: List of goalies, split by endlines, to get wins and shutouts")
    print("- goalsFile: List of skaters, split by endlines, to get goals")
    print("- assistsFile: List of skaters, split by endlines, to get assists")
    print("- pimFile: List of skaters, split by endlines, to get PIM")
    sys.exit()

if __name__ == "__main__":
    args = sys.argv[1:]
    if len(args) < 6:
        print("Invalid number of arguments!")
        printUsage()

    main(args[0], args[1], args[2], args[3], args[4], args[5])
    