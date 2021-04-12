from utils import database


USER_CHOICE = """
Enter
- 'a' to add a movie
- 'l' to list all movies
- 's' to mark a movie as seen
- 'r' to leave a short review of the movie
- 'd' to delete a movie
- 'q' to quit

your choice: 
"""

def menu():
    user_input = input(USER_CHOICE)
    while user_input != 'q':
        if user_input == 'a':
            prompt_add_movie()
        elif user_input =='l':
            list_movies()
        elif user_input =='s':
            prompt_seen_movie()
        elif user_input =='r':
            pass
        elif user_input =='d':
            prompt_delete_movie()
        else:
            print("unknown choice please try again. ")

        user_input = input(USER_CHOICE)



def prompt_add_movie():
    name = input("enter the name of the movie: ")
    director= input("enter the name of the Director: ")
    year = input("enter the year of release: ")
    database.add_movie(name,director,year)


def list_movies():
    for movie in database.list_all_movies():
        seen = 'YES' if movie['seen'] == '1' else 'NO'

        print(f"{movie['name']} by {movie['director']} released in {movie['year']} seen:{seen}")


def prompt_seen_movie():
    name = input('enter the name of the film you have seen: ')
    database.mark_movie_as_seen(name)


def prompt_delete_movie():
    name = input('enter the name of the movie you wish to delete: ')
    database.delete_movie(name)




menu()






