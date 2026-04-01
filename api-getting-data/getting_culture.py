import json
import requests
import apikey
import os
import pyeuropeana.apis as apis

europeana_api_key = apikey.load("EUROPEANA_API_KEY")
os.environ["EUROPEANA_API_KEY"] = europeana_api_key

url = "https://api.open5e.com/v1/monsters/"

response = requests.get(url)
print(response.status_code)

print(response.json())

url = "https://api.open5e.com/v1/monsters/?type=Dragon&document__slug=wotc-srd"
response = requests.get(url)
print(response.status_code)
print(response.json())

for monster in response.json()["results"]:
    if monster["type"] == "Dragon":
        print(monster)
        break

chosen_monster = response.json()["results"][0]
monster_name = chosen_monster["name"]
monster_type = chosen_monster["type"]

print(f"Chosen monster: {monster_name}")
print(f"Monster type: {monster_type}")

monster_slug = chosen_monster["slug"]
detail_url = f"https://api.open5e.com/v1/monsters/{monster_slug}/"
detail_response = requests.get(detail_url)
print(detail_response.status_code)
print(detail_response.json())

print(f"\nSearching Europeana for '{monster_type}'...")

europeana_response = apis.search(
    query=monster_type,
    qf="TYPE:IMAGE",
    reusability="open",
    media=True,
    thumbnail=True,
    rows=10
)

print(f"Total Europeana results: {europeana_response['totalResults']}")


items = europeana_response.get("items", [])
for item in items:
    print(item)

clean_items = []
for item in items:
    clean_item = {
        "id": item.get("id"),
        "title": item.get("title"),
        "type": item.get("type"),
        "dataProvider": item.get("dataProvider"),
        "country": item.get("country"),
        "rights": item.get("rights"),
        "edmPreview": item.get("edmPreview")
    }
    clean_items.append(clean_item)

output_data = {
    "selected_api": "open5e",
    "open5e_item": {
        "name": chosen_monster.get("name"),
        "type": chosen_monster.get("type"),
        "size": chosen_monster.get("size"),
        "alignment": chosen_monster.get("alignment"),
        "challenge_rating": chosen_monster.get("challenge_rating"),
        "hit_points": chosen_monster.get("hit_points"),
        "armor_class": chosen_monster.get("armor_class")
    },
    "europeana_items": clean_items
}

output_filename = "open5e_europeana_results.json"
with open(output_filename, "w", encoding="utf-8") as f:
    json.dump(output_data, f, indent=4, ensure_ascii=False)

print(f"Saved data to '{output_filename}'")