import unittest
from unittest.mock import patch
import slack
import os
#import pytest
#import mock

# Trying to write unit tests for my slack API Calls
# Here are a few different ways to do it.



# Here is how I would do it with the unittest package
class TestSlack(unittest.TestCase):



    # Set up is a special method used for starting patches in classes
    # Patches just create mocks
    def setUp(self):
        self.patcher1 = patch('os.environ')
        self.patcher2 = patch('slack.WebClient.chat_postMessage')
        self.mock_os = self.patcher1.start()
        self.mock_postMessage = self.patcher2.start()

    # Everything you start you have to stop.
    def tearDown(self):
        self.mock_os.stop()
        self.mock_postMessage.stop()


    def test_slack_success(self):
        self.mock_os.return_value = '5000'
        client = slack.WebClient(token=os.environ['SLACK_API_TOKEN'])

        # This data is data I took from a succesful json post response.
        fake_response = {'ok': True, 'channel': 'CJ9S864SG', 'ts': '1558360638.000100',
        'message': {'type': 'message', 'subtype': 'bot_message', 'text': 'Hello world!', 'ts': '1558360638.000100', 'username': 'testing', 'bot_id': 'BJCSV0UHL'},
        'warning': 'missing_charset',
        'response_metadata': {'warnings': ['missing_charset']}}

        # So, the return value is a special method that specifies this is what the 'fake' class is returning.
        # status code and data are both made up by me. Basically I am making up fields of the fake class.
        self.mock_postMessage.return_value.status_code = 200
        self.mock_postMessage.return_value.data = fake_response


        response = client.chat_postMessage(
            channel='#random',
            text="Hello world!")

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, fake_response)
        self.assertEqual(response.data['message']['text'], 'Hello world!')

    def test_slack_failure(self):
        self.mock_os.return_value = 5000
        client = slack.WebClient(token=os.environ['SLACK_API_TOKEN'])

        fake_response = {'ok': False, 'error': 'channel_not_found',
        'warning': 'missing_charset', 'response_metadata': {'warnings': ['missing_charset']}}

        self.mock_postMessage.return_value = fake_response

        response = client.chat_postMessage(
            channel='#random',
            text="Hello world!")

        assert(response['ok'], 'False')


"""
@patch('os.environ')
@patch('slack.WebClient.chat_postMessage')
def test_slackapi1(mock_postMessage, mock_os):


    mock_os.return_value = '5000'
    client = slack.WebClient(token=os.environ['SLACK_API_TOKEN'])


    mock_postMessage.return_value.status_code = 200
    response = client.chat_postMessage(
        channel='#random',
        text="Hello world!")

    assert mock_postMessage.status_code == 200
"""


