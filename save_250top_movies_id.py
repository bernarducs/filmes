'''
Retrieve the 250 top movies using this lib was just possible
refactoring the imdb/parser/http/topBottomParser.py file. See more in:

https://github.com/cinemagoer/cinemagoer/compare/master...DennisNemec:cinemagoer:fix-parse-top-250-movies

'''

from imdb import Cinemagoer

ia = Cinemagoer()
tops = ia.get_top250_movies()

with open('top250moviesID.txt', 'w', encoding='utf-8') as f:
    for top in tops:
        f.write(top.movieID[:2])
