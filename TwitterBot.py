# TwitterBot.py
import tweepy
import openai
import requests
from PIL import Image
from io import BytesIO

# Twitter API keys (replace with your own credentials)
CONSUMER_KEY = 'your_consumer_key'
CONSUMER_SECRET = 'your_consumer_secret'
ACCESS_TOKEN = 'your_access_token'
ACCESS_TOKEN_SECRET = 'your_access_token_secret'

# OpenAI API key (replace with your own API key)
openai.api_key = 'your_openai_api_key'

# Set up Twitter authentication
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)

# Define function to fetch tweets
def fetch_tweets():
    tweets = api.user_timeline(screen_name='ai_agent_account', count=10, tweet_mode='extended')
    for tweet in tweets:
        if 'art' in tweet.full_text.lower():
            text = tweet.full_text
            print(f"Processing tweet: {text}")
            generate_artwork(text)

# Define function to generate artwork based on tweet
def generate_artwork(prompt):
    response = openai.Image.create(
        prompt=prompt,
        n=1,
        size="1024x1024"
    )
    img_url = response['data'][0]['url']
    image_data = requests.get(img_url).content
    img = Image.open(BytesIO(image_data))
    img.show()  # Show the generated image
    img.save('generated_artwork.png')  # Save the artwork
    upload_to_blockchain('generated_artwork.png')  # Upload the image to blockchain

# Placeholder function to upload image to blockchain
def upload_to_blockchain(image_path):
    # You would call the upload function here (details in BlockchainInteraction.js)
    print(f"Uploading {image_path} to blockchain.")

if __name__ == '__main__':
    fetch_tweets()
