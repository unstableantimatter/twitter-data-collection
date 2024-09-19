import sqlite3
import random

# Database setup function
def setup_database():
    conn = sqlite3.connect('twitter_data.db')
    cursor = conn.cursor()

    # Create tweets table if it doesn't exist
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

# Define the political spectrum and associated hashtags
spectrum_data = {
    'Right-leaning': ['#maga', '#donaldtrump', '#trump2024', '#republican'],
    'Central-views': ['#americafirst', '#shoplocal', '#sustainable'],
    'Left-leaning': ['#democrat', '#liberal', '#biden', '#kamala']
}

# List of top 10 US cities by population
cities = [
    'New York', 'Los Angeles', 'Chicago', 'Houston', 'Phoenix',
    'Philadelphia', 'San Antonio', 'San Diego', 'Dallas', 'San Jose'
]

# Function to generate random tweets with hashtags and spectrum
def generate_mock_data():
    records = []
    for _ in range(50):
        # Randomly pick a political spectrum
        spectrum = random.choice(list(spectrum_data.keys()))
        # Randomly pick a hashtag from the selected spectrum
        hashtag = random.choice(spectrum_data[spectrum])
        # Randomly pick a location from the top US cities
        location = random.choice(cities)
        # Generate a random user ID (just a number for simplicity)
        user_id = f'user_{random.randint(1000, 9999)}'
        # Create a sample tweet text
        tweet_text = f"This is a sample tweet about {hashtag}. We believe in making a difference."
        
        # Append the generated record
        records.append((user_id, tweet_text, spectrum, location))
    
    return records

# Function to save the generated data to the SQLite database
def save_mock_data_to_db(records):
    conn = sqlite3.connect('twitter_data.db')
    cursor = conn.cursor()

    # Insert data into the database
    cursor.executemany('''
        INSERT INTO tweets (user_id, tweet_text, political_spectrum, location)
        VALUES (?, ?, ?, ?)
    ''', records)

    conn.commit()
    conn.close()

if __name__ == "__main__":
    # Set up the database and create the table if not present
    setup_database()

    # Generate 50 mock records
    mock_data = generate_mock_data()

    # Save the mock data to the database
    save_mock_data_to_db(mock_data)

    print("50 records have been successfully inserted into the database.")
