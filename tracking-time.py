import config
import requests


r = requests.get( "https://app.trackingtime.co/api/v4/users/ ID /tasks/", auth=( config.DATABASE_CONFIG['username'] , config.DATABASE_CONFIG['password'] ) )


print r.status_code
print r.reason
print r.content
