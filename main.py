import os
import json
import random
import tweepy
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Twitter API credentials
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

auth = tweepy.OAuth1UserHandler(consumer_key, consumer_secret, access_token, access_token_secret)
api = tweepy.API(auth)

images_dir = "images"

date_folders = [os.path.join(images_dir, d) for d in os.listdir(images_dir) if os.path.isdir(os.path.join(images_dir, d))]

random_folder = random.choice(date_folders)

image_files = [os.path.join(random_folder, f) for f in os.listdir(random_folder) if f.lower().endswith(('.png', '.jpg', '.jpeg'))]

random_image = random.choice(image_files)

movie_name = os.path.basename(random_image).rsplit('.', 1)[0].replace('_', ' ')

day_count = int(os.getenv("DAY_COUNT", 1))

media = api.media_upload(filename=random_image)

tweet_text = f"Day {day_count}: 🎬 #DailyMoviePuzzle #Movie #Puzzle"
response = client.create_tweet(text=tweet_text, media_ids=[media.media_id_string], user_auth=True)

print(f"✅ Posted Daily Puzzle Tweet: Day {day_count}")

state_data = {"DAY_COUNT": day_count + 1, "LAST_MOVIE": movie_name}

with open("state.json", "w") as f:
    json.dump(state_data, f)

print(f"✅ Stored LAST_MOVIE in `state.json`: {movie_name}")
