import csv
import time
from bs4 import BeautifulSoup
import cloudscraper

scraper = cloudscraper.create_scraper()

game_categories = [
    ("Fallout 1", "https://fallout.fandom.com/wiki/Category:Fallout_characters"),
    ("Fallout 2", "https://fallout.fandom.com/wiki/Category:Fallout_2_characters"),
    ("Fallout 3", "https://fallout.fandom.com/wiki/Category:Fallout_3_characters"),
    ("Fallout New Vegas", "https://fallout.fandom.com/wiki/Category:Fallout:_New_Vegas_characters"),
    ("Fallout 4", "https://fallout.fandom.com/wiki/Category:Fallout_4_characters"),
    ("Fallout 76", "https://fallout.fandom.com/wiki/Category:Fallout_76_characters"),
]

base_url = "https://fallout.fandom.com"

def get_character_details(url):
    try:
        response = scraper.get(url, timeout=10)
        if response.status_code != 200:
            return None
        soup = BeautifulSoup(response.text, "html.parser")

        aside = soup.find('aside')
        affiliation = None
        gender = None
        race = None
        role = None
        games = None
        status = None

        if aside:
            for section in aside.find_all('div', class_='pi-item'):
                label = section.find('h3')
                value = section.find('div', class_='pi-data-value')
                if label and value:
                    label_text = label.get_text(strip=True).lower()
                    value_text = value.get_text(separator=', ', strip=True)
                    if 'affiliation' in label_text:
                        affiliation = value_text
                    elif 'gender' in label_text:
                        gender = value_text
                    elif 'race' in label_text:
                        race = value_text
                    elif 'role' in label_text:
                        role = value_text
                    elif 'game' in label_text:
                        games = value_text
                    elif 'status' in label_text:
                        status = value_text

        return {
            "affiliation": affiliation,
            "gender": gender,
            "race": race,
            "role": role,
            "games": games,
            "status": status
        }
    except Exception as e:
        print("Error getting details: " + url + ": " + str(e))
        return None

def get_characters_from_page(url):
    try:
        response = scraper.get(url, timeout=10)
        soup = BeautifulSoup(response.text, "html.parser")

        characters = soup.find_all('a', class_='category-page__member-link')

        next_page = soup.find('a', class_='category-page__pagination-next')
        next_url = next_page.get('href') if next_page else None

        return characters, next_url
    except Exception as e:
        print("Error fetching: " + str(e))
        return [], None

characters_data = []

for game_name, category_url in game_categories:
    print("\nScraping " + game_name + "...")
    page_number = 1
    current_url = category_url

    while current_url:
        print("  Page " + str(page_number) + ": " + current_url)
        characters, next_url = get_characters_from_page(current_url)
        print("  Found " + str(len(characters)) + " characters on this page.")

        for character in characters:
            name = character.get_text(strip=True)
            link = character.get('href')
            if not link or 'Category:' in link:
                continue
            full_url = base_url + link if link.startswith('/') else link
            print("  Scraping: " + name)

            details = get_character_details(full_url)

            entry = {
                "game": game_name,
                "name": name,
                "link": full_url,
                "affiliation": details["affiliation"] if details else None,
                "gender": details["gender"] if details else None,
                "race": details["race"] if details else None,
                "role": details["role"] if details else None,
                "games": details["games"] if details else None,
                "status": details["status"] if details else None
            }
            characters_data.append(entry)
            time.sleep(1)

        current_url = next_url
        page_number = page_number + 1

with open("fallout_characters.csv", "w", newline="") as file:
    writer = csv.DictWriter(file, fieldnames=["game", "name", "link", "affiliation", "gender", "race", "role", "games", "status"])
    writer.writeheader()
    for character in characters_data:
        writer.writerow(character)

print("\nData saved to fallout_characters.csv")
print("Characters scraped: " + str(len(characters_data)))