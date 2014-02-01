#!/usr/bin/env python
#-*- coding: utf-8 -*-

__author__ = 'Robyn Perry'
__email__ = 'robyn@ischool.berkeley.edu'
__python_version = '2.7.2'
__can_anonymously_use_as_example = True


from i206_a6_search_robyn import term_search
from i206_a6_index_robyn import *
from bs4 import BeautifulSoup
from collections import defaultdict
from urllib2 import urlopen
import string
import re


def openUrl(url,verbose=False):

    #url = 'http://courses.ischool.berkeley.edu/i206/f13/a6-sandbox/index.html'
    #taken from AJ's example code
    #gets url and opens it
    response = urlopen(url)

    if verbose:
        print 'URL     :', response.geturl()

    #reads url using BeautifulSoup   
    data = response.read() 
    return data

			

#def crawl(seed, index_dict):
def crawl(seed, on_visit=None):
	#initialize dictionary, list to keep track of links crawled, links to be crawled
	crawled = {seed:1}
	to_crawl = []
	pages_found = [seed]	
	links_found = []
	links_followed = []

	#soupify the seed page & append to list to be crawled
	page = openUrl(seed)
	souped_page = BeautifulSoup(page)
	to_crawl.append(seed)
	
	#keep crawler going as long as there's something to be crawled in to_crawl
	while len(to_crawl) > 0:

		#remove and return first item from to_crawl list
		crawl_link = to_crawl.pop(0)

		#open url and extract HTML from it
		page = openUrl(crawl_link)

		#soupify HTML found at URL
		souped_page = BeautifulSoup(page)

		if on_visit is not None:
			on_visit(souped_page, crawl_link)
		#index_dict = index_words(souped_page, crawl_link, index_dict)

		#find all <a> tags on the page
		for link in souped_page.find_all('a'):

			#iterate through the links on the page & add the absolute path to the link
			full_link = 'http://courses.ischool.berkeley.edu/i206/f13/a6-sandbox/' + link.get('href')

			#count up as link found
			links_found.append(full_link)
			
			#as long as link isn't a key in the dictionary of links that have been crawled, add it as key to dictionary	
			if full_link not in crawled:
			
				#add link as key in dictionary with empty list as value
				crawled[full_link] = 1

				#count pages found, unduplicated	
				pages_found.append(full_link)

				#if the full_link is not in to_crawl list add the link to the list to be crawled	
				if full_link not in to_crawl:

					#add link to list to be crawled
					to_crawl.append(full_link)
					
					#keep track of links followed by appending to list
					links_followed.append(full_link)

			else: 
				#keep track of number of times crawler has come across this link
				crawled[full_link] = crawled[full_link] + 1

	#return all items needed for main function			
	#return links_found, pages_found, crawled, links_followed, index_dict
	return links_found, pages_found, crawled, links_followed		
		

def main():

	#initialize empty dictionary with values constrained to being lists
	index_dict = defaultdict(list)

	#start page url
	seed = 'http://courses.ischool.berkeley.edu/i206/f13/a6-sandbox/index.html'
	
	#open start page
	data = openUrl(seed, verbose=False)
	
	#return results of crawl including links found & followed, pages, what ended up being crawled
	#links_found, pages_found, crawled, links_followed, index_dict = crawl(seed, index_dict)
	links_found, pages_found, crawled, links_followed = crawl(seed, index_words)

	#print results of crawl
	print 'PART I'
	print
	print 'This crawler uses a breadth-first algorithm.'
	print
	print 'Pages found, including the starting page:' 
	print ' %s' % (pages_found)
	print

	#show total number of pages found
	print 'Total number of pages crawled: %s' % str(len(pages_found))
	print
	#total links that it came across
	print 'Total links found: %s' % str(len(links_found))
	print
	#Links followed is pages crawled plus 1, including start page.
	print 'Total links followed: %s' % str(len(links_followed))

	print
	print 'PART II'	
	print "Sorted list of entries in inverted index:"
	
	index_dict = get_index_dict()

	#print alpha sorted terms and the pages they appeared in
	for item in sorted(index_dict.keys()):
		print item , ':', index_dict[item]
		
	print	
	print "Total entries in inverted index: "
	
	#print number of terms in all pages
	print len(sorted(index_dict.keys()))

	print
	print 'PART III'

	#execute function that allows user to search for term
	term_search(index_dict)


#start execution here
if __name__ == '__main__':
	main()
	
