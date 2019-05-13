#!/usr/local/bin/python3

# Writing a simple script to post content to a slack channel for work.
# Not sure yet how to implement this until I do research into how gitlab runners and scheduled jobs work

import time
import datetime
from slackclient import SlackClient


# I know there is an easier way to do this with just time.
# But I think I will need to grab a specific date at a specific time later,
# so I made this script with that in mind.
today = date.today()
t = today.timetuple()
epoch_time = time.mktime(t)


slack_token = os.environ["SLACK_BOT_TOKEN"]
sc = SlackClient(slack_token)

sc.api_call(
  "chat.scheduleMessage",
  channel="CJ9S864SG",
  text="This is a timed message! :):)",
  post_at=epoch_time
)



