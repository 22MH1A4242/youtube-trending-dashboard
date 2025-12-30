# 📊 YouTube Trending Data ETL & Dashboard

## 🔍 Problem Statement
YouTube generates massive amounts of data daily, but raw data alone does not provide actionable insights.
This project focuses on extracting, transforming, and visualizing YouTube trending video data to analyze
video performance, audience engagement, and channel popularity.

---

## 📁 Dataset Source
- YouTube Data API v3
- Extracted fields:
  - Video Title
  - Channel Name
  - Views
  - Likes
  - Comments
  - Published Date
  - Trending Date

---

## ⚙️ Steps Taken

### 1️⃣ Data Extraction
- Used Python to fetch trending video data using the YouTube Data API
- Stored extracted data into a CSV file

**Tools:** Python, YouTube Data API

---

### 2️⃣ Data Loading
- Cleaned and structured the dataset
- Loaded processed data into a MySQL database

**Tools:** Python, MySQL

---

### 3️⃣ Exploratory Data Analysis (EDA)
- Checked data quality and missing values
- Analyzed:
  - Top trending videos by views
  - Engagement metrics (likes and comments)
  - Channel-wise performance

---

### 4️⃣ Data Visualization (Power BI)
Created an interactive Power BI dashboard including:
- Clustered bar chart showing Views, Likes, and Comments by Video Title
- Line chart showing Views trend over time
- Pie chart showing Total Views by Channel
- Slicers for Channel and Published Date

**Tools:** Power BI Desktop

---


## 🛠️ Technologies Used
- Python
- MySQL
- Power BI
- Git & GitHub

---

## 🎯 Key Learnings
- Built an end-to-end ETL pipeline
- Worked with APIs and databases
- Designed professional Power BI dashboards
- Improved data analysis and visualization skills

---

## ▶️ How to Run the Project
1. Clone the repository
2. Run `extract.py` to fetch YouTube data
3. Run `load.py` to load data into MySQL
4. Open the Power BI file and refresh the data

## 📸 Final Dashboard Screenshots


<img width="1839" height="963" alt="youtue dashboard preview " src="https://github.com/user-attachments/assets/260c78f8-0924-4649-813e-f604b3a1733c" />
<img width="1920" height="1020" alt="Screenshot 2025-12-26 162702" src="https://github.com/user-attachments/assets/4452eeba-5f85-4019-807d-8496a6a7cb80" />
<img width="1920" height="1020" alt="Screenshot 2025-12-26 162650" src="https://github.com/user-attachments/assets/50dd32dd-a50e-479f-b4ba-16e3d81bbe64" />
