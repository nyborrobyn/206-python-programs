__sentiment_dict = None

def get_sentiments():
	global __sentiment_dict
	if __sentiment_dict is not None:
		return __sentiment_dict
		
	__sentiment_dict = {}
	sentiment_list = [entry.strip().split("\t") for entry in open('sentiment-calc.txt', 'r').readlines()]	
#Read document into list of lists, strip extra chars and split at tab marker. 
	
	for element in sentiment_list: 
		element[1] = float(element[1])
#Make second element of all inner lists float so that we can average them. 		
	
	for sentiment in sentiment_list:
		__sentiment_dict[sentiment[0]] = sentiment[1]
#Add each list to dictionary, first element key, second value. 			
	
	return __sentiment_dict	 
	
	
	
def get_sentiment_list():
	sentiment_words = [entry.strip().split("\t") for entry in open('sentiment-calc.txt', 'r').readlines()]	
	word_list = []
	for e in sentiment_words:
		word_list.append(e[0])
	return word_list
#Make sentiments into list of words	
