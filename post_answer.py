import os
import json
import tweepy
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Twitter API credentials
consumer_key = os.getenv("CONSUMER_KEY")
consumer_secret = os.getenv("CONSUMER_SECRET")
access_token = os.getenv("ACCESS_TOKEN")
access_token_secret = os.getenv("ACCESS_TOKEN_SECRET")

# Initialize Tweepy Client
client = tweepy.Client(
    consumer_key=consumer_key,
    consumer_secret=consumer_secret,
    access_token=access_token,
    access_token_secret=access_token_secret
)

# Load `state.json`
if not os.path.exists("state.json"):
    print("❌ Error: `state.json` not found!")
    exit()

with open("state.json", "r") as f:
    state = json.load(f)

day_count = state["DAY_COUNT"]
movie_name = state["LAST_MOVIE"]

# Post the answer tweet
tweet_text = f"ANSWER DAY {day_count}:\n🎬 {movie_name}"
response = client.create_tweet(text=tweet_text, user_auth=True)

print(f"✅ Answer tweet posted successfully: {movie_name}")
