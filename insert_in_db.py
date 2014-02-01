#!/usr/bin/python
# -*- coding: utf-8 -*-

__author__ = 'Robyn Perry'
__email__ = 'robyn@ischool.berkeley.edu'
__python_version = '2.6.0'


import sqlite3 as lite
import sys
import re
from itertools import groupby



def resto_listing(yelpString):
    resto_info_regex = re.compile(r"""
    [0-9]+               #The above regular expressions have been combined with one difference. The '.' special character needs tojump to different lines before matching subsequent expressions
    \.                   #The 're.DOTALL' argument helps '.*' include newlines as well 
    \s\t
    ([a-zA-Z +0-9']+)    #alphanumeric sequences
    .*?
    class="location".*?> #finds tags where class attribute equals location
    ([a-zA-Z \(\)\/]*?)  #groups actual location/neighborhood text
    </a>                 #finds closing a tag   
    .*?                 
    title="([0-9\.]+)    #finds title property with float point rating attribute and grabs just the number
    \s
    star\srating"        #match 'star rating' text
    .*?
    (\([0-9]{3}\)\s[0-9]{3}-[0-9]{4})       #match and group 10 digit phone number
    .*?
    """, re.VERBOSE|re.DOTALL
    )
    
    #find all instances of reg expressions above and return as list of lists
    resto_info = resto_info_regex.findall(yelpString)

    return resto_info


#insert into db
def db_insert(resto_info):       #change to list of tuples to make executemany work
    
    #connect to resto.db
    con = lite.connect('resto.db')
    

    with con:
    
        cur = con.cursor()    
        cur.execute("DROP TABLE IF EXISTS Restos")
        cur.execute("CREATE TABLE Restos(Id INT, Name TEXT, Neighborhood TEXT, Rating INT, Phone TEXT)")
        
        counter = 1
        
        for resto in resto_info:
            cur.execute("INSERT INTO Restos VALUES(%d, ?, ?, ?, ?)" % (counter), resto)
            counter += 1
    return        

        


if __name__ == '__main__':

    #created sqlite3 database before execution of code

    #open yelp listings
    yelpObj = open('yelp_listings.html', 'r')

    #read listings
    yelpString = yelpObj.read()

    #close file
    yelpObj.close()

    #set return value of resto_listing method on yelp listings to be resto dictionary
    resto_info = resto_listing(yelpString)

    #call db_insert which inserts values of dictionary into database
    db_insert(resto_info)
