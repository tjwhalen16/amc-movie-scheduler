def makeSchedule(movies, moviesToSee, numMoviesToWatch):
    return [x for x in movies if x.name in moviesToSee]