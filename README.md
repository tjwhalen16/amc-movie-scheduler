# amc-movie-scheduler
A python utility that accepts a link to an amc showtimes page and builds a movie schedule with the least amount of downtime in between movies.

# Example run:
`python amc_movie_scheduler.py -l https://www.amctheatres.com/movie-theatres/san-francisco/amc-newpark-12/showtimes/all/2018-09-11/amc-newpark-12/all -m 'The Nun' 'Searching' 'The Meg' 'Peppermint' -n 3`

You'll have to find a newer link, and maybe update the movies after -m flag, because this example is likely out of date.
