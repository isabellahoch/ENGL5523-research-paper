import json
import os
from dotenv import load_dotenv
import requests
import pandas as pd

load_dotenv()

bearer_token = os.getenv('BEARER_TOKEN')

# stole the below from our first X-hour workshop :)
#create some functions to prepare for scraping (this does not need to make sense! don't worry!)
def create_headers(bearer_token):
    headers = {"Authorization": "Bearer {}".format(bearer_token)}
    return headers


def connect_to_endpoint(url, headers, params):
    response = requests.request("GET", url, headers=headers, params=params)
    # print(response.status_code)
    if response.status_code != 200:
        print('error connecting to endpoint')
        raise Exception(response.status_code, response.text)
    return response.json()

def fetch_tweets():
    headers = create_headers(bearer_token)
    query_params = {'query': 'dartmouth lang:en -is:retweet -is:reply',
                'tweet.fields': 'author_id,created_at,conversation_id,public_metrics',
                 'max_results': 100}
    search_url = "https://api.twitter.com/2/tweets/search/recent"
    json_response = connect_to_endpoint(search_url, headers, query_params)
    print(json_response)
    with open('data.json', 'w') as f:
        json.dump(json_response, f)

def parse_data():
    all_text = []
    num_tweets = 0

    # grab data
    with open('data/twitter/data.json') as data_file:    
        data = json.load(data_file)
        if 'data' in data:
            for tweet in data['data']:
                if 'text' in tweet:
                    all_text.append(tweet['text'])
                    num_tweets += 1

    print(all_text)

    print("FOUND "+str(num_tweets)+" TWEETS!")

    # Serializing json
    json_object = json.dumps({'posts':all_text}, indent=4)
    
    # Writing to textual_data.json.json
    with open('data/twitter/textual_data.json', 'w') as outfile:
        outfile.write(json_object)
        outfile.close() 

    with open('data/twitter/all_text.txt', 'w') as outfile:
        outfile.write('\n'.join(all_text))
        outfile.close() 


# Now fetch the data first
fetch_tweets()
# And parse it into the appropriate format
parse_data()