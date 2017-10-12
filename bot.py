import tweepy, sys, time
import requests
from secrets import *

def tweetToTwitter():
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_key, access_secret)
    api = tweepy.API(auth)
    responeData = requests.get("http://api.icndb.com/jokes/random/?escape=javascript")
    mystatustext = str(responeData.json()['value']['joke'])
    api.update_status(status=mystatustext)


def main():
    print('Yolo from London Artz')
while True:
    tweetToTwitter()
time.sleep(60)  # 1 minute

if __name__ == "__main__":
    main()