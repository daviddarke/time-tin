import config
import requests
import datetime
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

GPIO.setup(23, GPIO.IN, pull_up_down=GPIO.PUD_UP) #Button to GPIO23
GPIO.setup(24, GPIO.OUT) #LED to GPIO24

try:
    while True:
        button_state = GPIO.input(23)
        if button_state == False:

            GPIO.output(24, True)
            print('Button Pressed...')

            print "Now fire a POST request to start tracking a task"

            # Get current date and time
            now = datetime.datetime.now()

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

            time.sleep(0.3)

        else:
            GPIO.output(24, False)
except:
    GPIO.cleanup()



# print "GET all of the available tasks:"

# Fire a GET request to pull all of the user's available tasks
# r = requests.get(
#     "https://app.trackingtime.co/api/v4/users/" + config.TT_CONFIG['userid'] + "/tasks/",
#     auth=( config.TT_CONFIG['username'] , config.TT_CONFIG['password'] )
# )
#
# # Output a data from the request
# print r.status_code
# print r.reason
# print r.content
