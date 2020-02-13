# Meme API from reddit

#### How to use API:

Api Link : https://still-river-65459.herokuapp.com/givememe

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

#### Custom :

##### Custom Count (MAX 50)

Endpoint: https://still-river-65459.herokuapp.com/givememe/<Count>

Example: https://still-river-65459.herokuapp.com/givememe/2

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

##### Custom Subreddit

Endpoint: https://still-river-65459.herokuapp.com/givememe/<Subredditname>

Example: https://still-river-65459.herokuapp.com/givememe/dankmeme

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
##### Custom Subreddit count (MAX 50)

Endpoint: https://still-river-65459.herokuapp.com/givememe/<Subredditname>/<count>

Example: https://still-river-65459.herokuapp.com/givememe/wholesomeme/2

```

```