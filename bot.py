import os
import tweepy
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Load Twitter API credentials from .env
API_KEY = os.getenv("API_KEY")
API_SECRET = os.getenv("API_SECRET")
ACCESS_TOKEN = os.getenv("ACCESS_TOKEN")
ACCESS_SECRET = os.getenv("ACCESS_SECRET")
BEARER_TOKEN = os.getenv("BEARER_TOKEN")  # Add your Bearer Token here

# Authenticate using Twitter API v2
client = tweepy.Client(
    bearer_token=BEARER_TOKEN,  # Use Bearer Token for v2 authentication
    consumer_key=API_KEY,
    consumer_secret=API_SECRET,
    access_token=ACCESS_TOKEN,
    access_token_secret=ACCESS_SECRET
)

# Create a tweet
tweet_text = "📊 Canada’s latest population: 40.5M people 🇨🇦 #CanadaStats #PopulationGrowth"

# Post the tweet using v2 (create_tweet method)
response = client.create_tweet(text=tweet_text)

# Print the tweet confirmation
print(f"Successfully posted tweet: {response.data['text']}")
