#!/usr/bin/env python

__author__ = 'Robyn Perry'
__email__ = 'robyn@ischool.berkeley.edu'
__python_version = '2.6.1'
__can_anonymously_use_as_example = True


import re


file = open("yelp_listings.html", "r")
listings_string = file.read()


def get_input():
    print('''
============================================================
MENU
============================================================
0 - Exit
1 - Question 1:  Restaurant Names
2 - Question 2:  Restaurant Neighborhoods
3 - Question 3:  Restaurant Ratings
4 - Question 4:  Restaurant Telephone Numbers
5 - Question 5:  Neighborhood with the Highest Rating
6 - Question 6:  Extra Credit (Optional)
7 - Show Regular Expressions
    ''')
    command = raw_input('What would you like to do? ')
    return command

def q1():
    global listings_string
    
    #Look for words that follow two spaces after a number. Find every 
    #instance of '#.  Name' immediately following <div id="bizTitleLink#">. 
    #looks like id="bizTitleLink\d+">[0-9]+\.\s*[\dA-Za-z\s*/'"+&;-]*$
    resto_ex = re.compile(r'''
    id="bizTitleLink\d+">         #match div id containing bizTitleLink#
    ([0-9]+\.                    #store the number & period that enumerate resto
    \s*                            #spaces following number
    [\dA-Za-z\s*/'+&;-]*         #Resto name containing alpha-num & other chars.
    $)                              #Stop matching at word boundary or new line.
    ''', re.VERBOSE | re.MULTILINE)
    
    #Find all matches of this regex in listings_string, add to list
    resto_list = resto_ex.findall(listings_string) 
    for resto in resto_list:
        resto = resto.replace('\t', '')
        resto = resto.replace('&amp;', '&')
        print resto    

def q2():
    global listings_string 
    
    #Find substrings matching: id="hood_result_[\d]+_[\d]+">[\dA-Za-z\s*/]* 
    resto_hood = re.compile(r'''
       id="hood_result_            #match id starting with hood_result_
       [\d]+_                        #match 1 or more digits followed by underscore
       [\d]+">                        #match second digits following underscore
       ([\dA-Za-z\s*/]*)            #match and store text optionally including / 
    ''', re.VERBOSE | re.MULTILINE)
    
    #Find all strings that match above regex and put into a list.
    hood_list = resto_hood.findall(listings_string)
    i = 1
    for hood in hood_list: 
        #print results and include number
        print str(i) + ('. ') + str(hood)
        i = i + 1

def q3():
    global listings_string
    
    #Find substrings matching: title="\d\.?\d*\sstar\srating
    resto_rating = re.compile('''
    title="                #match this text
    (\d\.?\d*)            #match digit followed by optional . and digit
    \s                    #match space
    star\srating        #match this text
    ''', re.VERBOSE | re.MULTILINE)
    
    #Find substrings in listings_string that match the regex above.
    rating_list = resto_rating.findall(listings_string)
    e = 1
    for rating in rating_list:
        #print out ratings with number
        print str(e) + ('. ') + str(rating)
        e = e + 1


def q4():
    global listings_string
    
    #Match substrings like this: \(\d{3}\)\s*\d{3}-\d{4}
    resto_phone = re.compile('''
    \(                #match open paren
    \d{3}            #match any combo of 3 digits
    \)                #match closed paren
    \s*                #match space
    \d{3}            #match any combo of 3 digits    
    -                #match hyphen
    \d{4}            #match any combo of 4 digits                        
    ''', re.VERBOSE | re.MULTILINE)
    
    #Add numbers to list
    phone_list = resto_phone.findall(listings_string)
    j = 1
    for phone in phone_list:
        #print out phone numbers, enumerated
        print str(j) + ('. ') + str(phone)        
        j = j + 1

def q5():
    
    global listings_string
    
    #Find substrings matching: title="\d\.?\d*\sstar\srating
    resto_rating = re.compile('''
    title="                #match this text
    (\d\.?\d*)            #match digit followed by optional . and digit
    \s                    #match space
    star\srating        #match this text
    ''', re.VERBOSE | re.MULTILINE)
    
    #Find substrings in listings_string that match the regex above.
    rating_list = resto_rating.findall(listings_string)
    
    
    #Find substrings matching: id="hood_result_[\d]+_[\d]+">[\dA-Za-z\s*/]* 
    resto_hood = re.compile(r'''
       id="hood_result_            #match id starting with hood_result_
       [\d]+_                        #match 1 or more digits followed by underscore
       [\d]+">                        #match second digits following underscore
       ([\dA-Za-z\s*/]*)            #match and store text optionally including / 
    ''', re.VERBOSE | re.MULTILINE)
    
    #Find all strings that match above regex and put into a list.
    hood_list = resto_hood.findall(listings_string)
    
    #Create dictionary and iterate through number of items the length of the rating_list.
    
    hood_rating_dict = {}
    for k in range(len(rating_list)):
    
    #Go through hood_list and check if neighborhood is in dictionary already 
        if hood_list[k] not in hood_rating_dict:
            
            #add to dictionary with value as empty list
            hood_rating_dict[hood_list[k]] = []
        #append ratings for particular neighborhood to value
        hood_rating_dict[hood_list[k]].append(float(rating_list[k]))
    
    #Create dictionary for avg ratings.
    avg_rating = {}
    
    #Iterate through dictionary 
    for key, value in hood_rating_dict.iteritems():
        #Add keys, values to avg_ratings which are n-hood names and avg rating for that n-hood.
        avg_rating[key] = sum(value)/len(value)
    
    #Check which n-hood has max rating using dictionary.    
    max_hood = None    
    for key in avg_rating:
        if max_hood == None:
            max_hood = key
        elif avg_rating[key] >= avg_rating[max_hood]:
            max_hood = key
    print max_hood, avg_rating[max_hood]
                 
    
    
    
def q6():
    #Get string of Yelp ratings.
    global listings_string
    
    print 'Restaurant, Star Rating, Neighborhood, Phone Number'
    print
    
    #Set up reg expressions that match restaurant names, star ratings, n-hoods, phone numbers.
    full_list = re.compile(r'''
     id="bizTitleLink        #match exact text
     \d+                        #match at least one digit
    ">                        #match exact text
    \d+                        #match at least one digit
    \.                        #match a period
    \s*                        #match optional space(s)
    ([\dA-Za-z                #match alphanum combo
    \s*                        #match optional space(s)
    /'"+&;-]*)                #match any of this punctuation optionally, whole term optional
    $                        #match line break or end of word
    |                        #OR
    id="hood_result_        #match id starting with hood_result_
    [\d]+                    #match 1 or more digits
    _[\d]+                    #match underscore followed by 1+ digits
    ">                        #match exact text
    ([\dA-Za-z\s*/]*)        #match & store any alphanum combo w/spaces or slashes
    |                        #OR
    title="                    #match exact text
    (\d                        #store & match 1 digit
    \.?                        #match optional period
    \d*)                    #match 0 or some digits & finish storing
    \s                        #match space
    star\srating            #match text star rating
    |                        #OR
    (\(\d{3}\)                #store & match 3 digits inside parens
    \s*                        #match optional space(s)
    \d{3}-                    #match three digits
    \d{4})                    #match 4 digits & finish storing
    ''', re.VERBOSE | re.MULTILINE)
    
    #Find all strings that match above regex and put into a list.
    resto_list = full_list.findall(listings_string)
    

    #Find elements of returned lists (are they something other than lists?), strip extra chars, remove blank elements, print them. The output format isn't quite right. 
    for e in resto_list:
        for i in e:
            i.strip()
            if i != '':
                print i


def q7():
    print 'Regular Expressions:'
    
    #used escape characters to make this print, but that renders the regex for name incorrect! Note that it works in q1 and is also shown in full form in the comments there.
    print r"name: id=\"bizTitleLink\d+\">[0-9]+\.\s*[\dA-Za-z\s*/'\"+&;-]*$"
    print r'neighborhood: id="hood_result_[\d]+_[\d]+">[\dA-Za-z\s*/]*'
    print r'rating: title="\d\.?\d*\sstar\srating'
    print r'phone: \(\d{3}\)\s*\d{3}-\d{4}'
    print r'extra credit: id=\"bizTitleLink\d+\">[0-9]+\.\s*([\dA-Za-z\s*/\'"+&;-]*$)|id=\"hood_result_[\d]+_[\d]+\">([\dA-Za-z\s*/]*)|title=\"(\d\.?\d*)\sstar\srating|(\(\d{3}\)\s*\d{3}-\d{4})'
    
    
if __name__ == '__main__':

    command = None
    while command != '0':
        #gets input from the user:
        command = get_input()

        #depending on the item selected, call the corresponding function:
        if command == '0':
            exit()
        elif command == '1': q1()
        elif command == '2': q2()
        elif command == '3': q3()
        elif command == '4': q4()
        elif command == '5': q5()
        elif command == '6': q6()
        elif command == '7': q7()
        else: print('"{}" is an invalid command.'.format(command))

        raw_input('\nPress enter to continue...')
