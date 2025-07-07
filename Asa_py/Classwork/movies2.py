new_list_of_movie = []
movies = []
counter = []

def add_movie(title):
    movies.append([title, 0, 0])
    return movies

def movie_rate(title,rate):
    for movie in movies:
        if movie[0] == title:
            movie[1] += rate
            movie[2] += 1
            return f"{movie[0]}, {movie[1]}"
    return None

def average_rating_for_a_movie(title):
    for movie in movies:
        if movie[0] == title:
            movie[2] = movie[1] / movie[2]
            return movie[2]

def Average_rating_for_all_movies():
    #print(movies)
    for movie in movies:
        new_list_of_movie .append(movie)
    return new_list_of_movie
    return f"{movie[0]}, {movie[1]}"



if __name__ == '__main__':
    print(add_movie("Lagbaja"))
    print(add_movie("Def"))
    print(add_movie("scqi"))
    print(movie_rate("Def",4))
    print(average_rating_for_a_movie("Def"))
    print(Average_rating_for_all_movies())