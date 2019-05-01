#!/usr/local/bin/python3

import requests
import json
import os

# Messing around with the slack api now. Trying to make a simple bot.

SLACK_BOT_TOKEN = os.environ["SLACK_BOT_TOKEN"]


# Need a way to grab the specific info I am looking for
"""
url = 'https://slack.com/api/conversations.list'
params = {'token': SLACK_BOT_TOKEN}
headers = {'content-type': 'application/json'}
response = requests.get(url, params=params, headers=headers)
print(response.text)
"""



webhook_url = 'https://hooks.slack.com/services/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'


# You have to retrieve the token as an environment variable, make sure to put it in.
# Found a good way of doing it with a webhook url set up for this app.
headers = {'content-type': 'application/json'}
payload = {'text': 'Hello, world'}
response = requests.post(webhook_url, data=json.dumps(payload), headers=headers)

print(response)



