#!/usr/local/bin/python3
import praw

# Script hits the reddit api endpoint to see which comments have gotten above a certain likes threshold for my user

# Print all the top level comments that got above the upvote requirment in that submission.
def get_comments(submission, upvote_requirement):
    for top_level_comment in submission.comments:
        if top_level_comment.score >= upvote_requirement:
            print(top_level_comment.body)
            print('------------------------------------------------------')

# Grab the first 10 posts in the subreddit from hot and print out the comments from them.
def get_submissions(subreddit, upvote_requirement):
    for submission in subreddit.hot(limit=10):
        submission.comments.replace_more(limit=0)
        print(submission.title)
        print(submission.author)
        print('|||||||||||||||||||||||||||||||||||')
        get_comments(submission, upvote_requirement)
        print('===============================================')

# Now we are dealing with all the subreddits I am subscribed to!
def get_subreddits(subreddits, upvote_requirement):
    for subreddit in subreddits:
        print(subreddit.title)
        get_submissions(subreddit, upvote_requirement)

def main():
    reddit = praw.Reddit('Carter', user_agent='My Program')
    temp = ['AskReddit', 'bestof', 'askwomen', 'askmen', 'Showerthoughts', 'changemyview', 'BlackPeopleTwitter']
    subreddits = [reddit.subreddit(subreddit) for subreddit in temp]
    get_subreddits(subreddits, 5000)


if __name__ == '__main__':
    main()
