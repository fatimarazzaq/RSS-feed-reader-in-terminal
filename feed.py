import feedparser
import sys


feed_url = sys.argv[1]

parsed_feed = feedparser.parse(feed_url) # https://feeds.bbci.co.uk/news/rss.xml


def final_results(feed):
    if feed['bozo']:
        print("failed to fetch results")
    for entry in feed['entries']:
        print(f'Title: {entry.title}')
        print(f'Description: {entry.description}')
        print(f'Link: {entry.link}\n')


final_results(parsed_feed)
