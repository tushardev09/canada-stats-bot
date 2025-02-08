import tweepy
import random
import os

# Twitter API authentication (retrieved from GitHub Secrets)
API_KEY = os.getenv("API_KEY")
API_SECRET = os.getenv("API_SECRET")
ACCESS_TOKEN = os.getenv("ACCESS_TOKEN")
ACCESS_SECRET = os.getenv("ACCESS_SECRET")
BEARER_TOKEN = os.getenv("ACCESS_BEARER")
# Authenticate with Twitter
auth = tweepy.OAuth1UserHandler(API_KEY, API_SECRET, ACCESS_TOKEN, ACCESS_SECRET)
api = tweepy.API(auth)

# Example tweets (replace with real data fetching logic)
tweets = [
    "Canada’s population is now 40.5 million, growing faster than most G7 nations! 🇨🇦 #CanadaStats",
    "Did you know? 67% of Canada’s electricity came from renewable sources in 2023! ⚡🌱 #CleanEnergy",
    "The Canadian economy grew by 2.3% in 2023! 📈💰 #CDNeconomy #CanadaStats",
]

# Select a random tweet
tweet = random.choice(tweets)

# Post the tweet
api.update_status(tweet)
print(f"Tweet posted: {tweet}")
