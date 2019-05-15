#!/usr/local/bin/python3
import praw
from praw.models import MoreComments

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

"""
subreddit = reddit.subreddit('sekiro')
posts = [posts for posts in subreddit.top('all', limit=10)]
comments = [comments for comments in posts[0].comments]


# Learning about comment forests!
# They are a list of top level comments with a comment forest of replies.

"
# prints all the top-level-comments in the first post in all time top
# at least it does until eventually I need to reset the comments cause it runs out.
print(posts[0].title)
print('\n')
for comment in comments:
    # One way of dealing with morecomments
    if isinstance(comment, MoreComments):
        continue
    print(comment.body)
"""

# Another way of dealing with more comments, better it seems.

#submission = reddit.submission(url='https://www.reddit.com/r/programming/comments/bh67bz/raycasting_engine_in_factorio_vanilla_017/')
#submission.comments.replace_more(limit=None)
#for top_level_comment in submission.comments:
#     for second_level_comment in top_level_comment.replies:
#        print(second_level_comment.body)

# This will output all the front level comments, then all the second level comments, then all the third etc.
#submission.comments.replace_more(limit=None)
#for comment in submission.comments.list():
#    print(comment.body)

print(reddit.user)

for subreddit in reddit.user.subreddits():
    print(subreddit.title)










