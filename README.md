# Meme API from reddit

### How to use API:

Api Link : https://memeapi26.herokuapp.com/givememe

#### Example Response:
```
{
  "Downvotes": 0,
  "Redditurl": "https://redd.it/eyhdf3",
  "Subreddit": "dankmeme",
  "Title": "When you get jumped by some Chinese kids and they say 嘲笑他",
  "Upvotes": 12,
  "Url": "https://i.redd.it/qyyv797u0te41.jpg"
}
```

### Custom :

#### Custom Count (MAX 50)

Endpoint: https://memeapi26.herokuapp.com/ivememe/<Count>

Example: https://memeapi26.herokuapp.com/givememe/2

Response:
```
{
  "count": 2,
  "memes": [
    {
      "Downvotes": 0,
      "Redditurl": "https://redd.it/eyjcwb",
      "Subreddit": "dankmeme",
      "Title": "Always remember....",
      "Upvotes": 25,
      "Url": "https://i.redd.it/eh3d2tqcqte41.jpg"
    },
    {
      "Downvotes": 0,
      "Redditurl": "https://redd.it/eypiik",
      "Subreddit": "dankmeme",
      "Title": "Everytime she says \"im pregnant\" in a damn novela shit be real 🌋",
      "Upvotes": 6,
      "Url": "https://i.redd.it/nrx0gq6vkwe41.png"
    }
  ]
}
```

#### Custom Subreddit

Endpoint: https://memeapi26.herokuapp.com/givememe/<Subredditname>

Example: https://memeapi26.herokuapp.com/givememe/dankmeme

```
{
  "Downvotes": 0,
  "Redditurl": "https://redd.it/f1r9pz",
  "Subreddit": "dankmeme",
  "Title": "Well can argue with that",
  "Upvotes": 1,
  "Url": "https://i.redd.it/ibyvs9qvz3g41.png"
}
```
#### Custom Subreddit count (MAX 50)

Endpoint: https://memeapi26.herokuapp.com/givememe/<Subredditname>/<count>

Example: https://memeapi26.herokuapp.com/givememe/wholesomeme/2

```
{
  "count": 2,
  "memes": [
    {
      "Downvotes": 0,
      "Redditurl": "https://redd.it/ca0d3r",
      "Subreddit": "wholesomemes",
      "Title": "Probably a repost but I love it. 🥰",
      "Upvotes": 124,
      "Url": "https://i.redd.it/ph1c8s8psr831.jpg"
    },
    {
      "Downvotes": 0,
      "Redditurl": "https://redd.it/dmdis4",
      "Subreddit": "wholesomemes",
      "Title": "Wholesome McDonald's",
      "Upvotes": 110,
      "Url": "https://i.redd.it/zm2qjx3qocu31.jpg"
    }
  ]
}
```
#### Text Subreddit (Eg showerthoughts,quotes)

Endpoint: https://memeapi26.herokuapp.com/givetext/<Subredditname>

Example: https://memeapi26.herokuapp.com/givetext/quotes

```
{
  "Downvotes": 0,
  "Redditurl": "https://redd.it/f374yi",
  "Selftext": "No selftext Present",
  "Subreddit": "quotes",
  "Title": "\"Almost everything will work again if you unplug it for a few minutes, including you.\" - Anne Lamott",
  "Upvotes": 21
}
```
#### Text Subreddit Count(MAX 50)

Endpoint: https://memeapi26.herokuapp.com/givetext/<Subredditname>/<count>

Example: https://memeapi26.herokuapp.com/givetext/showerthoughts/2

```
{
  "count": 2,
  "sub": [
    {
      "Downvotes": 0,
      "Redditurl": "https://redd.it/f3kyt6",
      "Selftext": "No selftext Present",
      "Subreddit": "showerthoughts",
      "Title": "Calling your hair pulled back a “ponytail” makes your head a pony’s ass.",
      "Upvotes": 1227
    },
    {
      "Downvotes": 0,
      "Redditurl": "https://redd.it/f3mp7x",
      "Selftext": "No selftext Present",
      "Subreddit": "showerthoughts",
      "Title": "Pinocchio is a puppet because he was easily manipulated (like how a puppet is controlled by a puppeteer. Only after he learned to think for himself was when he became a real boy.",
      "Upvotes": 19
    }
  ]
}
```