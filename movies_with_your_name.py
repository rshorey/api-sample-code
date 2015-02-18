import requests #get requests

firstname = "rachel" #put your first name here

#hit the API.
#use the parameter "s" to search for movies containing your fist name
#use the parameter "type" to tell it you want movies
#otherwise you'll also get TV shows
r = requests.get("http://www.omdbapi.com/?s={0}&type=movie".format(firstname))

#the .json method turns the api response into a python dictionary
movies = r.json()

#the first level of the dictionary is titled "Search".
#loop through all the movies in the search and print our their titles
for m in movies["Search"]:
    print "\"{0}\" came out in {1}".format(m["Title"],m["Year"])
