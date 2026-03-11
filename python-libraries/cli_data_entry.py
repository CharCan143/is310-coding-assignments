from rich.console import Console
from rich.table import Table

console = Console()

example_games = [
    {"Title": "Elden Ring", "Release Year": "2022", "Developer": "FromSoftware", "Genre": "Action RPG"},
    {"Title": "Super Mario Bros", "Release Year": "1985", "Developer": "Nintendo", "Genre": "Platformer"},
    {"Title": "Fallout: New Vegas", "Release Year": "2010", "Developer": "Obsidian Entertainment", "Genre": "Action RPG"},
    {"Title": "Fallout Tactics: Brotherhood of Steel", "Release Year": "2001", "Developer": "Micro Forté", "Genre": "Tactical RPG"},
    {"Title": "Fallout: Brotherhood of Steel", "Release Year": "2004", "Developer": "Interplay Entertainment", "Genre": "Action RPG"},
    {"Title": "Fallout", "Release Year": "1997", "Developer": "Interplay Productions", "Genre": "RPG"},
    {"Title": "Fallout 2", "Release Year": "1998", "Developer": "Black Isle Studios", "Genre": "RPG"},
    {"Title": "Fallout 3", "Release Year": "2008", "Developer": "Bethesda Game Studios", "Genre": "Action RPG"},
    {"Title": "Fallout 4", "Release Year": "2015", "Developer": "Bethesda Game Studios", "Genre": "Action RPG"},
    {"Title": "Fallout 76", "Release Year": "2018", "Developer": "Bethesda Game Studios", "Genre": "Action RPG"},
]

table = Table(title="Favorite Video Games")
table.add_column("Title", style="cyan", no_wrap=True)
table.add_column("Release Year", style="green", justify="center")
table.add_column("Developer", style="yellow")
table.add_column("Genre", style="magenta")

for game in example_games:
    table.add_row(game["Title"], game["Release Year"], game["Developer"], game["Genre"])

console.print(table)

console.print("\n[bold cyan]Now enter your own video games![/bold cyan]")

new_games = []

another = "yes"
while another == "yes" or another == "y":
    console.print("\n[bold cyan]Enter video game details:[/bold cyan]")
    title = input("Title: ")
    release_year = input("Release Year: ")
    developer = input("Developer: ")
    genre = input("Genre: ")

    entry = {"Title": title, "Release Year": release_year, "Developer": developer, "Genre": genre}

    console.print("\n[bold green]You entered:[/bold green]")
    for field, value in entry.items():
        console.print(field + ": " + value)

    confirm = input("\nIs this correct? (yes/no): ").strip().lower()

    if confirm == "yes" or confirm == "y":
        new_games.append(entry)
        console.print("\n[green]Game added![/green]")
    else:
        console.print("[red]Entry not saved. Try again.[/red]")

    another = input("\nWould you like to add another game? (yes/no): ").strip().lower()

console.print("\n[bold magenta]Your submitted games:[/bold magenta]")

new_table = Table(title="New Entries")
new_table.add_column("Title", style="cyan", no_wrap=True)
new_table.add_column("Release Year", style="green", justify="center")
new_table.add_column("Developer", style="yellow")
new_table.add_column("Genre", style="magenta")

for game in new_games:
    new_table.add_row(game["Title"], game["Release Year"], game["Developer"], game["Genre"])

console.print(new_table)

import csv

output_file = open("games.csv", "w", newline="")
writer = csv.DictWriter(output_file, fieldnames=["Title", "Release Year", "Developer", "Genre"])
writer.writeheader()
for game in new_games:
    writer.writerow(game)
output_file.close()

console.print("\n[bold green]Data saved to games.csv![/bold green]")
