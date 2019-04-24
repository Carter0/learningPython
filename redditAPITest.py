#!/usr/local/bin/python3
import praw

# Thought I really didnt understand what I was touching with PRAW and that I needed to go over some simple examples, so that is what I am doing.
# Need to set up OAuth 2 certification so I can use reddit API. https://github.com/reddit-archive/reddit/wiki/OAuth2-Quick-Start-Example#first-steps

reddit = praw.Reddit('Carter', user_agent='My Program')

# Prints the top 10 hot submissions from reddit
"""
for submission in reddit.subreddit('learnpython').hot(limit=10):
    print(submission.title)

print('\n')

subreddit = reddit.subreddit('me_irl')
print(subreddit.display_name)
print(subreddit.title)
print(subreddit.description)

print('\n')

for submission in subreddit.hot(limit=1):
    print(submission.title)
    print(submission.score)
    print(submission.id)
    print(submission.url)
"""


subreddit = reddit.subreddit('sekiro')
posts = [posts for posts in subreddit.top('all', limit=10)]
comments = [comments for comments in posts[0].comments]



print(posts[0].title)
print('\n')
for comment in comments:
    print(comment.body)







