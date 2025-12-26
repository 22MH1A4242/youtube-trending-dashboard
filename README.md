
# YouTube Trending ETL Dashboard

## Project Overview
This project extracts trending video data from **YouTube Data API v3**, transforms it, loads it into a **MySQL database**, and visualizes key trends in **Power BI**.  
It demonstrates a full **ETL pipeline** and provides insights into video popularity, channel performance, and user engagement metrics.

---

## Features
- **ETL Pipeline:** Automates data collection from YouTube API.  
- **Database Storage:** Stores cleaned data in MySQL for easy querying.  
- **Interactive Dashboard:** Visualizes trending videos, likes, comments, views, and channel statistics.  
- **Filters & Slicers:** Filter by channel or published date to explore specific trends.  

---

## Technologies Used
- **Python:** `extract.py`, `load.py` for API calls and data processing  
- **MySQL:** Stores trending video data  
- **Power BI:** Visualizes data in charts and dashboards  
- **Libraries:** `pandas`, `mysql-connector-python`, `google-api-python-client`  

---

## Project Structure
youtube_etl/
│
├── extract.py # Script to extract data from YouTube API
├── load.py # Script to load data into MySQL
├── youtube_trends.csv # Sample data file (optional)
├── dashboard.pdf # Exported dashboard (viewable offline)
├── README.md # Project overview (this file)

## How to Run

1. **Clone the repository:**  
`git clone https://github.com/yourusername/youtube-trending-dashboard.git`

2. **Install dependencies:**  
`pip install pandas mysql-connector-python google-api-python-client`

3. **Set up MySQL:**  
- Create a database `youtube_trends` and table `trending_videos` as shown in the scripts.  
- Update MySQL credentials in `load.py`.

4. **Run the ETL scripts:**  
`python extract.py`   # Extract data from YouTube API  
`python load.py`      # Load data into MySQL

5. **Open Power BI Dashboard:**  
- Connect to MySQL database to refresh visuals.  
- Explore charts and use slicers for filtering.
