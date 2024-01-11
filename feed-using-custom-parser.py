from custom_parser import custom_parser
import sys

print(sys.argv)

feed_urls = ""
if len(sys.argv)>1:
    feed_urls = sys.argv[1:]
else:
    print("no url given to show feed")


for url in feed_urls:
    custom_parser.parsed(url)