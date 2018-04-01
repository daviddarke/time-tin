import config
import requests
import datetime

# Get current date and time
now = datetime.datetime.now()

print "GET all of the available tasks:"

# Fire a GET request to pull all of the user's available tasks
r = requests.get(
    "https://app.trackingtime.co/api/v4/users/" + config.TT_CONFIG['userid'] + "/tasks/",
    auth=( config.TT_CONFIG['username'] , config.TT_CONFIG['password'] )
)

# Output a data from the request
print r.status_code
print r.reason
print r.content

print "Now fire a POST request to start tracking a task"

# Fire a POST request to start tracking a task
r = requests.post(
    "https://app.trackingtime.co/api/v4/tasks/track/" + config.TT_CONFIG['taskid'],
    data = {'date' : now.strftime("%Y-%m-%d %H:%M:%S") },
    auth=( config.TT_CONFIG['username'] , config.TT_CONFIG['password'] )
)

# Output a data from the request
print r.status_code
print r.reason
print r.content
