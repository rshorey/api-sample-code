import requests
import datetime #to convert dates to day of week

#paste the username of the repo you care about here:
git_username = "rshorey"
#and put the reponame here
git_reponame = "api-sample-code"

#put together the url
url = "https://api.github.com/repos/{0}/{1}/commits".format(git_username,git_reponame)

#get the data!
r = requests.get(url)

#turn the data into a python dictionary
commits = r.json()


#dictionary of numbers to days of the week, we'll use to convert later
num_to_weekday = {0:"Monday",
                    1:"Tuesday",
                    2:"Wednesday",
                    3:"Thursday",
                    4:"Friday",
                    5:"Saturday",
                    6:"Sunday"}

commit_dict = {} #empty dictionary to throw our results in

for commit in commits: #loop through commits
    date = commit["commit"]["committer"]["date"] #find the the commit date in the data

    #converts the date to python's internal representation
    date = datetime.datetime.strptime(date,"%Y-%m-%dT%H:%M:%SZ")
    
    #finds the day of the week where 0 is monday and 6 is sunday
    day_as_num = datetime.datetime.weekday(date)

    day_of_week = num_to_weekday[day_as_num] #converts number to day name
    
    if day_of_week in commit_dict:
        commit_dict[day_of_week] += 1
    else:
        commit_dict[day_of_week] = 1


#find the day of the week with the most commits
if len(commit_dict) == 0:
  print "This repo doesn't seem to have any commits"

else:

    #the maximum function has a special way to let find the
    #dictionary key with the largest value! I just learned this
    #from stack overflow:
    #http://stackoverflow.com/questions/14091636/get-dict-key-by-max-value
    #Cool! We use it here:
    max_commit_day = max(commit_dict, key=commit_dict.get)

    #there's actually a problem here: if multiple days
    #tie for the same number of commits, we'll
    #just spit out one arbitrarily.
    #fixing this is outside the scope of this problem, sorry

    #but it's a fun exercise if you're bored!!!


    print "Committers to {0} are most productive on {1}".format(git_reponame, max_commit_day)