# hockey-reference-scraper
Hockey Reference Webscraper for Data
Scrapes data from hockeyreference.com

REQUIRES:
Developed with Python 3.8+, should run with Python 3.6+
- Uses BeautifulSoup4 (install with pip)

USAGE:
```
python3 main.py <year> <skaterFile> <goalieFile>
```
- `year`: Last hockey year of the season to get for (e.g. 2020-21 season would be 2021)
- `skaterFile`: A file containing a list of skaters to get points for, split by endlines
- `goalieFile`: A file containing a list of goalies to get wins and shutouts for, split by endlines