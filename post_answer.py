import os
import json
import tweepy
from dotenv import load_dotenv

load_dotenv()

consumer_key = os.getenv("CONSUMER_KEY")
consumer_secret = os.getenv("CONSUMER_SECRET")
access_token = os.getenv("ACCESS_TOKEN")
access_token_secret = os.getenv("ACCESS_TOKEN_SECRET")

client = tweepy.Client(
    consumer_key=consumer_key,
    consumer_secret=consumer_secret,
    access_token=access_token,
    access_token_secret=access_token_secret
)

if not os.path.exists("state.json"):
    print("❌ Error: `state.json` not found!")
    exit()

with open("state.json", "r") as f:
    state_data = json.load(f)

day_count = state_data.get("DAY_COUNT", "Unknown")
movie_name = state_data.get("LAST_MOVIE", "Unknown Movie")

print(f"✅ Retrieved DAY_COUNT: {day_count}")
print(f"✅ Retrieved LAST_MOVIE: {movie_name}")
tweet_text = f"ANSWER DAY {day_count}:\n🎬 {movie_name}"
response = client.create_tweet(text=tweet_text, user_auth=True)

print("✅ Answer tweet posted successfully!", response)
