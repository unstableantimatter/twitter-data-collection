import sqlite3
import pandas as pd
import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt

# Connect to the SQLite database
conn = sqlite3.connect('twitter_data.db')

# Load the data into a pandas DataFrame
df = pd.read_sql_query("SELECT * FROM tweets", conn)

# Close the connection
conn.close()

# Split the 'retail_store' column and explode it into individual rows
df['retail_store'] = df['retail_store'].str.split(', ')
df = df.explode('retail_store').reset_index(drop=True)

# 3 Key Insights (These are placeholders, replace with real insights after analyzing data)
st.title("Political Affiliation and Retail Store Preferences Dashboard")
st.subheader("Key Insights")
st.markdown("""
1. **Majority of users from New York and Los Angeles** lean Left-leaning, with significant interest in home decor and beauty stores.
2. **Right-leaning users** are more inclined towards pet care and furniture shopping.
3. **Central-views users** show a balanced distribution across all retail categories, with a notable presence in sustainable shopping.
""")

# Distribution of users across regions (by political affiliation)
st.subheader("Distribution of Users Across Cities and Political Affiliations")
city_political_dist = pd.crosstab(df['location'], df['political_spectrum'])

# Plot using Seaborn
fig, ax = plt.subplots(figsize=(10, 6))
city_political_dist.plot(kind="bar", stacked=True, ax=ax)
plt.title('Political Spectrum Distribution by City')
plt.ylabel('Number of Users')
st.pyplot(fig)

# Distribution of political affiliations across individual retail store categories
st.subheader("Political Affiliations Across Individual Retail Categories")
store_political_dist = pd.crosstab(df['retail_store'], df['political_spectrum'])

# Plot using Seaborn
fig, ax = plt.subplots(figsize=(10, 6))
store_political_dist.plot(kind="bar", stacked=True, ax=ax)
plt.title('Political Spectrum Distribution by Individual Retail Store Category')
plt.ylabel('Number of Users')
st.pyplot(fig)

# Countplot showing the distribution of political affiliations across retail store types
st.subheader("Distribution of Political Affiliations Across Individual Retail Store Types")
fig, ax = plt.subplots(figsize=(10, 6))
sns.countplot(data=df, x='retail_store', hue='political_spectrum', ax=ax)
plt.xticks(rotation=45)
plt.title("Count Plot of Political Affiliations by Individual Retail Store Types")
plt.ylabel("Count")
st.pyplot(fig)

# Summary Statistics
st.subheader("Summary Statistics by Political Spectrum and Retail Store Category")
st.dataframe(df.groupby(['retail_store', 'political_spectrum']).size().unstack().fillna(0))
