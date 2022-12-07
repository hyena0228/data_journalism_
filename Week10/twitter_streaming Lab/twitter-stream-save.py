import tweepy
import json

consumer_key = ''
consumer_secret = ''
access_token = ''
access_secret = ''

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)

class MyListener(tweepy.StreamListener):

    def on_status(self, data):
        print(data.text + "\n----")

    def on_data(self, data):
        try:
            with open('tweet_stream.json', 'a') as file:
                file.write(data)
                print(data)
                return True
        except BaseException as e:
            print("Error on_data: {}".format(str(e)))
        return True

twitter_stream = tweepy.Stream(auth, MyListener())
twitter_stream.filter(track=['trump', 'clinton'])
