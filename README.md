# Trending Hashtags

## Summary
Count hashtags on twitter for a specified geo location overnight, and google search them in order to find trending news articles for when you wake up.

## Code Overview

This is a simple code to scrape real time public domain tweets, and maintain a cumulative histogram of the unique hashtags. Tweepy is used to scrape the tweets and feed the separated hashtags into a counter. An asyncronous messaging (via RabbitMQ) has been utilized to message the hashtags with a heighest counts to a download script every X seconds, which in turn google searches and downloads urls for these hashtags. Another instance of use for asynchrnous messaging is to maintain a plot of the top trending hashtags for easy viewing.
