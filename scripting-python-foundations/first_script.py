favorite_movies =[
    {
        "name": "The Godfather: Part II", "release_year": 1974,
        "sequels": ["The Godfather: Part III"],
        "prequels": ["The Godfather"]
    },
    {
        "name": "A Bronx Tale", "release_year": 1993
    },
    {
        "name": "2001: A Space Odyssey", "release_year": 1968,
        "sequels": ["2010: The Year We Make Contact"]
    },
    {
        "name": "The Deer Hunter", "release_year": 1978
    },
    {
        "name": "American Gangster (film)", "release_year": 2007
    },
    {
        "name": "Star Wars: Episode V","release_year": 1977,
        "sequels": ["Star Wars: Episode VI", "Star Wars: Episode VII", "Star Wars: Episode VIII", "Star Wars: Episode IX"],
        "prequels": ["Star Wars: Episode I", "Star Wars: Episode II", "Star Wars: Episode III", "Star Wars: Episode IV"]
    },
    {
        "name": "The Life Aquatic with Steve Zissou", "release_year": 2004
    },
    {
        "name": "Fantastic Mr. Fox", "release_year": 2009
    },
    {
        "name": "The Lord of the Rings: The Fellowship of the Ring", "release_year": 2001,
        "sequels": ["The Lord of the Rings: The Two Towers","The Lord of the Rings: The Return of the King"],
        "prequels": ["The Hobbit: An Unexpected Journey", "The Hobbit: The Desolation of Smaug", "The Hobbit: The Battle of the Five Armies"]
    },
]

def check_movie(movie):
    if movie["release_year"] < 2000:
        print("This movie was released before 2000")
        return None
    else:
        print("This movie was released after 2000")
        return movie["name"]
    
recent_movies = []

for movie in favorite_movies:
    result = check_movie(movie)
    if result is not None:
        recent_movies.append(result)

print("\n Movies released after 2000:")
print(recent_movies)