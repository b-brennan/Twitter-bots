import tweepy
import random
import time
import math

#print("This will be my twitter bot")

#I've taken out the keys/secrets for this github post

CONSUMER_KEY = 
CONSUMER_SECRET = 
ACCESS_KEY = 
ACCESS_SECRET = 


auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)


#public_tweets = api.home_timeline()


RESTS = ["Friendly's", "McDonald's", "Wendy's", "Dunkin", "Chipotle", "Moe's", "Hot Table", "Taco Bell", "Red Robin", "99", "Uno's",
         "Denny's", "Burger King", "Chick-fil-a", "Olive Garden", "Texas Roadhouse"]
INTROS = [" Hi! You should go to ", " I think you're in the mood for some ", " I personally love ", " I guess you could do ", 
          " Definitely don't not go to ", " Yo! Go to ", " A really great spot is ", " How about "]

FILE_NAME = 'last_seen_id.txt'


def random_response(rests, intros):
    randRest = random.choice(rests)
    randIntro = random.choice(intros)
    randString = str(randIntro + randRest)
    
    return randString

def retrieve_last_seen_id(file):
    f_read = open(file, 'r')
    last_seen_id = int(f_read.read().strip())
    f_read.close()
    return last_seen_id

def store_last_seen_id(last_seen_id, file):
    f_write = open(file, 'w')
    f_write.write(str(last_seen_id))
    return

def reply_to_tweets():
    last_seen_id = retrieve_last_seen_id(FILE_NAME)
    mentions = api.mentions_timeline(last_seen_id, tweet_mode='extended')

    #1154586212352634883

    for m in reversed(mentions):
        
        print(str(m.id) + ' -> ' + m.full_text)
        last_seen_id = m.id
        store_last_seen_id(last_seen_id, FILE_NAME)
    
        if '#whereshouldieat' in m.full_text.lower():
            api.update_status('@'+ m.user.screen_name + random_response(RESTS, INTROS), m.id)
            print('hashtag found...responding')
        
while True:
    reply_to_tweets()
    time.sleep(15)
