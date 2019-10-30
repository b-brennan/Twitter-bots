import tweepy
import random
import numpy
import time
import re

#print("This will be my twitter bot")

#I've taken out keys/secrets for this github post
CONSUMER_KEY = 
CONSUMER_SECRET = 
ACCESS_KEY = 
ACCESS_SECRET = 


auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)


public_tweets = api.home_timeline()
user_tweets = api.user_timeline('LilNasX', count=300)

u_list = []
for u in user_tweets:
    if 'RT' not in u.text:
        u_list.append(u.text)

def get_words(tweet_list):
    words = []
    word_list = []
    new_list = []
    
    for tweet in tweet_list:
        wordStr = (re.sub("[^\w]", " ",  tweet).split())
        words.append(wordStr)
    for w in words:
        word_list += w 
    for wrd in word_list:
        new_word =' ' + wrd + ' '
        new_list.append(new_word)
    return new_list
    
def combine_tweets(tweet_list):
    words = get_words(tweet_list)
  
    random_word = random.choice(words)
    random_tweet1 = random.choice(tweet_list)
    random_tweet2 = random.choice(tweet_list)
    
    while random_word not in random_tweet1 or random_word not in random_tweet2 or random_tweet1 is random_tweet2:
        random_word = random.choice(words)
        random_tweet1 = random.choice(tweet_list)
        random_tweet2 = random.choice(tweet_list) 
    
    word_index = random_tweet1.find(random_word)
    word_index2 = random_tweet2.find(random_word)
    new_string = str(random_tweet1[:word_index] + random_tweet2[word_index2:])
    
    if 'https' in new_string:
        https = new_string.find('https')
        new_string = new_string[:https]
    
    return new_string

#print (combine_tweets(u_list))

while True:
    tweet = combine_tweets(u_list)
    api.update_status(tweet)
    time.sleep(1800)


