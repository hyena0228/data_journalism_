import json

json_data = []
with open("tweet_stream.json") as file:
    data = file.readlines()
    for d in data:
        json_data.append(json.loads(d))

i = 0
for tweet in json_data:
    if ("text" in tweet) and ("user" in tweet):
        print(str(i) + " - " + tweet["user"]["name"] + " :: " + tweet["text"])
        print("---")
        i = i + 1
