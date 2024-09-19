import sqlite3

# Connect to the SQLite database
conn = sqlite3.connect('twitter_data.db')
cursor = conn.cursor()

# Query to select all records
cursor.execute("SELECT * FROM tweets")

# Fetch all records
rows = cursor.fetchall()

# Display the records
for row in rows:
    print(row)

conn.close()
