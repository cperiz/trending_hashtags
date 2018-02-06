from __future__ import absolute_import, print_function

from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
import json
import time
import os
from lib.hash_counter import HashProcessor
from lib.async_sender import Sender

"""
#: Downloads tweets from the geobox area (set in bounding box).
#: Finds most common hashtags.
#: Uses rabbitMQ to asynchronously message a program that
#: downloads news urls for these hashtags or prints a histogram of hashtags.
"""
"""
# ----- Bounding boxes for geolocations ------#
## Online-Tool to create boxes (c+p as raw CSV): http://boundingbox.klokantech.com/
#GEOBOX_WORLD = [-180,-90,180,90]
#GEOBOX_GERMANY = [5.0770049095, 47.2982950435, 15.0403900146, 54.9039819757]
#stream.filter(locations=GEOBOX_GERMANY)
#---------------------------------------------#
"""

consumer_key = os.environ['consumer_key']
consumer_secret = os.environ['consumer_secret']
access_token = os.environ['access_token']
access_token_secret = os.environ['access_token_secret']

class StdOutListener(StreamListener):
    """ A listener handles tweets that are received from the stream.
    This is a listener that counts hashtags and communicates with OAuthHandler
    programs via asynchronous messaging.
    """
    def __init__(self, t_start, t_silent, *args, **kwargs):
        super(StdOutListener, self).__init__(*args, **kwargs)
        self.hash_processor = HashProcessor()
        self.sender = Sender()
        self.t_start = t_start
        self.t_silent = t_silent
        self.c = 1

    def on_data(self, tweet):
        tweet = json.loads(tweet)

        self.hash_processor.process(tweet)
        if time.time()-self.t_start > self.c*t_silent:
            self.c += 1
            print()
            print("time: ", time.time()-self.t_start)
            topX = self.hash_processor.get_topX_counts(10)
            print(topX)
            #: send to exchange to download
            #self.sender.send_msg(msg=",".join([i[0] for i in topX]))
            #: send to exchange to plot
            self.sender.send_msg(msg="|||".join([i[0] + "|::|" + str(i[1]) for i in topX]))
        return True

    def on_error(self, status):
        print(status)

if __name__ == '__main__':

    t_start = time.time()
    t_silent = 5 # seconds

    l = StdOutListener(t_start, t_silent)
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)

    stream = Stream(auth, l)
    GEOBOX_MA = [-73.7990632216,41.90293316,-70.2467151391,42.9610385979]
    #GEOBOX_CA = [-124.5984090405,32.5791974819,-116.648756203,43.1737269492]
    stream.filter(locations=GEOBOX_MA)
