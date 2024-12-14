# Server.py
from flask import Flask, render_template
import requests

app = Flask(__name__)

# Simulate fetching artworks from the blockchain
def fetch_artworks():
    # Ideally, this would interact with a blockchain service to fetch uploaded artworks
    artworks = [
        {"url": "http://example.com/generated_artwork.png", "description": "Generated AI artwork"}
    ]
    return artworks

@app.route('/')
def home():
    artworks = fetch_artworks()
    return render_template('index.html', artworks=artworks)

if __name__ == '__main__':
    app.run(debug=True)
