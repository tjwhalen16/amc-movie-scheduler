def makeSchedule(movies, moviesToSee, numMoviesToWatch):
    return { name: movies[name] for name in moviesToSee }