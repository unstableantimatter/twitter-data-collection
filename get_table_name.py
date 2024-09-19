import sqlite3

# Connect to the SQLite database
conn = sqlite3.connect('twitter_data.db')

# Query to list all tables in the database
cursor = conn.cursor()
cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
tables = cursor.fetchall()

# Close the connection
conn.close()

# Display the tables
tables
