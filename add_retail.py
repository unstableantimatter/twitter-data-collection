import sqlite3
import random

# Define the retail store options
retail_store_options = [
    'boutiques', 'clothing', 'furniture', 'pet care', 'home decor', 'beauty', 'drug store'
]

# Connect to the database
conn = sqlite3.connect('twitter_data.db')
cursor = conn.cursor()

# Step 1: Add the new column `retail_store` (if it doesn't already exist)
# Note: SQLite doesn't support `ALTER TABLE ADD COLUMN IF NOT EXISTS`, so we manually check if the column exists
cursor.execute("PRAGMA table_info(tweets);")
columns = [info[1] for info in cursor.fetchall()]
if 'retail_store' not in columns:
    cursor.execute("ALTER TABLE tweets ADD COLUMN retail_store TEXT;")
    print("Added 'retail_store' column.")

# Step 2: Generate random retail stores for each record
cursor.execute("SELECT rowid, * FROM tweets")
records = cursor.fetchall()

# Randomly assign 1 or 2 store types to each tweet
for record in records:
    rowid = record[0]
    # Randomly choose 1 or 2 retail store options
    selected_stores = random.sample(retail_store_options, random.randint(1, 2))
    retail_store = ', '.join(selected_stores)  # Combine selected stores as a comma-separated string
    
    # Update the record with the randomly selected store(s)
    cursor.execute("UPDATE tweets SET retail_store = ? WHERE rowid = ?", (retail_store, rowid))

# Commit the changes and close the connection
conn.commit()
conn.close()

print("Successfully updated the 'retail_store' column with random values.")
