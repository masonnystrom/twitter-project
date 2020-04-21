# web_app/services/twitter_service.py
import tweepy
import os
from dotenv import load_dotenv

load_dotenv()

TWITTER_API_KEY = os.getenv("TWITTER_API_KEY")
TWITTER_API_SECRET = os.getenv("TWITTER_API_SECRET")
TWITTER_ACCESS_TOKEN = os.getenv("TWITTER_ACCESS_TOKEN")
TWITTER_ACCESS_TOKEN_SECRET = os.getenv("TWITTER_ACCESS_TOKEN_SECRET")

def api_client():
    auth = tweepy.OAuthHandler(TWITTER_API_KEY, TWITTER_API_SECRET)
    auth.set_access_token(TWITTER_ACCESS_TOKEN, TWITTER_ACCESS_TOKEN_SECRET)
    print("AUTH", auth) 

    #pass auth object into tweepy
    api = tweepy.API(auth)
    print("API", api)

    return api

if __name__ == "__main__":

    api = api_client()
    