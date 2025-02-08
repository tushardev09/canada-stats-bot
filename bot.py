import requests
import os
import tweepy
import xml.etree.ElementTree as ET


# Statistics Canada SDMX API endpoint and parameters
base_url = 'https://www150.statcan.gc.ca/t1/wds/sdmx/statcan/rest/data/DF_17100005/1.1.1'

# Define the parameters for your query (replace with correct parameters)
params = {
    'startPeriod': '2010',
    'endPeriod': '2024',
    'detail': '1'
}

# Fetch data from the Statistics Canada API
response = requests.get(base_url, params=params)

# Check if the request was successful
if response.status_code == 200:
    try:
        # Parse the XML response content
        root = ET.fromstring(response.text)  # Parse XML data
        print("Data fetched successfully.")
        
        # Example: Extract the observation values (you can customize this based on your needs)
        for obs in root.iter('generic:Obs'):
            year = obs.find('generic:ObsDimension').attrib['value']
            value = obs.find('generic:ObsValue').attrib['value']
            print(f"Year: {year}, Value: {value}")
        
    except ET.ParseError as e:
        print(f"Error parsing XML: {e}")
        print("Response content:", response.text)
        exit(1)
else:
    print(f"Error: {response.status_code} - {response.text}")
    exit(1)

 # Fetch data from the Statistics Canada API
# response = requests.get(base_url, params=params)

# Check if the request was successful
#if response.status_code == 200:
 #   data = response.json()  # Parse JSON data
  #  print("Data fetched successfully.")
#else:
 #   print(f"Error: {response.status_code} - {response.text}")
  #  exit(1) /

# Process the data (example, extract specific details to tweet)
# This part needs to be adjusted according to the exact structure of the data
# Here's an example of extracting the population data for a simple tweet
# You will need to modify this to fit the actual API response structure

# For the sake of this example, let's pretend we're extracting population data


# Twitter API credentials (You need to create a Twitter Developer account to get these keys)
API_KEY = os.getenv("API_KEY")
API_SECRET = os.getenv("API_SECRET")
ACCESS_TOKEN = os.getenv("ACCESS_TOKEN")
ACCESS_SECRET = os.getenv("ACCESS_SECRET")



# Authenticate with Twitter using Tweepy
lient = tweepy.OAuth1UserHandler(
  # Use Bearer Token for v2 authentication
    consumer_key=API_KEY,
    consumer_secret=API_SECRET,
    access_token=ACCESS_TOKEN,
    access_token_secret=ACCESS_SECRET
)
auth = tweepy.OAuth1UserHandler

api = tweepy.API(auth)

# Post the tweet with the fetched data
tweet_data = "Hello, world! This is my first tweet from the bot!"
try:
    api.update_status(tweet_data)
    print("Tweet posted successfully!")
except Expectation as e:
    print(f"Error posting tweet: {e}")
