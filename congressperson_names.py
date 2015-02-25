#for all first names represented in congress,
#how many members have each name?

#you will need a sunlight API key for this.
#to sign up for one, go here: http://sunlightfoundation.com/api/accounts/register/


import requests
import time


#prompt the user for a sunlight foundation API key

api_key = raw_input("What is your sunlight API key? ")

#the base url. We'll insert the API key and the page number later
base_url = "https://congress.api.sunlightfoundation.com/legislators?apikey={0}&per_page=20&page={1}&in_office=true"

#set up a dictionary. The keys will be first names, the values will be counts
firstname_dict = {}

#we need to cycle through a bunch of pages
#because it's going to return 20 legislators at once
page_number = 1
r = requests.get(base_url.format(api_key,page_number)).json()

#when we run out of new pages, r["results"] will be empty,
#so we want to keep going until it is.


while len(r["results"]) > 0:
    print "Got page {0}".format(page_number) #pring which page we're on
    for leg in r["results"]: #loop through all the leg's on this page
        firstname = leg["first_name"] #find the legislator's first name
        if firstname in firstname_dict: #if we've already seen this first name...
            firstname_dict[firstname] += 1 #...add one, because we saw it again!
        else:
            firstname_dict[firstname] = 1 #otherwise we've only seen it once

    #wait 1 second so we don't overwhelm the API
    time.sleep(1)
    #get the next page
    page_number += 1
    r = requests.get(base_url.format(api_key,page_number)).json()


#now print out the results!
#I'd like to print the names in alpbetical order
#but dictionaries aren't sortable! I'll sort the keys instead
#and then find the values I want in the dictionary
sorted_keys = sorted(firstname_dict.keys())
for k in sorted_keys:
    name = k.encode('utf-8') #this deals with unicode. I hate unicode

    #check whether there is only 1, so we can say "legislator" instead of "legislators"
    if firstname_dict[k] == 1:
        print "There is {0} legislator with first name {1}".format(firstname_dict[k],name)
    else:
        print "There are {0} legislators with first name {1}".format(firstname_dict[k],name)


