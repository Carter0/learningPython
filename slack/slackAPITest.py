#!/usr/local/bin/python3

import requests
import json
import os
import datetime
from slackclient import SlackClient


# Messing around with the slack api now. Trying to make a simple bot that prints the time.
# This method works well, but it lacks the functionality of other methods.
# Runs with a chron job.
# The cron job I used to test it: */5 * * * * ~/Desktop/learningPython/slackAPITest.py

"""
webhook_url = 'https://hooks.slack.com/services/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'
now = datetime.datetime.now()
time = 'The current time is {}:{}'.format(now.hour, now.minute)
headers = {'content-type': 'application/json'}
payload = {'text': time}
response = requests.post(webhook_url, data=json.dumps(payload), headers=headers)
"""

# I want to now try doing it another way. This way provides a warning about the content-type being wrong. But changing it also provides errors.
# I do not like this method.
"""
url = 'https://slack.com/api/chat.postMessage'
headers = {'Content-type': 'application/json', 'Authorization': '<GET THE TOKEN LATER>'}
data = {'channel': 'CJ9S864SG', 'text': 'It is a warning not an error.'}
response = requests.post(url, data=json.dumps(data), headers=headers)
print(response.text)
"""

# Now lets use the python wrapper
# This is my favorite way to do it.
"""
slack_token = os.environ["SLACK_BOT_TOKEN"]
sc = SlackClient(slack_token)

sc.api_call(
  "chat.postMessage",
  channel="CJ9S864SG",
  text="This is the python wrapper way :)"
)
"""

# Now trying to schedule it
slack_token = os.environ["SLACK_BOT_TOKEN"]
sc = SlackClient(slack_token)

sc.api_call(
  "chat.scheduleMessage",
  channel="CJ9S864SG",
  text="This is a timed message! :):)",
  post_at="1556824221"
)



