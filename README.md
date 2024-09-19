# The Polit-shop App - Political Leanings Retail Shopping Recommendation App


### To get started we did some Python Data Scraping and Visualization Exercises

Libraries used:
- sqlite
- pandas
- streamlit
- seaborn
- matplotlib

Original Project Goal:
Create a shopping recommender app that would recommend retail stores to users that aligned with their political affiliation.

Project Sequence So Far
1.  Explored twitter API and scraping program to create a dataset for a specific use case application.
2.  Define database tables that would benefit to create the RAG / model on for the recommender.  -- twitter_scraper.py  
3.  Generated some sample data for the database for preliminary analysis and to move project forward -- generate_mock_data.py -- (wasnt willing to pay $100 for paid twitter API access)
4.  Create a more useful data model for initial analytics -- add_retail.py
5.  Create streamlit visualization app with some basic data analysis based on the updated data model -- db_viz.py

You can view the streamlit here -- https://unstableantimatter-twitter-data-collection-db-viz-nqg6wu.streamlit.app/

This project has a few more big programs to create:
- The RAG -- train the model on our collected data to help with user interactions when we create the shopping recommender app.
- The shopping recommender app -- integrate the RAG model into our shopping recommender app so users can set their preferences, interact with the AI, and get recommendations based on their interactions for local retail stores that they might be looking for.
- Apply deepgram voice interactivity on the application so users can chat with the RAG and it can fine tune the user models with the voice chat.

## This project is probably not going to be developed any further, but if anyone is interested in contributing please reach out !
