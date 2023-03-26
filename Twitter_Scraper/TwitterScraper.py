import tweepy
import json
import argparse


# Open the JSON file and load the data
def load_env():
    with open('../env.json') as f:
        data = json.load(f)

    return data

def handle_auth(tokens):

    consumer_key = tokens.CONSUMER_KEY
    consumer_secret = tokens.CONSUMER_SECRET
    access_token = tokens.ACCESS_TOKEN
    access_token_secret = tokens.ACCESS_TOKEN_SECRET

    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)

    return tweepy.API(auth)

def parse_args():
    # Create a new ArgumentParser object
    parser = argparse.ArgumentParser(description='Collect n of the most recent tweets with a hashtag of your choice')

    # Add an argument for the hashtag to search for
    parser.add_argument('hashtag', type=str, help='The hashtag to search for')

    # Add an optional argument for the number of tweets to retrieve (default 100)
    parser.add_argument('--count', type=int, default=100, help='The number of tweets to retrieve')

    # Parse the command-line arguments
    args = parser.parse_args()
    return args


def main():

    args = parse_args()
    api = handle_auth(load_env())
    tweets = tweepy.Cursor(api.search, q=args.hashtag).items(args.count)

    for tweet in tweets:
        print(tweet.text)

if __name__ == '__main__':
    main()




