#author - Yike Chen & Hao Liu

#Content Added
#Chris Pratt, Guardians of the Galaxy, The Lego Movie
#Michael Emerson, Person of Interest, The Dark Knight Returns, Lost

import csv

def create_actors_DB(actor_file):
    '''Create a dictionary keyed on actors from a text file'''
    f = open(actor_file)
    movieInfo = {}
    for line in f:
        line = line.rstrip().lstrip()
        actorAndMovies = line.split(',')
        actor = actorAndMovies[0]
        movies = [x.lstrip().rstrip() for x in actorAndMovies[1:]]    #make a list of an actor's movie
        movieInfo[actor] = set(movies)   #turn the previous list into a set
    f.close()
    return movieInfo

def create_ratings_DB(ratings_file):
    '''make a dictionary from the rotten tomatoes csv file'''
    scores_dict = {}
    with open(ratings_file, 'r') as csvfile:
        reader = csv.reader(csvfile)
        reader.next()
        for row in reader:
            scores_dict[row[0]] = [row[1], row[2]]
    return scores_dict


##def insert_actor_info(actor, movies, movie_Db):
##
##def insert_rating(movie, ratings, ratings_Db):
##
##def delete_moview(movie, movie_Db, ratings_Db):
##
##def select_where_actor_is(actorName, movie_Db):
##
##def select_where_movie_is(movieName, movie_Db):
##
##def select_where_rating_is(targeted_rating, comparison, is_critic,ratings_Db):


def main():
    actor_DB = create_actors_DB('movies.txt')
    ratings_DB = create_ratings_DB('moviescores.csv')
    # PLEASE TAKE THE NEXT FEW PRINTING LINES OUT
    # ONCE YOU HAVE CONFIRMED THIS WORKS
    print actor_DB.keys()
    print ratings_DB.keys()
    print '\n'
    print actor_DB['Humphrey Bogart']
    print ratings_DB['Rambo']
    
if __name__ == '__main__':
    main()
