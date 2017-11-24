
from twython import TwythonStreamer
import time
import json
import vaderSentiment
from datetime import datetime, timedelta
import plotly as py
import plotly.graph_objs as go
from pprint import pprint
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer


CONSUMER_KEY = 'vbdTbBGv3RzRq77vbUwBIFSJ5'
CONSUMER_SECRET = 'hSYjoSg8Ql7TFrBe5HgjEN4jhsLPwuY32A7ULC6yYOZFSgwbA8'
ACCESS_TOKEN = '261796503-2Ei3eAvL8CL48zasgEeljxdEtj76qMdoitzucIK1'
ACCESS_TOKEN_SECRET = 'CWTK9skZgYn1RYDHbbSoEeODqqdaxLDKu9uBDiPrN9XOQ'

analyser = SentimentIntensityAnalyzer()
analyser.polarity_scores('test')

tweets = []


class MyStreamer(TwythonStreamer): # base class is TwythonStreams. Inherits everything that is in TwythonStreamer.
    counter = 0

    def on_success(self, data):
        if data['lang'] == 'en':
            if 'london' or 'dubai' in data['text']:
                MyStreamer.counter += 1
                # tweets.append(data)
                # print('YES - Tweet number {c} hss arrived'.format(c = MyStreamer.counter))
                print('{c} '.format(c = MyStreamer.counter), analyser.polarity_scores((data['text']))['compound'],
                      data['text'])

    def on_error(self, status_code, data):
        print(status_code, data)
        self.disconnect()


stream = MyStreamer(CONSUMER_KEY, CONSUMER_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

timeout = time.time() + 60 # current time + 60 seconds
while True: # until you break
    if time.time() > timeout: # more than 60 seconds
        break # exits the while loop
    stream.statuses.filter(track='lincoln', locations='51.293147, -0.432062 , 51.671336, 0.1790202')

while True: # until you break
    if time.time() > timeout: # more than 60 seconds
        break # exits the while loop
    stream.statuses.filter(track='dubai', locations='51.293147, -0.432062 , 51.671336, 0.1790202')


# tweets[:100]
#
# sentiment_for_times = []
# for t in tweets[1:100]:
#    # td = json.loads(str(t))
#    sentiment_for_times.append(analyser.polarity_scores(t['text'])['compound'])
#    print(analyser.polarity_scores(t['text'])['compound'], t['text'])
#




