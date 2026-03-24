# Fallout Wiki Character Scraper

robots.txt: https://fallout.fandom.com/robots.txt

page: https://fallout.fandom.com/wiki/Category:Fallout_characters

Content license: CC-BY-

## robots.txt:
cloudscraper is not blocked or prohibited for this wiki.

## Why the Fallout Wiki?

Fallout is an RPG series that I love. RPGs as a genre involve alot of lore and characters for their story.

**Why characters?:** Characters are an important part of the stories of many storytelling media. Things like faction affiliation, status, role, game apperiences, and possibly race/gender of characters give a better scope of a stories world, and how that relates to the story's commentary(in fallot's case politics and society).

## Requirements

- Python 3
- cloudscraper
- beautifulsoup4

pip3 install cloudscraper beautifulsoup4

## Running:
python3 fandom_wiki_scraping.py

## Scraped info:

From the Fallout characters page
- Name
- Link
- Affiliation
- Gender 
- Race
- Role
- Games
- Status

## Output:

fallout_characters.csv