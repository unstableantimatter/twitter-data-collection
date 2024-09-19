import os
import tweepy
import sqlite3
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Use the Bearer Token directly from the .env file
BEARER_TOKEN = os.getenv("TWITTER_BEARER_TOKEN")

# Function to authenticate with Twitter API using Bearer Token
def create_twitter_client():
    client = tweepy.Client(bearer_token=BEARER_TOKEN)
    return client

# Database setup function (same as before)
def setup_database():
    conn = sqlite3.connect('twitter_data.db')
    cursor = conn.cursor()

    # Create tables if they do not exist
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS tweets (
        user_id TEXT,
        tweet_text TEXT,
        political_spectrum TEXT,
        location TEXT
    )
    ''')

    conn.commit()
    conn.close()

# Hashtags and corresponding political spectrum categories (same as before)
HASHTAG_CATEGORIES = {
    'Right-leaning': ['#maga', '#donaldtrump', '#trump2024', '#republican'],
    'Central-views': ['#americafirst', '#shoplocal', '#sustainable'],
    'Left-leaning': ['#democrat', '#liberal', '#biden', '#kamala', '#harris']
}

# Function to determine political spectrum based on hashtags (same as before)
def categorize_spectrum(tweet_text):
    tweet_text_lower = tweet_text.lower()  # Normalize the tweet text to lowercase for matching

    for spectrum, hashtags in HASHTAG_CATEGORIES.items():
        if any(hashtag in tweet_text_lower for hashtag in hashtags):
            return spectrum

    return "Unknown"  # Default if no known hashtags are found

# Create or update tweet data in the database (same as before)
def save_tweet_data(user_id, tweet_text, spectrum, location):
    conn = sqlite3.connect('twitter_data.db')
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO tweets (user_id, tweet_text, political_spectrum, location)
        VALUES (?, ?, ?, ?)
    ''', (user_id, tweet_text, spectrum, location))
    conn.commit()
    conn.close()

# Check if tweet mentions a purchase (same as before)
def check_for_purchase(tweet_text):
    purchase_keywords = ["bought", "purchased", "ordered", "shopping"]
    return any(keyword in tweet_text.lower() for keyword in purchase_keywords)

# Extract location from the tweet metadata if available (same as before)
def extract_location(tweet):
    if tweet.geo and 'place_name' in tweet.geo:
        return tweet.geo['place_name']
    return "Unknown"

# Function to collect 25 tweets mentioning shopping/purchasing items with political hashtags
def collect_tweets_with_purchase(client, hashtags):
    total_tweets = 0
    max_results = 100  # Max results per request (Twitter API limit)

    for hashtag in hashtags:
        # Search for recent tweets containing the hashtag
        response = client.search_recent_tweets(query=hashtag, tweet_fields=['author_id', 'text', 'geo'], max_results=max_results)
        
        if not response.data:
            print(f"No tweets found for hashtag: {hashtag}")
            continue

        # Process the response to gather relevant user data
        for tweet in response.data:
            if total_tweets >= 25:  # Limiting to 25 tweets for testing
                break

            tweet_text = tweet.text
            user_id = tweet.author_id
            location = extract_location(tweet)

            # Only process tweets that mention a purchase
            if check_for_purchase(tweet_text):
                # Determine political spectrum based on hashtags in the tweet
                spectrum = categorize_spectrum(tweet_text)

                # Save the full tweet text, political spectrum, and location to the SQLite database
                save_tweet_data(user_id, tweet_text, spectrum, location)

                total_tweets += 1
                print(f"Saved tweet {total_tweets}: {tweet_text}, Location: {location}")

        # Stop if we've collected 25 tweets
        if total_tweets >= 25:
            break

    print(f"Total tweets collected: {total_tweets}")

# Example usage
if __name__ == "__main__":
    # Setup database before collecting tweets
    setup_database()

    # Create Twitter API client using Bearer Token authentication
    twitter_client = create_twitter_client()

    hashtags = ['#maga', '#donaldtrump', '#trump2024', '#republican',
                '#americafirst', '#shoplocal', '#sustainable',
                '#democrat', '#liberal', '#biden', '#kamala', '#harris']

    # Collect 25 tweets mentioning purchases and political hashtags
    collect_tweets_with_purchase(twitter_client, hashtags)

    print("Data collection complete!")
