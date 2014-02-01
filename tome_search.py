#! /usr/bin/env python

__author__ = 'Robyn Perry'
__email__ = 'robyn@ischool.berkeley.edu'
__python_version = '2.6.1'
__can_anonymously_use_as_example = True



from common import *
'''Get sentiment_dict and word_list from common file 
which processes sentiment scores into both a dictionary and a list.'''

import time
#For use with clock functions

#get text corpus into file
def get_corpus(file):
	import string
	corpus = open(file,'r').read()
#Read tweets from file.
	corpus = corpus.translate(None, r"!?.-*#\):;,<>\"/").lower().split(' ')
#Remove punctuation, split into strings for each word.	
	new_corpus = [word.strip('\n') for word in corpus]
#Remove the line break again (somehow it doesn't work on the first go-round). 	
 	return new_corpus		

def dict_lookup(new_corpus, sentiment_dict):
	dict_start = time.clock()
#Find start time when dict_lookup begins	
	for word in new_corpus:
		if word in sentiment_dict:
#Perform lookup comparing word in tome with sentiment dictionary		
			pass
	dict_end = time.clock()
#Find end time after loop completes	
	print 'The dictionary look-up takes ' + str(dict_end - dict_start) + ' seconds.'




def linear_lookup(new_corpus, word_list):
	lin_start = time.clock()
#Find start time when linear_lookup begins	
	
	for word in new_corpus:
		if word in word_list:
#Look up word in tome and compare to list created from lexicon sentiment analysis file.		
			pass
	lin_end = time.clock()
#Find start time when linear_lookup finishes	
	
	print 'The linear look-up takes ' + str(lin_end - lin_start) + ' seconds.'


	
def bin_lookup(new_corpus, word_list):
	bin_start = time.clock()
#Find start time when binary lookup begins	
	
	for word in new_corpus:
		start = 0
		end = len(word_list)-1
#Loop through word in tome; set start and end points of array to look through.
		while start < end:
			mid = (end + start)/2 + 1
#Assign midpoint by adding end/start indices together, dividing by two, which rounds down, and adding 1 to find the real midpoint if it's an odd number.			
			mid_val = word_list[mid]
#Find middle index and set variable to word which occurs at that index.			
			if word == mid_val:
				start = end
#Check if middle word equals word, exit while loop if so. 				
			elif word < mid_val:
				end = mid - 1
#Check if word falls earlier in list than middle value. If so, set new end to mid index (minus 1 because we already know it's not the mid_val from earlier condition).				
			elif word > mid_val:
				start = mid + 1
#Check if word falls later in list. If so, set new start to one after the middle value word.				
	bin_end = time.clock()
#Find end time. 	
 	print 'The binary look-up takes ' + str(bin_end - bin_start) + ' seconds.'

def refactor(corpus_file, corpus_name):
	new_corpus = get_corpus(corpus_file)
	sentiment_dict = get_sentiments()
	word_list = get_sentiment_list()
	print "Here are the lookup numbers for %s in seconds" % corpus_name
	dict_lookup_time = dict_lookup(new_corpus, sentiment_dict)
 	linear_lookup(new_corpus, word_list)	
 	bin_lookup(new_corpus, word_list)
	print

def main():
	refactor('19033-8.txt', 'Alice in Wonderland')
	refactor('135.txt', 'Les Miserables')
	refactor('8800.txt', 'Divine Comedy')
	refactor('shakes.txt', 'the complete works of William Shakespeare')
	refactor('koran.txt', 'Koran')

 	
#Controller from which code is executed. Final print of recommendations happens here.		 		

		
#Code execution begins here
if __name__ == "__main__":
	main() 		
