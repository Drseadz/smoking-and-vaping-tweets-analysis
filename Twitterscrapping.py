# -*- coding: utf-8 -*-
"""
Created on Mon Nov 17 06:53:11 2022

@author: Dr Oluwaseun
"""

import pandas as pd
import snscrape.modules.twitter as sntwitter
query = "vaping, smoking uk (#vaping, OR #smoking)"
tweets = []
limit = 5000
for tweet in sntwitter.TwitterHashtagScraper(query).get_items():
    if len(tweets) == limit:
        break
    else:
        tweets.append([tweet.date, tweet.url, tweet.user.username, tweet.sourceLabel, tweet.user.location, tweet.content, tweet.likeCount, tweet.retweetCount,  tweet.quoteCount, tweet.replyCount])
df = pd.DataFrame(tweets, columns=['Date', 'TweetURL','User', 'Source', 'Location', 'Tweet', 'Likes_Count','Retweet_Count', 'Quote_Count', 'Reply_Count'])
df.to_csv('finalhealthuk2.csv')