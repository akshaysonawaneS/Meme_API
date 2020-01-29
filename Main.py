import praw
import random

randommeme = ['meme','dankmeme','wholesomeme','memes']

reddit = praw.Reddit(client_id='sL-KeSmcQP6U1w',
                     client_secret='oOgusUP9BBgZyhTQPoaIrdXBP3Q',
                     password='akshay@123',
                     user_agent='meme_api',
                     username='meme_api')

def random_meme():
    sub = random.choice(randommeme)
    sub_reddit = reddit.subreddit(sub)
    hot_meme = sub_reddit.hot(limit=100)

    for submissions in hot_meme:
        print(submissions.title)

    return True

def get_meme(sub):
    sub_reddit = reddit.subreddit(sub)
    hot_meme = sub_reddit.hot(limit=100)

    for submissions in hot_meme:
        print(submissions.title)

get_meme('memes')

