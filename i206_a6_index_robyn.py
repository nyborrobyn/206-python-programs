
from bs4 import BeautifulSoup
from urllib2 import urlopen
from collections import defaultdict
import string
import re


__index_dict = defaultdict(list)

def get_index_dict():
	return __index_dict

#def index_words(page, url, index_dict):
def index_words(page, url):
	global __index_dict

	#page already soupified
	html_text = page.body
		
	#turn page text into unicode object without html tags
	body_text = html_text.get_text().lower().split()

	#initialize list for all the words on all the pges
	word_list = []
	
	#remove everything that's not alpha, numeric character or ' character
	for word in body_text: 
		clean_word = re.sub(r"([^A-Za-z0-9'])", '', word)
		
		#if not empty string, append to word list
		if clean_word:
			word_list.append(clean_word)

	#check if url where this word was found has already been captured in values list; if not, add		
	for word in word_list: 
		if url not in __index_dict[word]:
			__index_dict[word].append(url)
	
	#return index_dict
