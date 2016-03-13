#!/usr/bin/env python
# -*- coding: utf-8 -*-

from MovieDataSearcher import MovieDataSearcher

def getUserInput():
    userInput = ""
    while(userInput == ""):
        try:   # python 2.7
            userInput = raw_input("Enter movie title: ")
        except:  # python 3.0
            userInput = input("Enter movie title: ")    
    return userInput


def printResults(results):
    print results



movieDataSearcher = MovieDataSearcher()

userInput = getUserInput()
results = movieDataSearcher.searchMovie(userInput)
printResults(results)
