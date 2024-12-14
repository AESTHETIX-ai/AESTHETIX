# AI Artist Agent with AI16Z Framework for Twitter Interaction and Blockchain Integration
![7df24373dddc3215f7ec42025a9cd93](https://github.com/user-attachments/assets/d863ebf7-eea6-435f-b698-c584447e5fbf)

## Project Overview

This project aims to create an **AI Artist Agent** powered by the **AI16Z framework** that interacts with **Twitter personalities**. It generates **artistic images** based on Twitter content, stores these images on a **blockchain**, and displays outstanding artworks on an official platform. The goal is to combine **AI-driven art generation**, **Twitter integration**, and **blockchain-based storage** into a seamless ecosystem.

The system ensures that the generated artworks are stored securely, with ownership tracked through **Ethereum blockchain** technology. The project is designed for artists, creators, and technology enthusiasts interested in AI, art, and blockchain.

### Key Features:
- **AI Agent**: The agent listens to Twitter posts and generates artworks using the content.
- **Blockchain Storage**: Generated artworks are stored on Ethereum blockchain, ensuring decentralization and secure ownership.
- **Official Platform**: An official web platform where the best artworks are displayed.
- **Smart Contracts**: Ethereum smart contracts handle artwork storage and ownership tracking.

![4743d905b16617e1172f2a9a8e45488](https://github.com/user-attachments/assets/62a0a33a-6bfb-4a02-ba48-d3338c2a8b07)


## Table of Contents

1. [Technologies Used](#technologies-used)
2. [System Architecture](#system-architecture)
3. [Installation & Setup](#installation-setup)
4. [AI Agent Development](#ai-agent-development)
5. [Blockchain Integration](#blockchain-integration)
6. [Uploading Artworks to Blockchain](#uploading-artworks-to-blockchain)
7. [Displaying Artworks on the Platform](#displaying-artworks-on-platform)
8. [Testing](#testing)
9. [Conclusion](#conclusion)
10. [File Structure](#file-structure)
11. [License](#license)

---

## Technologies Used

This project uses the following technologies:

- **AI16Z Framework**: The framework used to build the AI agent for generating artwork.
- **Python**: Python is used to interact with the **Twitter API**, generate art via the **OpenAI DALL·E API**, and save the generated images.
- **Node.js**: Node.js is used to interact with the **Ethereum blockchain** through the **Web3.js** library.
- **Solidity**: Solidity is used to write smart contracts that handle storing artwork metadata on the blockchain.
- **Flask**: Flask is used to create the web-based platform to display artworks.
- **OpenAI DALL·E API**: This API is used for generating artistic images based on textual descriptions.
- **Twitter API**: This API is used to monitor tweets from specified users.
- **Ethereum Blockchain**: Ethereum is used for decentralized storage of artwork and to track ownership.

---

## System Architecture

The system is composed of the following components:

1. **AI Agent**: Listens to content from Twitter personalities, analyzes their tweets, and generates artwork.
2. **Twitter API Integration**: Captures tweet content from selected Twitter users and sends it to the AI agent for artwork generation.
3. **Blockchain Storage**: Generated artwork is uploaded to the Ethereum blockchain, ensuring transparent and immutable storage.
4. **Official Display Platform**: A web application powered by Flask that allows users to view the artworks stored on the blockchain.
5. **Smart Contracts**: Ethereum-based smart contracts handle uploading, managing, and tracking ownership of the artworks.

---

## Installation & Setup

Follow these instructions to get the project up and running.

### Prerequisites

1. **Python 3.x** – For backend operations and AI integration.
2. **Node.js** and **npm** – For managing blockchain interactions.
3. **Ethereum Wallet** – MetaMask or any other wallet to interact with Ethereum.
4. **Twitter Developer Account** – To access Twitter API keys.


# agent-twitter-client

This is a modified version of [@the-convocation/twitter-scraper](https://github.com/the-convocation/twitter-scraper) with added functionality for sending tweets and retweets. This package does not require the Twitter API to use and will run in both the browser and server.

## Installation

```sh
npm install agent-twitter-client
```

## Setup

Configure environment variables for authentication.

```
TWITTER_USERNAME=    # Account username
TWITTER_PASSWORD=    # Account password
TWITTER_EMAIL=       # Account email
PROXY_URL=           # HTTP(s) proxy for requests (necessary for browsers)

# Twitter API v2 credentials for tweet and poll functionality
TWITTER_API_KEY=               # Twitter API Key
TWITTER_API_SECRET_KEY=        # Twitter API Secret Key
TWITTER_ACCESS_TOKEN=          # Access Token for Twitter API v2
TWITTER_ACCESS_TOKEN_SECRET=   # Access Token Secret for Twitter API v2
```

### Getting Twitter Cookies

It is important to use Twitter cookies to avoid sending a new login request to Twitter every time you want to perform an action.

In your application, you will likely want to check for existing cookies. If cookies are not available, log in with user authentication credentials and cache the cookies for future use.

```ts
const scraper = await getScraper({ authMethod: 'password' });

scraper.getCookies().then((cookies) => {
  console.log(cookies);
  // Remove 'Cookies' and save the cookies as a JSON array
});
```

## Getting Started

```ts
const scraper = new Scraper();
await scraper.login('username', 'password');

// If using v2 functionality (currently required to support polls)
await scraper.login(
  'username',
  'password',
  'email',
  'appKey',
  'appSecret',
  'accessToken',
  'accessSecret',
);

const tweets = await scraper.getTweets('elonmusk', 10);
const tweetsAndReplies = scraper.getTweetsAndReplies('elonmusk');
const latestTweet = await scraper.getLatestTweet('elonmusk');
const tweet = await scraper.getTweet('1234567890123456789');
await scraper.sendTweet('Hello world!');

// Create a poll
await scraper.sendTweetV2(
  `What's got you most hyped? Let us know! 🤖💸`,
  undefined,
  {
    poll: {
      options: [
        { label: 'AI Innovations 🤖' },
        { label: 'Crypto Craze 💸' },
        { label: 'Both! 🌌' },
        { label: 'Neither for Me 😅' },
      ],
      durationMinutes: 120, // Duration of the poll in minutes
    },
  },
);
```

### Fetching Specific Tweet Data (V2)

```ts
// Fetch a single tweet with poll details
const tweet = await scraper.getTweetV2('1856441982811529619', {
  expansions: ['attachments.poll_ids'],
  pollFields: ['options', 'end_datetime'],
});
console.log('tweet', tweet);

// Fetch multiple tweets with poll and media details
const tweets = await scraper.getTweetsV2(
  ['1856441982811529619', '1856429655215260130'],
  {
    expansions: ['attachments.poll_ids', 'attachments.media_keys'],
    pollFields: ['options', 'end_datetime'],
    mediaFields: ['url', 'preview_image_url'],
  },
);
console.log('tweets', tweets);
```

## API

### Authentication

```ts
// Log in
await scraper.login('username', 'password');

// Log out
await scraper.logout();

// Check if logged in
const isLoggedIn = await scraper.isLoggedIn();

// Get current session cookies
const cookies = await scraper.getCookies();

// Set current session cookies
await scraper.setCookies(cookies);

// Clear current cookies
await scraper.clearCookies();
```

### Profile

```ts
// Get a user's profile
const profile = await scraper.getProfile('TwitterDev');

// Get a user ID from their screen name
const userId = await scraper.getUserIdByScreenName('TwitterDev');
```

### Search

```ts
import { SearchMode } from 'agent-twitter-client';

// Search for recent tweets
const tweets = scraper.searchTweets('#nodejs', 20, SearchMode.Latest);

// Search for profiles
const profiles = scraper.searchProfiles('John', 10);

// Fetch a page of tweet results
const results = await scraper.fetchSearchTweets('#nodejs', 20, SearchMode.Top);

// Fetch a page of profile results
const profileResults = await scraper.fetchSearchProfiles('John', 10);
```

### Relationships

```ts
// Get a user's followers
const followers = scraper.getFollowers('12345', 100);

// Get who a user is following
const following = scraper.getFollowing('12345', 100);

// Fetch a page of a user's followers
const followerResults = await scraper.fetchProfileFollowers('12345', 100);

// Fetch a page of who a user is following
const followingResults = await scraper.fetchProfileFollowing('12345', 100);

// Follow a user
const followUserResults = await scraper.followUser('elonmusk');
```

### Trends

```ts
// Get current trends
const trends = await scraper.getTrends();

// Fetch tweets from a list
const listTweets = await scraper.fetchListTweets('1234567890', 50);
```

### Tweets

```ts
// Get a user's tweets
const tweets = scraper.getTweets('TwitterDev');

// Get a user's liked tweets
const likedTweets = scraper.getLikedTweets('TwitterDev');

// Get a user's tweets and replies
const tweetsAndReplies = scraper.getTweetsAndReplies('TwitterDev');

// Get tweets matching specific criteria
const timeline = scraper.getTweets('TwitterDev', 100);
const retweets = await scraper.getTweetsWhere(
  timeline,
  (tweet) => tweet.isRetweet,
);

// Get a user's latest tweet
const latestTweet = await scraper.getLatestTweet('TwitterDev');

// Get a specific tweet by ID
const tweet = await scraper.getTweet('1234567890123456789');

// Send a tweet
const sendTweetResults = await scraper.sendTweet('Hello world!');

// Send a quote tweet - Media files are optional
const sendQuoteTweetResults = await scraper.sendQuoteTweet('Hello world!', '1234567890123456789', ['mediaFile1', 'mediaFile2']);

// Retweet a tweet
const retweetResults = await scraper.retweet('1234567890123456789');

// Like a tweet
const likeTweetResults = await scraper.likeTweet('1234567890123456789');
```

## Sending Tweets with Media

### Media Handling
The scraper requires media files to be processed into a specific format before sending:
- Media must be converted to Buffer format
- Each media file needs its MIME type specified
- This helps the scraper distinguish between image and video processing models

### Basic Tweet with Media
```ts
// Example: Sending a tweet with media attachments
const mediaData = [
  {
    data: fs.readFileSync('path/to/image.jpg'),
    mediaType: 'image/jpeg'
  },
  {
    data: fs.readFileSync('path/to/video.mp4'),
    mediaType: 'video/mp4'
  }
];

await scraper.sendTweet('Hello world!', undefined, mediaData);
```

### Supported Media Types
```ts
// Image formats and their MIME types
const imageTypes = {
  '.jpg':  'image/jpeg',
  '.jpeg': 'image/jpeg',
  '.png':  'image/png',
  '.gif':  'image/gif'
};

// Video format
const videoTypes = {
  '.mp4': 'video/mp4'
};
```


### Media Upload Limitations
- Maximum 4 images per tweet
- Only 1 video per tweet
- Maximum video file size: 512MB
- Supported image formats: JPG, PNG, GIF
- Supported video format: MP4
