import pandas as pd
import mysql.connector

print("LOADING STARTED")

# Read CSV
df = pd.read_csv("youtube_trending.csv")

# Connect to MySQL
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="AnDv_2026",
    database="youtube_trends"
)

cursor = conn.cursor()

# Insert data row by row
for _, row in df.iterrows():
    cursor.execute("""
        INSERT INTO trending_videos
        (title, channel, published_date, trending_date, views, likes, comments)
        VALUES (%s, %s, %s, %s, %s, %s, %s)
    """, tuple(row))

conn.commit()
cursor.close()
conn.close()

print("DATA LOADED INTO MYSQL SUCCESSFULLY")
