import tweepy 
from textblob import TextBlob

consumer_key  ='xa9NXc2DJ1u2jr0E3gJxPI0hm'
consumer_key_secret = '1pSBRK7aDusgdW4yZTugMQZYQjNDSsvja03NrbVsDKJjA0lvIP'

access_token = '1438378690669252613-EJ0ZMqGTy8b1iyPWp8Xzc4KLFZRbye'
access_token_secret = 'Qoe5hKtdSnRfdGJk2GpJCz88Rv0KtVFinSnvnL8bZTs1l'

auth = tweepy.OAuthHandler(consumer_key, consumer_key_secret)

auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

public_tweets = api.search('AVENGERS')

for tweet in public_tweets:
    print(tweet.text)
    analysis = TextBlob(tweet.text)
    print(analysis.sentiment)
    if analysis.sentiment[0]>0:
      print ('Positive')
    elif analysis.sentiment[0]<0:
      print ('Negative')
    else:
      print ('Netural')  
