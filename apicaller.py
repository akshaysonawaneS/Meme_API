from flask import Flask,jsonify
import random,logging
from Main import get_meme, check_image
app = Flask(__name__)
count = 0
randommeme = ['meme','dankmeme','wholesomeme','memes']

@app.route('/')
def welcome():
    return "Welcome To API"

@app.route('/givememe')
def random_meme():              #Random and one
    sub = random.choice(randommeme)
    r = get_meme(sub,100)
    requsted = random.choice(r)

    while not check_image(requsted["Url"]):
        requsted = random.choice(r)

    return jsonify({
        'Title':requsted["Title"],
        'Url': requsted["Url"],
        'Upvotes': requsted["Upvotes"],
        'Downvotes': requsted["Downvotes"],
        'Redditurl': requsted["Redditurl"],
        'Subreddit': requsted["Subreddit"]
    })

@app.route('/givememe/<sub>')
def custom_meme(sub):              #Custom and one
    try:
        r = get_meme(sub,100)

    except:
        return jsonify({
            'Status_code': 404,
            'Message': 'Invalid Subeddit'
        })

    requsted = random.choice(r)

    while not check_image(requsted["Url"]):
        count=count+1
        requsted = random.choice(r)
        if count == 100:
            break

    return jsonify({
        'Title':requsted["Title"],
        'Url': requsted["Url"],
        'Upvotes': requsted["Upvotes"],
        'Downvotes': requsted["Downvotes"],
        'Redditurl': requsted["Redditurl"],
        'Subreddit': requsted["Subreddit"]
    })

@app.route('/givememe/<int:c>')
def multiple(c):
    sub = random.choice(randommeme)

    if c >= 50:
        return jsonify({
            'status_code': 400,
            'message': 'Please ensure the count is less than 50'
        })

    requested = get_meme(sub, 100)

    random.shuffle(requested)

    memes = []
    for post in requested:
        if check_image(post["Url"]) and len(memes) != c:

            t = {
                'Title': post["Title"],
                'Url': post["Url"],
                'Upvotes': post["Upvotes"],
                'Downvotes': post["Downvotes"],
                'Redditurl': post["Redditurl"],
                'Subreddit': post["Subreddit"]
            }
            memes.append(t)


    return jsonify({
        'memes': memes,
        'count': len(memes)
        })


@app.route('/<sub>/<int:c>')
def multiple_from_sub(sub, c):


    if c >= 50:
        return jsonify({
            'status_code': 400,
            'message': 'Please ensure the count is less than 50'
        })

    requested = get_meme(sub, 100)

    random.shuffle(requested)

    memes = []
    for post in requested:
        if check_image(post["Url"]) and len(memes) != c:

            t = {
                'Title': post["Title"],
                'Url': post["Url"],
                'Upvotes': post["Upvotes"],
                'Downvotes': post["Downvotes"],
                'Redditurl': post["Redditurl"],
                'Subreddit': post["Subreddit"]
            }
            memes.append(t)


    return jsonify({
        'memes': memes,
        'count': len(memes)
        })



@app.errorhandler(404)
@app.route('/<lol>')
def not_found(lol):
    return "Are You Lost?"


if __name__ == '__main__':
    app.run()