
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


CONSUMER_KEY = 'KFpkYBIUb2FwQflF53ledoMYe'
CONSUMER_SECRET = 'JqlkgGVyj2U6QUFmWLf54kO6j41p6Yg9kBJLxDo2Ixy7hO4l63'
ACCESS_TOKEN = '925717664508645376-h7bsgP10K6lyW0wqaOY7TYgEVlLjBVk'
ACCESS_TOKEN_SECRET = 'Uc7khWeoeJjn15qFr7Lit0LpAeUUTCo84VF1yT73NSLhH'

analyser = SentimentIntensityAnalyzer()
analyser.polarity_scores('test')

norwich_dict = {}
norwich_tweets = []

c = pymongo.MongoClient("mongodb://localhost")
db = c.uber
l_tweets = db.tweets

norwich_dict['city'] = 'Norwich'


class MyStreamer(TwythonStreamer): # base class is TwythonStreams. Inherits everything that is in TwythonStreamer.
    counter = 0

    def on_success(self, data):
        self.tweet_dict = {}
        if data['lang'] == 'en':
            if 'uber' in data['text']:
                MyStreamer.counter += 1

                print('YES - Tweet number {c} hss arrived'.format(c = MyStreamer.counter))
                self.tweet_dict['tweet no'] = '{c} '.format(c = MyStreamer.counter)
                self.tweet_dict['sentiment'] = analyser.polarity_scores((data['text']))['compound']
                self.tweet_dict['text'] = data['text']
                self.tweet_dict['city'] = 'Norwich'
                print(self.tweet_dict)
                t = self.tweet_dict
                norwich_tweets.append(self.tweet_dict)
                norwich_dict['tweets'] = norwich_tweets
                #l_tweets.insert_one(norwich_dict)
                l_tweets.insert_one(t)

    def on_error(self, status_code, data):
        print(status_code, data)
        self.disconnect()


stream = MyStreamer(CONSUMER_KEY, CONSUMER_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

timeout = time.time() + 60 # current time + 60 seconds
while True: # until you break
    if time.time() > timeout: # more than 60 seconds
        break # exits the while loop
    stream.statuses.filter(locations='-5.067775, 50.254185, -5.038774, 50.274355')


# tweets[:100]
#
# sentiment_for_times = []
# for t in tweets[1:100]:
#    # td = json.loads(str(t))
#    sentiment_for_times.append(analyser.polarity_scores(t['text'])['compound'])
#    print(analyser.polarity_scores(t['text'])['compound'], t['text'])
#




