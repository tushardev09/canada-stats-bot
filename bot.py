import requests
import os
import tweepy
import json

# Statistics Canada SDMX API endpoint and parameters
base_url = "https://www150.statcan.gc.ca/t1/wds/sdmx/statcan/rest/data/DF_17100005/1.1.1"  # Adjust URL based on the dataset you need
params = {
    'startPeriod': '2010',  # Start period for data
    'endPeriod': '2020',    # End period for data
    'detail': 'full'        # Set to 'full' for detailed data
}

# Fetch data from the Statistics Canada API
response = requests.get(base_url, params=params)

# Check if the request was successful
if response.status_code == 200:
    data = response.json()  # Parse JSON data
    print("Data fetched successfully.")
else:
    print(f"Error: {response.status_code} - {response.text}")
    exit(1)

# Process the data (example, extract specific details to tweet)
# This part needs to be adjusted according to the exact structure of the data
# Here's an example of extracting the population data for a simple tweet
# You will need to modify this to fit the actual API response structure

# For the sake of this example, let's pretend we're extracting population data
tweet_data = "Population estimate for Canada from 2010 to 2020:\n"
try:
    # Example: Extract relevant data from the response
    # This part will depend on the actual structure of your response.
    # Replace with the actual data extraction logic.
    dataset = data.get('dataSets', [])
    if dataset:
        # For example, let's take the first dataset's first series
        series = dataset[0].get('series', {})
        for key, value in series.items():
            # Customize this part to format your data correctly
            population_value = value.get('value', 'N/A')  # Adjust key according to response structure
            tweet_data += f"Year: {key}, Population: {population_value}\n"
except Exception as e:
    print(f"Error processing data: {e}")
    exit(1)

# Twitter API credentials (You need to create a Twitter Developer account to get these keys)
API_KEY = os.getenv("API_KEY")
API_SECRET = os.getenv("API_SECRET")
ACCESS_TOKEN = os.getenv("ACCESS_TOKEN")
ACCESS_SECRET = os.getenv("ACCESS_SECRET")
BEARER_TOKEN = os.getenv("BEARER_TOKEN")


# Authenticate with Twitter using Tweepy
lient = tweepy.Client(
    bearer_token=BEARER_TOKEN,  # Use Bearer Token for v2 authentication
    consumer_key=API_KEY,
    consumer_secret=API_SECRET,
    access_token=ACCESS_TOKEN,
    access_token_secret=ACCESS_SECRET
)

api = tweepy.API(auth)

# Post the tweet with the fetched data
try:
    api.update_status(tweet_data)
    print("Tweet posted successfully!")
except tweepy.TweepError as e:
    print(f"Error posting tweet: {e}")
