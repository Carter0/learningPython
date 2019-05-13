# Writing a script to take the current time and convert it into epoch time.
# Then call the slack api to say hello and goodbye
from datetime import datetime
from datetime import date
import time
from slack import WebClient
import os

def send_message(epoch_time, message, client, channel_id):
    client.chat_scheduleMessage(
    channel=channel_id,
    text=message,
    post_at=epoch_time)

def get_time(hour):
	today = date.today()
	temptime = datetime(today.year, today.month, today.day, hour, 15)
	return time.mktime(temptime.timetuple())

def main():
	slack_token = os.getenv('SLACK_BOT_TOKEN')
	client = WebClient(slack_token, timeout=30)
	data = { get_time(8):'Good Morning Everyone!', get_time(16): 'Have a Good Night Everyone'}
	for time, message in data.items():
		send_message(time, message, client, "CFSG8RUL9")

if __name__ == '__main__':
    main()
