# hockey-reference-scraper
Hockey Reference Webscraper for Data
Scrapes data from hockeyreference.com

REQUIRES:
Developed with Python 3.8+, should run with Python 3.6+
- Uses BeautifulSoup4 (install with pip)

USAGE:
```
python3 main.py <year> <skaterFile> <goalieFile> <goalsFile> <assistsFile> <pimFile>
```
- `year`: Last hockey year of the season to get for (e.g. 2020-21 season would be 2021)
- `skaterFile`: A file containing a list of skaters to get points for, split by endlines
- `goalieFile`: A file containing a list of goalies to get wins and shutouts for, split by endlines
- `goalsFile`: A file containing a list of skaters to get goals for, split by endlines
- `assistsFile`: A file containing a list of skaters to get assists for, split by endlines
- `pimFile`: A file containing a list of skaters to get PIMs for, split by endlines

Outputs a file that contains all of the statistics, split by new lines per player, and dashes for each category

LIMITATIONS:
- Does not handle players with the same name - picks the most recent one