"""Capturing tweets which are sent from a location that is approximately the area that is Norwich"""

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
CONSUMER_KEY = 'vbdTbBGv3RzRq77vbUwBIFSJ5'
CONSUMER_SECRET = 'hSYjoSg8Ql7TFrBe5HgjEN4jhsLPwuY32A7ULC6yYOZFSgwbA8'
ACCESS_TOKEN = '261796503-2Ei3eAvL8CL48zasgEeljxdEtj76qMdoitzucIK1'
ACCESS_TOKEN_SECRET = 'CWTK9skZgYn1RYDHbbSoEeODqqdaxLDKu9uBDiPrN9XOQ'

analyser = SentimentIntensityAnalyzer()  # analyses the sentiment of each tweet which is how positive or negative it is,
#  a positive score indicates a positive sentiment and vice versa

# here is the process which captures various elements of the tweet which is then put into a dictionary which is then
#  loaded into MongoDB
lincoln_dict = {}
lincoln_tweets = []

# connection to MongoDB
c = pymongo.MongoClient("mongodb://localhost")
db = c.uber
l_tweets = db.tweets

lincoln_dict['city'] = 'Lincoln'


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
                self.tweet_dict['city'] = 'Lincoln'
                print(self.tweet_dict)
                t = self.tweet_dict
                lincoln_tweets.append(self.tweet_dict)
                lincoln_dict['tweets'] = lincoln_tweets
                l_tweets.insert_one(t)

    def on_error(self, status_code, data):
        print(status_code, data)
        self.disconnect()


stream = MyStreamer(CONSUMER_KEY, CONSUMER_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

stream.statuses.filter(locations='-0.579088, 53.199882, -0.502960, 53.253700')  # this is a location box for Lincoln,
# the first set of coordinates is the southwest box and the second set is the northeast box
