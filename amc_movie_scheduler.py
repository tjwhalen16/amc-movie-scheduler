import argparse
import amc_web_parser
import movie_schedule_algorithm

def main():
    args = getArgs()
    print(args['link'])
    print(args['movies'])
    print(args['numMoviesToSee'])
    moviesToSee = args['movies']
    numMoviesToSee = args['numMoviesToSee']
    movies = amc_web_parser.parseMoviesFromURL(args['link'])
    movies = movie_schedule_algorithm.makeSchedule(movies, moviesToSee, numMoviesToSee)
    printMovies(movies)
    
def getArgs():
    parser = argparse.ArgumentParser()
    parser.add_argument('-l', '--link', required=True)
    parser.add_argument('-m', '--movies', nargs='+', required=True)
    parser.add_argument('-n', '--numMoviesToSee', required=True)
    args = vars(parser.parse_args())
    return {'link' : args['link'], 'movies' : args['movies'], 'numMoviesToSee' : args['numMoviesToSee']}

def printMovies(movies):
    for movie in movies:
        movie.print()
        print('\n-----------------------')

main()