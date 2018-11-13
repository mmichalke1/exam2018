"""
What is the most interesting/funny/cool thing(s) about Python that you learned from this class or from somewhere else.

You can use code or a short paragraph to illustrate it.
"""

"""The most interesting thing I've learned with Python is how to pull Tweets using twython. I think it's pretty cool 
to be able to pull data from the internet but something like Tweets can be useful since they can be sometimes hard
to find and can give up to date insight on events. I was able to use this for one of our assignments and used it
in sentiment analysis of certain sports teams and players. This data can be useful when trying to see how people
view a certain topic."""


from twython import Twython
def pull_tweets(search, count=1000):
    """Pulls tweets for whatever string is placed inside the function"""
    TOKEN = '250817899-swqJ13ma87ENulvsYkKmgUuCjSj3mslYhLz4BIVM'
    TOKEN_SECRET = 'eRYHOHJuDZGspmXx07HLfIVq3TQWk4zfkutRfBc5DaDms'
    CONSUMER_KEY = 'uvDnCxP8wXu4JkVP6WfBEQBZ6'
    CONSUMER_SECRET = 'nBIpditFHIz86MUEY4ed9DEPX6tv4XfclAJ1cISeOCZsTmfb8F'
    t = Twython(CONSUMER_KEY, CONSUMER_SECRET, TOKEN, TOKEN_SECRET)

    data = t.search(q=search, count=count)

    tweets = ''
    for status in data['statuses']:
        tweets = tweets + status['text']
    return tweets

print(pull_tweets('#Python', count=10))