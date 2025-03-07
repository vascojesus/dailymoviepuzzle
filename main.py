import os
import random
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

auth = tweepy.OAuth1UserHandler(consumer_key, consumer_secret, access_token, access_token_secret)
api = tweepy.API(auth)

images_dir = "images"

date_folders = [os.path.join(images_dir, d) for d in os.listdir(images_dir) if os.path.isdir(os.path.join(images_dir, d))]

random_folder = random.choice(date_folders)

image_files = [os.path.join(random_folder, f) for f in os.listdir(random_folder) if f.lower().endswith(('.png', '.jpg', '.jpeg'))]

random_image = random.choice(image_files)

movie_name = os.path.basename(random_image).rsplit('.', 1)[0].replace('_', ' ')

counter_file = "tweet_counter.txt"

if not os.path.exists(counter_file):
    day_count = 1
else:
    with open(counter_file, "r") as f:
        day_count = int(f.read().strip()) + 1

with open(counter_file, "w") as f:
    f.write(str(day_count))

with open("last_posted.txt", "w") as f:
    f.write(f"{day_count},{movie_name}")

media = api.media_upload(filename=random_image)

tweet_text = f"Day {day_count}: 🎬 #DailyMoviePuzzle"
response = client.create_tweet(text=tweet_text, media_ids=[media.media_id_string], user_auth=True)

print("Tweet posted successfully!", response)