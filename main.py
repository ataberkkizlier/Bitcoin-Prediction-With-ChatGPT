import feedparser
import ssl
from datetime import datetime, timedelta, timezone

ssl._create_default_https_context = ssl._create_unverified_context

url = "https://cointelegraph.com/rss/tag/bitcoin"
feed = feedparser.parse(url)

print("Feed Title:", feed.feed.title)
print("Feed Description:", feed.feed.description)
print("Feed Link:", feed.feed.link)

# Get current time in UTC timezone
now = datetime.now(timezone.utc)

# Define the time range (e.g., the last 24 hours)
time_range = timedelta(days=1)


for entry in feed.entries:
    entry_date = datetime.strptime(entry.published, "%a, %d %b %Y %H:%M:%S %z").astimezone(timezone.utc)

    if now - entry_date <= time_range:
        print("Entry Title:", entry.title)
        print("Entry Link:", entry.link)
        print("Entry Published Date:", entry.published)
        print("Entry Summary:", entry.summary)
        print("\n")
import csv

# Prepare the CSV file
with open('hohoho.csv', mode='w', newline='', encoding='utf-8') as csv_file:
    fieldnames = ['title', 'link', 'published', 'summary']
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    writer.writeheader()
    # Iterate through entries and write to the CSV file
    for entry in feed.entries:
        writer.writerow({'title': entry.title, 'link': entry.link, 'published': entry.published, 'summary': entry.summary})
def fetch_rss_data(url):
    feed = feedparser.parse(url)
    print("Feed Title:", feed.feed.title)
    for entry in feed.entries:
        print("Entry Title:", entry.title)
        print("Entry Link:", entry.link)
        print("Entry Published Date:", entry.published)
        print("Entry Summary:", entry.summary)
        print("\n")
# List of RSS feed URLs
rss_feed_urls = [
    "https://bitcoinmagazine.com/.rss/full/",

]
# Fetch data from multiple RSS feeds
for url in rss_feed_urls:
    fetch_rss_data(url)
