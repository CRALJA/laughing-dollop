"""Capturing tweets which are sent from a location that is approximately the area that is Chelmsford"""

from twython import TwythonStreamer
import time
import json
import vaderSentiment
from datetime import datetime, timedelta
import plotly as py
import plotly.graph_objs as go
from pprint import pprint
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import pymongo

# These keys are supplied from the Twitter
CONSUMER_KEY = 'KFpkYBIUb2FwQflF53ledoMYe'
CONSUMER_SECRET = 'JqlkgGVyj2U6QUFmWLf54kO6j41p6Yg9kBJLxDo2Ixy7hO4l63'
ACCESS_TOKEN = '925717664508645376-h7bsgP10K6lyW0wqaOY7TYgEVlLjBVk'
ACCESS_TOKEN_SECRET = 'Uc7khWeoeJjn15qFr7Lit0LpAeUUTCo84VF1yT73NSLhH'

analyser = SentimentIntensityAnalyzer() # analyses the sentiment of each tweet which is how positive or negative it is,
#  a positive score indicates a positive sentiment and vice versa

# here is the process which captures various elements of the tweet which is then put into a dictionary which is then
#  loaded into MongoDB
chelmsford_dict = {}
chelmsford_tweets = []

# connection to MongoDB
c = pymongo.MongoClient("mongodb://localhost")
db = c.uber
l_tweets = db.tweets

chelmsford_dict['city'] = 'Chelmsford'


class MyStreamer(TwythonStreamer): # base class is TwythonStreams. Inherits everything that is in TwythonStreamer.
    counter = 0

    def on_success(self, data):  # when a tweet is found, it is manipulated as the code shows below
        self.tweet_dict = {}
        if data['lang'] == 'en':
            MyStreamer.counter += 1
            print('YES - Tweet number {c} has arrived'.format(c=MyStreamer.counter))
            if 'uber' in data['text']:
                self.tweet_dict['tweet no'] = '{c} '.format(c = MyStreamer.counter)
                self.tweet_dict['sentiment'] = analyser.polarity_scores((data['text']))['compound']
                self.tweet_dict['text'] = data['text']
                self.tweet_dict['city'] = 'Chelmsford'
                print(self.tweet_dict)
                t = self.tweet_dict
                chelmsford_tweets.append(self.tweet_dict)
                chelmsford_dict['tweets'] = chelmsford_tweets
                l_tweets.insert_one(t)

    def on_error(self, status_code, data):
        print(status_code, data)
        self.disconnect()


stream = MyStreamer(CONSUMER_KEY, CONSUMER_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

stream.statuses.filter(locations='0.437072, 51.716400, 0.505139, 51.758723')  # this is a location box for Chelmsford,
# the first set of coordinates is the southwest box and the second set is the northeast box
