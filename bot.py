import tweepy, sys, time
import requests


def tweetToTwitter():
    consumer_key = 'MpoM8pyCYfuoJwMvbYmpr16ad'
    consumer_secret = 'acABkkmipSBxw3dY1JblEpbFp2mB4fnoBsX1mN1fTmFx6zFVh0'
    access_key = '918245280092483586-O2RKRyw9FzIqAmSwOnekBi1WeQR64A4'
    access_secret = 'SADUimBtSsfdtx9huzioIIieSDxvpcpqTUpqkxgsrOxTx'

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