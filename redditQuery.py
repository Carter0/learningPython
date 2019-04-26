#!/usr/local/bin/python3
import praw



reddit = praw.Reddit('Carter', user_agent='My Program')

# Script hits the reddit api endpoint to see which comments have gotten above a certain likes threshold for my user
# Might just use praw cause it makes things really easy with Python

# Might want to split this into a few separate scripts, for sure a few separate functions
# start at bottom, just make a script that looks through each post for comments that have above a certain amount of likes, for now we might just do top level comments, current score to check is 5000
# Then go above that and make a scrip that searches each subreddit for top few posts for the day
# Then make a script that goes through all the subreddits you are subscribed to




# Print all the top level comments that got above the upvote requirment in that submission.
def get_comments(submission, upvote_requirement):
    for top_level_comment in submission.comments:
        if top_level_comment.score >= upvote_requirement:
            print(top_level_comment.body)
            print('------------------------------------------------------')

# Now we are dealing with posts instead of comments
subreddit = reddit.subreddit('AskReddit')
for submission in subreddit.hot(limit=10):
    submission.comments.replace_more(limit=0)
    print(submission.title)
    print(submission.author)
    get_comments(submission, 10000)
    print('===============================================')


#get_comments(submission, 4000)
