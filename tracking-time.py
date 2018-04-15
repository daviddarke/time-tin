#!/usr/bin/python
import config
import requests
import datetime
import RPi.GPIO as GPIO
import time
import Adafruit_CharLCD as LCD

# Raspberry Pi pin configuration:
lcd_rs        = 26  # Note this might need to be changed to 21 for older revision Pi's.
lcd_en        = 19
lcd_d4        = 13
lcd_d5        = 6
lcd_d6        = 5
lcd_d7        = 11
lcd_backlight = 4

# Define LCD column and row size for 16x2 LCD.
lcd_columns = 16
lcd_rows    = 2

# Alternatively specify a 20x4 LCD.
# lcd_columns = 20
# lcd_rows    = 4

# Initialize the LCD using the pins above.
lcd = LCD.Adafruit_CharLCD(lcd_rs, lcd_en, lcd_d4, lcd_d5, lcd_d6, lcd_d7,
                           lcd_columns, lcd_rows, lcd_backlight)

# Print a two line message
lcd.message('Hello World!')


# GPIO.setmode(GPIO.BCM)
#
# GPIO.setup(23, GPIO.IN, pull_up_down=GPIO.PUD_UP) #Button to GPIO23
# GPIO.setup(24, GPIO.OUT) #LED to GPIO24
#
# try:
#     while True:
#         button_state = GPIO.input(23)
#         if button_state == False:
#
#             GPIO.output(24, True)
#             print('Button Pressed...')
#
#             print "Now fire a POST request to start tracking a task"
#
#             # Get current date and time
#             now = datetime.datetime.now()
#
#             # Fire a POST request to start tracking a task
#             r = requests.post(
#                 "https://app.trackingtime.co/api/v4/tasks/track/" + config.TT_CONFIG['taskid'],
#                 data = {'date' : now.strftime("%Y-%m-%d %H:%M:%S") },
#                 auth=( config.TT_CONFIG['username'] , config.TT_CONFIG['password'] )
#             )
#
#             # Output a data from the request
#             print r.status_code
#             print r.reason
#             print r.content
#
#             time.sleep(0.3)
#
#         else:
#             GPIO.output(24, False)
# except:
#     GPIO.cleanup()



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
