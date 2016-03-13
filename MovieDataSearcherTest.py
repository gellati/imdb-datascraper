#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
from MovieDataSearcher import MovieDataSearcher

class MovieDataSearcherTest(unittest.TestCase):

    def testFormatOutputString(self):
        searcher = MovieDataSearcher()
        testInput = {'title': 'Big',
                     'year': '1988',
                     'ratingValue': '5',
                     'bestRating': '10',
                     'genres': ['Comedy']
        }
        correctResult = "Big (1988)\n5/10\nComedy"
        testResult = searcher.formatOutputString(testInput)
        self.assertEqual(correctResult, testResult)

        
    def testGetMovieLink(self):
        searcher = MovieDataSearcher()
        testTitle = "Big"
        correctResult = "/title/tt0094737/?ref_=fn_al_tt_1"
        testResult = searcher.getMovieLink(testTitle)
        self.assertEqual(correctResult, testResult)

        
    def testGetMovieData(self):
        searcher = MovieDataSearcher()
        testLink1 = "/title/tt0094737/?ref_=fn_al_tt_1" # Big
        testResult1 = searcher.getMovieData(testLink1)
        correctResult1 = {'title': u'Big\xa0',
                         'year': u'1988',
                         'ratingValue': u'7.3',
                         'bestRating': u'10',
                         'genres': [u'Comedy', u'Drama', u'Fantasy']
                         }
        self.assertEqual(correctResult1, testResult1)

        testLink2 = "/title/tt3798324/?ref_=fn_al_tt_1" # Word
        testResult2 = searcher.getMovieData(testLink2)
        correctResult2 = {'title': u'Word\xa0',
                         'year': u'2014',
                         'ratingValue': 'none',
                         'bestRating': 'none',
                         'genres': [u'Comedy']
                         }        
        self.assertEqual(correctResult2, testResult2)        

    def testSearchMovie(self):
        searcher = MovieDataSearcher()
        movieTitle = "the holy mountain"
        movieData = searcher.searchMovie(movieTitle)
        correctResult = (u'The Holy Mountain\xa0 (1973)\n' +
                        u'7.9/10\n' +
                        u'Drama, Fantasy')
        self.assertEqual(correctResult, movieData)
        

if __name__ == '__main__':
    unittest.main()
    
