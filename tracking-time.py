import config
import requests

r = requests.get( "https://app.trackingtime.co/api/v4/users/" + config.TT_CONFIG['userid'] + "/tasks/", auth=( config.TT_CONFIG['username'] , config.TT_CONFIG['password'] ) )

print r.status_code
print r.reason
print r.content
