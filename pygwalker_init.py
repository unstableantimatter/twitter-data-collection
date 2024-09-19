import sqlite3
import pandas as pd
import pygwalker as pyg
import webbrowser

# Connect to the SQLite database
conn = sqlite3.connect('twitter_data.db')

# Load the data from the 'tweets' table into a pandas DataFrame
df = pd.read_sql_query("SELECT * FROM tweets", conn)

# Close the connection
conn.close()

# Launch Pygwalker for interactive exploration
pyg.walk(df)

# Open the local Pygwalker server in a browser
# Ensure it opens the Pygwalker session in the browser
url = "http://localhost:5006/pygwalker"  # Default Pygwalker URL
webbrowser.open(url)
