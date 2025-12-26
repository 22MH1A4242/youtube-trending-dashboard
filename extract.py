print("SCRIPT STARTED")

from googleapiclient.discovery import build
import pandas as pd
from datetime import datetime

API_KEY = "AIzaSyDzYwWCtr43Gmcq_VgNcNjtJ2UPyScoUT4"

youtube = build("youtube", "v3", developerKey=API_KEY)

request = youtube.videos().list(
    part="snippet,statistics",
    chart="mostPopular",
    regionCode="IN",
    maxResults=10
)

response = request.execute()

videos = []

for item in response["items"]:
    videos.append({
        "title": item["snippet"]["title"],
        "channel": item["snippet"]["channelTitle"],
        "published_date": item["snippet"]["publishedAt"][:10],
        "trending_date": datetime.today().strftime("%Y-%m-%d"),
        "views": int(item["statistics"].get("viewCount", 0)),
        "likes": int(item["statistics"].get("likeCount", 0)),
        "comments": int(item["statistics"].get("commentCount", 0))
    })

df = pd.DataFrame(videos)
df.to_csv("youtube_trending.csv", index=False)

print("CSV CREATED SUCCESSFULLY")
print(df.head())
