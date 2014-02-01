import webbrowser 


def term_search(dictionary):
	
	#take user input of a single term & turn into string
	select_term = str(raw_input("Enter up to 4 search terms separated by commas (i.e. thing1, thing2, thing3, thing4): ")).lower()

	#split terms at comma followed by a space and put into list
	term_list = select_term.split(', ')

	if len(term_list) < 5:
	
		#create new html file or overwrite file if it already exists
		results_file = open("new.html", "w+")

		#create most of tags for html doc
		start_html = '<!DOCTYPE html><html><header><title>Search Results</title></header><body><h1>Search Results</h1>'

		#write opening tags for html document up to body
		results_file.write(start_html)

		#iterate through terms entered by user	
		for term in term_list:

			#match against keys in dictionary
			if term in dictionary: 

				#print the search term in html in p tags
				term_html = '<p> The term "%s" appears on the following page(s): </p><br>' % term

				#print the term in the html document in p tags
				results_file.write(term_html)

				#if key in dictionary, write the pages where it is found to an html page
				for value in dictionary[term]:
					

					#create html a tag that includes link
					a_tag = '<a href="%s">%s</a><br>' % (value, value)

					#write the a tag including the link to the results file
					results_file.write(a_tag)
			
			

			else:

				#create string for invalid entry
				no_result_text = '<p>This search term or terms you entered is not on the pages crawled. <br>Return to the command line to try entering different terms.</p>'

				#write negative text to html	
				results_file.write(no_result_text)
		
			#write closing tags into document after all a tags print	
			results_file.write('</body></html>')

			#open written file in web browser
			webbrowser.open("file:///Users/robynperry/Dropbox/MIMS/Fall2013/206/a6/new.html")		
	


	else: 

		#give user another chance to enter in terms
		print 'Oops, please enter 4 terms or fewer!'
		term_search(dictionary)	

