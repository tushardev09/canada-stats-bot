import os
import requests
import random
from dotenv import load_dotenv
import tweepy

# Load environment variables
load_dotenv()

# Set up your Tweepy client
client = tweepy.Client(
    bearer_token=os.getenv("BEARER_TOKEN"),
    consumer_key=os.getenv("API_KEY"),
    consumer_secret=os.getenv("API_SECRET"),
    access_token=os.getenv("ACCESS_TOKEN"),
    access_token_secret=os.getenv("ACCESS_SECRET"),
)

# Define a function to fetch data from Statistics Canada API
def fetch_canada_stats():
    # API endpoint for Statistics Canada (replace with the actual endpoint you're using)
    url = "https://www150.statcan.gc.ca/t1/wds/rest/getData"
    
    # Example query parameters (you need to replace with real parameters based on the API you are using)
    params = {
        'product': '14-10-0023',  # This is an example. Replace with actual product code
        'language': 'en'
    }
    
    # Fetch the data from the API
    response = requests.get(url, params=params)
    
    # Handle the response
    if response.status_code == 200:
        data = response.json()  # Assuming the response is in JSON format
        
        # Extract the relevant data
        # (This depends on the specific API, so adjust this part based on the API response structure)
        population_data = data.get("data", {}).get("population", "No data available")
        
        # Create tweet text
        tweet_text = f"📊 Canada's population in 2024: {population_data} people 🇨🇦 #CanadaStats #PopulationGrowth"
        
        return tweet_text
    else:
        return "Sorry, could not retrieve the data. Please try again later."

# Fetch the data
tweet_text = fetch_canada_stats()

# Post the tweet
response = client.create_tweet(text=tweet_text)

# Print the tweet confirmation
print(f"Successfully posted tweet: {response.data['text']}")


