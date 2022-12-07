from pprint import pprint
import json 

import tweepy

class MyListenerV2(tweepy.StreamingClient): 
    def on_connect(self):
        print("Connected.")
            
    def on_data(self, data):
        try:
            with open('tweet_stream.json','a',encoding='utf-8') as file:
                file.write(data.decode('utf-8'))
                file.write("\n")
                pprint(json.loads(data.decode('utf-8')))
                print("-"*100)
                return True
        except BaseException as e:
            print("Error on_data: {}".format(str(e)))
        return True  

twitter_stream = MyListenerV2("AAAAAAAAAAAAAAAAAAAAADOMjAEAAAAAQyNm0LcAGpMy0beQAyVVSwQP7sY%3DuFae4vhnagYe5vZZx4nUytsyegB7WKACd4yo4PR3RRKRte2k9l")
twitter_stream.add_rules(tweepy.StreamRule("(피원하모니) place_country:KR"))

twitter_stream.filter()

