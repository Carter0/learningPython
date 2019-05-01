#!/usr/local/bin/python3

import requests
import json
import os

# Messing around with the slack api now. Trying to make a simple bot.
# For now I will just start with posting a message

# You have to retrieve the token as an environment variable, make sure to put it in.
# I want to programmatically find my channel id before I do any of this.
"""
SLACK_BOT_TOKEN = os.environ["SLACK_BOT_TOKEN"]
url = 'https://slack.com/api/chat.postMessage'
headers = {'content-type': 'application/json'}
payload = {'token': SLACK_BOT_TOKEN, 'channel': 'YOUR_CHANNEL_ID', 'text': 'Hello, world'}
response = requests.post(url, data=json.dumps(payload), headers=headers)
"""



