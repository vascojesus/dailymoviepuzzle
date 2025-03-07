import os
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

last_posted_file = "last_posted.txt"

if not os.path.exists(last_posted_file):
    print("No movie found to tweet.")
    exit()

with open(last_posted_file, "r") as f:
    data = f.read().strip()
    if "," in data:
        day_count, movie_name = data.split(",", 1)
    else:
        print("Invalid data format in last_posted.txt")
        exit()

tweet_text = f"ANSWER DAY {day_count}:\n {movie_name}"
response = client.create_tweet(text=tweet_text, user_auth=True)

print("Answer tweet posted successfully!", response)
