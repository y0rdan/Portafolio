# 🕸️ Python Web Crawler with SQLite Integration

This project is a **simple web crawler** that:
- Loads starting URLs from a file,
- Crawls web pages recursively (up to a configurable limit),
- Saves the crawled URLs to a text file, and
- Stores them in an SQLite database.

It’s designed for educational or internal use, ideal for learning about **web scraping, queue-based crawling, and database integration** in Python.

---

## 📦 Features

- ✅ Reads starting URLs from a `urls.txt` file  
- ✅ Creates and connects to a local SQLite database (`db/pages.db`)  
- ✅ Crawls pages recursively up to a max limit per domain  
- ✅ Saves crawled URLs to a file (`crawled.txt`)  
- ✅ Inserts crawled URLs into an SQLite table  
- ✅ Uses `requests` and `BeautifulSoup` for HTML parsing  

---

## 🧰 `Requirements`

Create a `requirements.txt` file with these dependencies:


requests>=2.31.0
beautifulsoup4>=4.12.3

## 🧰 Install Requirements

pip install -r requirements.txt

📂 Project Structure
    
project/
│
├── db/
│   └── pages.db          # SQLite database (auto-created)
│
├── urls.txt              # Input file containing URLs to crawl
├── crawled.txt           # Output file with all crawled URLs
├── crawler.py            # Main script (this file)
└── requirements.txt


⚙️ Usage

Prepare your URL list
Create a file named urls.txt in the same directory, e.g.:

https://example.com
https://another-site.com


**Run the crawler**

chmod +x crawler.py
./crawler.py or: python3 crawler.py


View results

Crawled URLs: stored in crawled.txt

Database: db/pages.db

Table: urls (id INTEGER PRIMARY KEY, url TEXT, visited TEXT)


🧠 How It Works
Main Functions
Function	Description
create_db()	Checks if the database exists; creates it if not.
load_url()	Loads all starting URLs from a file into a set.
crawl()	Crawls up to 10 pages (by default) from each start URL, within the same domain.
save_urls()	Saves crawled URLs to crawled.txt.
connect_db()	Opens an SQLite connection and prints connection status.
add_to_db()	Creates the urls table if it doesn’t exist and inserts crawled URLs.
print_db()	Prints the contents of the database table.

⚠️ Notes and Limitations

    The crawler currently limits itself to 10 pages per seed URL (max_pages parameter).
    It only follows internal links (same domain as the start URL).
    It doesn’t obey robots.txt — for ethical and legal use, consider adding compliance if you plan to crawl live sites.
    You must manually ensure the db/ directory exists (or the script will fail to write the database file).


👤 Author


**Yordan Borges**
Coding Portfolio Project
---
