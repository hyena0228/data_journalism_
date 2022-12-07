import tweepy

consumer_key = ''
consumer_secret = ''
access_token = ''
access_secret = ''

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)

class MyListener(tweepy.StreamListener):

    def on_status(self, data):
        print(data.text + "\n----")

twitter_stream = tweepy.Stream(auth, MyListener())
twitter_stream.filter(track=['trump', 'clinton'])
