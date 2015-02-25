#list movies whose title contains your first name

import requests #get requests

#get the user's first name
firstname = raw_input("What is your first name? ")

#hit the API.
#use the parameter "s" to search for movies containing your fist name
#use the parameter "type" to tell it you want movies
#otherwise you'll also get TV shows
r = requests.get("http://www.omdbapi.com/?s={0}&type=movie".format(firstname))

#the .json method turns the api response into a python dictionary
movies = r.json()

if "Error" in movies: #check if there was an error
    #check if the error is that the search was empty:
    if movies["Error"] == "Movie not found!":
        print "Sorry, there are no movie titles containing {0}".format(firstname)
    else:
        #then there was another error and we don't know what
        print "There was an unexpected error: {0}. Try again.".format(movies["Error"])
else:
    print "The following movies contain your first name:"
    #the first level of the dictionary is titled "Search".
    #loop through all the movies in the search and print our their titles
    for m in movies["Search"]:
        print "\"{0}\" from {1}".format(m["Title"],m["Year"])

