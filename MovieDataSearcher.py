#!/usr/bin/env python
# -*- coding: utf-8 -*-

#import requests
from mechanize import Browser
from bs4 import BeautifulSoup
from lxml import html
import re
import sys

base_url = "http://www.imdb.com"

class MovieDataSearcher:

    def getMovieLink(self, movietitle):

        br = Browser()
        br.set_handle_robots(False)
        br.open(base_url)
        br.select_form(nr=0)
        br.form['q'] = movietitle
        br.submit()
        #    print br.response().read()

        pageData = br.response().read()
        br.close()

        tree = html.fromstring(pageData)
    
        soup = BeautifulSoup(pageData, 'lxml')
        allFindSections = soup.find_all('div', class_='findSection')
        #    print allFindSections[0]
        firstSectionHeader = allFindSections[0].findAll('h3', class_="findSectionHeader")
        #    print firstSectionHeader[0].contents[1] 

#        if (re.match('Title', firstSectionHeader[0].contents[1])):
#            print "title found:"
#            print firstSectionHeader[0].contents[1]
            
        findList = allFindSections[0].findAll('tr', class_='findResult')
        #    print findList[0]
        firstResultLinks = findList[0].findAll('a')
        firstResultLink = firstResultLinks[1].get('href')
            
        allFindTitles = soup.find_all('h3', class_="findSectionHeader")
        return firstResultLink


    def getMovieData(self, link):
        url = base_url + link
        br = Browser()
        br.set_handle_robots(False)

        # some movies do not contain a rating, so initialise with no values
        ratingValue = "none"
        bestRating = "none"

        title = ""
        year = ""
    
        pageData = br.open(url)

        soup = BeautifulSoup(pageData, 'lxml')

        ratingValueElement = soup.find_all('span', itemprop='ratingValue')

        if len(ratingValueElement) > 0:
            ratingValue = ratingValueElement[0].string
                    
        bestRatingElement = soup.find_all('span', itemprop='bestRating')

        if len(bestRatingElement) > 0:
            bestRating = bestRatingElement[0].string
        
        titleHeadingElement = soup.find_all('h1', itemprop='name')
        title = titleHeadingElement[0].contents[0]

        yearElement = soup.find_all('span', id='titleYear')
        yearElementLink = yearElement[0].find_all('a')
        year = yearElementLink[0].contents[0]

        genreElement = soup.find_all('span', class_='itemprop', itemprop='genre')

        genres = []
        for ge in genreElement:
            genres.append(ge.contents[0])
    
        results = {'title' : title,
                   'year' : year,
                   'ratingValue' : ratingValue,
                   'bestRating' : bestRating,
                   'genres' : genres
        }
        br.close()
        return results

    def formatOutputString(self, results):
        outputString = (results['title'] + ' (' + results['year'] + ')' + '\n' +
                       results['ratingValue'] + "/" + results['bestRating'] + '\n' +
                       ', '.join(results['genres']))
        return outputString

    
    def searchMovie(self, title):
        link = self.getMovieLink(title)
        results = self.getMovieData(link)
        outputString = self.formatOutputString(results)
        return outputString

