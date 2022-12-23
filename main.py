from googleapiclient.discovery import build
from pprint import pprint

api_key = "your_ap_ki"
channel_name = "sentdex"

youtube = build("youtube", "v3", developerKey=api_key)

request = youtube.channels().list(part="statistics", forUsername=channel_name)

response = request.execute()
items = response["items"]

for item in items:
    subscriber = item["statistics"]["subscriberCount"]
    videoCount = item["statistics"]["videoCount"]
    print("Channel: ", channel_name)
    print("Subscribers: ", subscriber)
    print("Total videos: ", videoCount)
