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

# Initialize Tweepy Client
client = tweepy.Client(
    consumer_key=consumer_key,
    consumer_secret=consumer_secret,
    access_token=access_token,
    access_token_secret=access_token_secret
)

# Initialize Tweepy API for media upload
auth = tweepy.OAuth1UserHandler(consumer_key, consumer_secret, access_token, access_token_secret)
api = tweepy.API(auth)

# Check if state.json exists
if os.path.exists("state.json"):
    with open("state.json", "r") as f:
        state = json.load(f)
    day_count = state["DAY_COUNT"] + 1
else:
    day_count = 1  # First run

# Path to images
images_dir = "images"

# Get all subdirectories (dates)
date_folders = [os.path.join(images_dir, d) for d in os.listdir(images_dir) if os.path.isdir(os.path.join(images_dir, d))]

# Choose a random date folder
random_folder = random.choice(date_folders)

# Get all image files from the chosen folder
image_files = [os.path.join(random_folder, f) for f in os.listdir(random_folder) if f.lower().endswith(('.png', '.jpg', '.jpeg'))]

# Choose a random image
random_image = random.choice(image_files)

# Extract movie name from the file name
movie_name = os.path.basename(random_image).rsplit('.', 1)[0].replace('_', ' ')

# Upload media
media = api.media_upload(filename=random_image)

# Post tweet with image
tweet_text = f"Day {day_count}: 🎬 #DailyMoviePuzzle"
response = client.create_tweet(text=tweet_text, media_ids=[media.media_id_string], user_auth=True)

print(f"✅ Posted Daily Puzzle Tweet: Day {day_count} - {movie_name}")

# Save to state.json
state = {"DAY_COUNT": day_count, "LAST_MOVIE": movie_name}

with open("state.json", "w") as f:
    json.dump(state, f)

print(f"✅ Saved state.json: {state}")
