import praw


reddit = praw.Reddit(client_id='sL-KeSmcQP6U1w',
                     client_secret='oOgusUP9BBgZyhTQPoaIrdXBP3Q',
                     password='akshay@123',
                     user_agent='meme_api',
                     username='meme_api')

def check_image(urllink):
    ext = urllink[-4:]
    if ext == '.jpg' or ext == '.png':
        return True

    return False


def get_meme(sub,count):
    sub_reddit = reddit.subreddit(sub)
    hot_meme = sub_reddit.hot(limit=count)
    result =[]
    for submissions in hot_meme:
        temp = {"Title": submissions.title,
                  "Url": submissions.url,
                  "Upvotes": submissions.ups,
                  "Downvotes": submissions.downs,
                  "Redditurl": submissions.shortlink,
                  "Subreddit": sub
                  }
        result.append(temp)

    return result

def get_text(sub,count):
    sub_reddit = reddit.subreddit(sub)
    hot_meme = sub_reddit.hot(limit=count)
    result=[]
    for submission in hot_meme:
        temp = {"Title": submission.title,
                "Selftext": submission.selftext
                "Upvotes": submission.ups,
                "Downvotes": submission.downs,
                "Redditurl": submission.shortlink,
                "Subreddit": sub
                }
        result.append(temp)


    return result

