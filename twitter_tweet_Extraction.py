from data_pre_processing import data_preprocessing
import tweepy
import datetime
import csv
import os
import pandas as pd
import shutil
import re
import yfinance as yf

#ADD your credentials here
'''consumer_key =
consumer_secret =
access_token =
access_token_secret =
'''
# Credentials of one of our teammates
consumer_key='7pCrGcjYjcf1oeEK1ur3999pw'
consumer_secret='O2YkRoOQXjCgjOerh9mxCfHWwYCy8c1sAQSY5zqJFR7eKUQfY2'
access_token='1647380080291708929-6zMKh0i6i5PaZgJge0TYAUlvG2pX4n'
access_token_secret='xU6pMLrTPx2cJKdhJvtgQ8kvAzY2y1ChiNdbC22644m6M'

def getTweets(stock,company):
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth,wait_on_rate_limit=True)
    
    

    #for tweet in tweepy.Cursor(api.search_tweets,q=("from:" + "@elonmusk"),lang="en",count=1000).items():
    #handles = ["elonmusk"] # replace with handles of your choice
    #for handle in handles:

    #Random working

    output = []
    '''
    # search for tweets containing "Microsoft" within the specified ID range
    #for tweet in tweepy.Cursor(api.search,q='Microsoft',lang="en",result_type="recent").items(2):
    for tweet in tweepy.Cursor(api.search_tweets,q=('microsoft'),lang="en",result_type="popular").items():
        if tweet.retweet_count >= 100 and tweet.favorite_count >= 50:
       
        #if (not tweet.retweeted) and ('RT @' not in tweet.text):
            tweet.text = re.sub(r'[^\x00-\x7F]+',' ', tweet.text)
            text = tweet.text
            favourite_count = tweet.favorite_count
            retweet_count = tweet.retweet_count
            created_at = tweet.created_at
            line = {'text' : text, 'favourite_count' : favourite_count, 'retweet_count' : retweet_count, 'created_at' : created_at}
            output.append(line)
    df = pd.DataFrame(output)
    df.to_csv("./output/" + stock + ".csv")
    data = pd.read_csv(r"./output/" + stock + ".csv" , encoding = 'utf8')
    return data
    
    users = []
    for user in tweepy.Cursor(api.search_users, q="tech").items(10):
        users.append(user.screen_name)
    #print(users)
    for handle in users:
        # Collect tweets from successful people that mention the company
        for tweet in tweepy.Cursor(api.user_timeline, screen_name=handle,tweet_mode='extended').items():
            if (not tweet.retweeted) and ('RT @' not in tweet.full_text):
                tweet_text = tweet.full_text
                #if re.search(r'\b{}\b'.format(company), tweet_text, re.IGNORECASE):
                if re.search(company, tweet_text, re.IGNORECASE):
                    tweet_text = re.sub(r'[^\x00-\x7F]+',' ', tweet_text)
                    favourite_count = tweet.favorite_count
                    retweet_count = tweet.retweet_count
                    created_at = tweet.created_at
                    line = {'text' : tweet_text, 'favourite_count' : favourite_count, 'retweet_count' : retweet_count, 'created_at' : created_at, 'handle': handle}
                    output.append(line)
    df = pd.DataFrame(output)
    #df = df[(pd.to_datetime(df['created_at']) >= start_date) & (pd.to_datetime(df['created_at']) <= end_date)]
    df.to_csv("./output/" + stock +"sucessfulhandles"+".csv")
    data = pd.read_csv(r"./output/" +stock+ "sucessfulhandles"+".csv" , encoding = 'utf8')
    return data
    '''
    '''
    # Search for tweets containing "Microsoft" posted by the selected users
    for user in users:
        query = "from:" + user + " Microsoft"
        tweets = tweepy.Cursor(api.search_tweets, q=query, lang="en", tweet_mode="extended").items(10)
        for tweet in tweets:
            #if (not tweet.retweeted) and ('RT @' not in tweet.text):
            tweet.text = re.sub(r'[^\x00-\x7F]+',' ', tweet.full_text)
            text = tweet.text
            favourite_count = tweet.favorite_count
            retweet_count = tweet.retweet_count
            created_at = tweet.created_at
            line = {'text' : text, 'favourite_count' : favourite_count, 'retweet_count' : retweet_count, 'created_at' : created_at}
            output.append(line)
            # Clean the text of the tweet
            
            text = re.sub(r'http\S+', '', tweet.full_text) # Remove URLs
            text = re.sub(r'@[A-Za-z0-9_]+', '', text) # Remove usernames
            text = re.sub(r'[^\w\s]', '', text) # Remove punctuation
            text = re.sub(r'\s+', ' ', text) # Remove extra whitespace
            text = text.lower() # Convert to lowercase
            line = {'text' : text}# 'favourite_count' : favourite_count, 'retweet_count' : retweet_count, 'created_at' : created_at}
            output.append(line)
            
        df = pd.DataFrame(output)
        #df = df[(pd.to_datetime(df['created_at']) >= start_date) & (pd.to_datetime(df['created_at']) <= end_date)]
        df.to_csv("./output/" + stock +"random"+".csv")
        data = pd.read_csv(r"./output/" +stock+ "random"+".csv" , encoding = 'utf8')
        print("done")
        return data
            #output.append(text)
    # Define the company you want to search for
    '''

    # handles with sucessful people working over years 2019-22 in file TSLA.csv
    #then now adding covid to see how sentiment happened then
    #handles=["@elonmusk", "@Tesla", "@MKBHD"]
    #handles = ["@elonmusk", "@BillGates", "@satyanadella", "@tim_cook", "@JeffBezos"]
    
    import pandas as pd

# Filter data from 2020 to 2022
    start_date = pd.to_datetime('2022-01-01', utc=True)
    end_date = pd.to_datetime('2023-04-01', utc=True)
    handles = []

    with open('./data/twitteruserhandles/randomuser_twiiterhandle.csv', newline='') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            handles.append(row[2])
    search_terms = ['# +techlayoffs', 'Microsoft']
    #handles=["@lindeplc","@scott_santi","@BrownGreg2","@Rich_Barton","@AlexGorsky"]
    #handles = ["@elonmusk", "@BillGates", "@satyanadella", "@tim_cook", "@JeffBezos"]
    for handle in handles:
        # Collect tweets from successful people that mention the company
        for tweet in tweepy.Cursor(api.user_timeline, screen_name=handle,tweet_mode='extended').items():
            if (not tweet.retweeted) and ('RT @' not in tweet.full_text):
                tweet_text = tweet.full_text
                #if re.search(r'\b{}\b'.format(company), tweet_text, re.IGNORECASE):
                if re.search(company, tweet_text, re.IGNORECASE):
                    tweet_text = re.sub(r'[^\x00-\x7F]+',' ', tweet_text)
                    favourite_count = tweet.favorite_count
                    retweet_count = tweet.retweet_count
                    created_at = tweet.created_at
                    line = {'text' : tweet_text, 'favourite_count' : favourite_count, 'retweet_count' : retweet_count, 'created_at' : created_at, 'handle': handle}
                    output.append(line)
    df = pd.DataFrame(output)
    #df = df[(pd.to_datetime(df['created_at']) >= start_date) & (pd.to_datetime(df['created_at']) <= end_date)]
    df.to_csv("./data/random30usersdata"+".csv")
    data = pd.read_csv("./data/random30usersdata"+".csv" , encoding = 'utf8')
    return data
