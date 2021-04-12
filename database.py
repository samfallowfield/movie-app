"""
an app to store and rate films that i want to see and rate films i have seen
in csv
"""

movies_file = 'movies.txt'

def create_movie_table():
    with open(movies_file,'a') as file:
        pass


def add_movie(name,director,year):
    with open(movies_file,'a') as file:
        file.write(f"{name},{director},{year},0\n")


def list_all_movies():
    with open(movies_file,'r') as file:
        lines =[line.strip().split(',') for line in file.readlines()]

    return[
        {'name':line[0], 'director':line[1], 'year':line[2],'seen':line[3]}
        for line in lines
    ]



def mark_movie_as_seen(name):
    movies = list_all_movies()
    for movie in movies:
        if movie['name'] == name:
            movie['seen'] =1
    save_all_movies(movies)


def save_all_movies(movies):
    with open(movies_file, 'w') as file:
        for movies in movies:
            file.write(f"{movies['name']}, {movies['director']}, {movies['year']},{movies['seen']}\n")


def delete_movie(name):
    movies = list_all_movies()
    movies =[movie for movie in movies if ['name'] != name ]
    save_all_movies(movies)