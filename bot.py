import tweepy
import os
import sys
from war import War

PATH = os.path.dirname(os.path.abspath(__file__))
IMG_PATH = PATH + '/output.jpg'
CSV_PATH = PATH + '/data/war_data.csv'
ROWS = 6

war = War(CSV_PATH)
message = war.attack()
if message is None:
    sys.exit()
war.save_state()
war.image(IMG_PATH, ROWS)

# Authenticate to Twitter
auth = tweepy.OAuthHandler("API key", "API secret key")
auth.set_access_token("Access token", "Access token secret")

# Create API object
api = tweepy.API(auth)
# Create a tweet
api.update_with_media(IMG_PATH, status=message)