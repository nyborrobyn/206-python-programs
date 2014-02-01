#! /usr/bin/env python

__author__ = 'Robyn Perry'
__email__ = 'robyn@ischool.berkeley.edu'
__python_version = '2.6.1'
__can_anonymously_use_as_example = True


from common import *
#get sentiment_dict from common file
 	
		
def get_tweets(sentiment_dict): 
	import string
	tweet_list = open('tweets.txt','r').readlines()
#Read tweets from file.
	raw_tweets = tweet_list
	new_list = []
	for tweet in tweet_list: 
		tweet = tweet.translate(None, r"!?.-*#\):;<>,\"/").lower()
#Remove punctuation from tweets		
		tweet = tweet.strip('\n').split(' ')
		new_list.append(tweet)
#Split tweets into individual words	after stripping line break character. 	
	for tweet in new_list:	
#Loop through each tweet in list of tweets		
		score = 0
		i = 0
		for word in tweet: 
#Loop through each word of tweet			
			if word in sentiment_dict:
#Check if words in each tweet are in dictionary.  	
				i = i + 1	
#Keep track of how many words get scored in tweet
				score = score + sentiment_dict[word]
#Add to score if word in sentiment dictionary				
		if score != 0:
			score = score/i
			
#Average score over how many words scored in tweet			
			tweet.append(score)
		else: 
			tweet.append(score)
#In either case, append sentiment average to end of tweet			
	i = 0
	for tweet in new_list:
		print 'For the tweet "' + str(raw_tweets[i]) + '" sentiment score is ' + str(tweet[-1])	
	 	i = i + 1
				


def main():
	sentiment_dict = get_sentiments()
	get_tweets(sentiment_dict)
 		
#Controller from which the rest of the code is executed. Final print of recommendations happens here.		 		

		
#Code execution begins here
if __name__ == "__main__":
	main() 		
