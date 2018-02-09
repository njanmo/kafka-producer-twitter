# uses python3

"""
Created on Mon Oct 09 09:35:34 2017

@author: NayJay

"""

from __future__ import print_function
import json
from kafka import KafkaProducer, KafkaClient
import tweepy
import configparser

# Read the credententials from 'twitter-app-credentials.txt' file
# config = configparser.ConfigParser()
# config.read('twitter-app-credentials.txt')
consumer_key = 'ENTER YOUR CONSUMER KEY HERE'
consumer_secret = 'ENTER YOUR CONSUMER SECRET HERE'
access_key = 'ENTER YOUR ACCESS TOKEN KEY HERE'
access_secret = 'ENTER YOUR ACCESS TOKEN SECRET HERE'

# Words to track
WORDS = ['bitcoin', 'Bitcoin', '#Bitcoin', '#bitcoin', 'BTC', '#BTC', 'btc', '#btc']


class StreamListener(tweepy.StreamListener):
    # This is a class provided by tweepy to access the Twitter Streaming API.

    def on_connect(self):
        # Called initially to connect to the Streaming API
        print("You are now connected to the streaming API.")

    def on_error(self, status_code):
        # On error - if an error occurs, display the error / status code
        print("Error received in kafka producer " + repr(status_code))
        return True # Don't kill the stream

    def on_data(self, data):
        """ This method is called whenever new data arrives from live stream.
        We asynchronously push this data to kafka queue"""
        try:
            producer.send('btc_twitter_stream', data.encode('utf-8'))
        except Exception as e:
            print(e)
            return False
        return True

    def on_timeout(self):
        return True # Don't kill the stream

# Kafka Configuration
producer = KafkaProducer(bootstrap_servers=['localhost:6667'])

# Create Auth object
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_key, access_secret)
api = tweepy.API(auth)

# Set up the listener. The 'wait_on_rate_limit=True' is needed to help with Twitter API rate limiting.
listener = StreamListener(api=tweepy.API(wait_on_rate_limit=True, wait_on_rate_limit_notify=True, timeout=60, retry_delay=5, retry_count=10, retry_errors=set([401, 404, 500, 503])))
stream = tweepy.Stream(auth=auth, listener=listener)
print("Tracking: " + str(WORDS))
stream.filter(track=WORDS, languages = ['en'])
