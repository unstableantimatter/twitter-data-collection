import tweepy
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Twitter API credentials
API_KEY = os.getenv("TWITTER_API_KEY")
API_KEY_SECRET = os.getenv("TWITTER_API_KEY_SECRET")
BEARER_TOKEN = os.getenv("TWITTER_BEARER_TOKEN")

# Set up Tweepy client
client = tweepy.Client(bearer_token=BEARER_TOKEN)

# Test request to verify the API connection
try:
    response = client.search_recent_tweets(query="test", max_results=1)
    if response:
        print("API connection successful!")
    else:
        print("No tweets found, but API connection works.")
except tweepy.errors.TweepyException as e:
    print(f"API connection failed: {e}")
