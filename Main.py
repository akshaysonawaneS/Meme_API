import praw
import random

randommeme = ['meme','dankmeme','wholesomeme','memes']

reddit = praw.Reddit(client_id='sL-KeSmcQP6U1w',
                     client_secret='oOgusUP9BBgZyhTQPoaIrdXBP3Q',
                     password='akshay@123',
                     user_agent='meme_api',
                     username='meme_api')

def check_image(urllink):


def get_meme(sub,count):
    sub_reddit = reddit.subreddit(sub)
    hot_meme = sub_reddit.hot(limit=count)

    for submissions in hot_meme:
        result = {"Title": submissions.title,
                  "Url": submissions.url,
                  "Upvotes": submissions.ups,
                  "Downvotes": submissions.downs,
                  "Subreddit": submissions.subreddit,
                  "Redditurl": submissions.shortlink
                  }
        print(result)



get_meme('dankmeme',5)

