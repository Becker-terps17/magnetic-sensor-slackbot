from slackclient import SlackClient
import RPi.GPIO as GPIO
import time

inputPin = 17
GPIO.setmode(GPIO.BCM)
GPIO.setup(inputPin,GPIO.IN,GPIO.PUD_UP)

# add personal slack token inside ''
slack_token = ''

def door_status():
    if GPIO.input(inputPin) == GPIO.HIGH:
        return True
    else:
        return False

def door_status_string(doorStatus):
    if doorStatus:
        return "Open"
    else:
        return "Closed"

def post_to_slack(to_send):
    sc = SlackClient(slack_token)
    sc.api_call(
        'chat.postMessage',
        channel = "#door-bot",
        text = to_send
    )

if __name__ == "__main__":
    last_status = door_status()
    #post_to_slack("test")
    while True:
    	if last_status != door_status():
    	    post_to_slack("Door status: " + door_status_string(door_status()))
    	    last_status = door_status()
    	    time.sleep(5)
