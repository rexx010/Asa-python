from unittest.async_case import IsolatedAsyncioTestCase

movies = []

def add_movie(title):
    movies.append([title, 0.0, 0])
    return movies

def movie_rate(title, rate):
    if rate < 1 or rate > 5:
        return "invalid rate input"
    else:
        for movie in movies:
            if movie[0] == title:
                movie[1] += rate
                movie[2] += 1
                return [movie[0], movie[1]]
        return "Movie not found"

def average_rating_for_a_movie(title):
    for movie in movies:
        if movie[0] == title:
            if movie[2] == 0:
                return "No ratings yet"
            average = movie[1] / movie[2]
            return average
    return "Movie not found"

def Average_rating_for_all_movies():
    list_of_movies = []
    for movie in movies:
        list_of_movies.append([movie[0], movie[1]])
    return list_of_movies
    return f"{movie[0]}, {movie[1]}"



