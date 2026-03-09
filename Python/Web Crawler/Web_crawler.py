#!/usr/bin/env python3

import sqlite3
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse
from collections import deque
import os


# FUNCTIONS


# Creates Database

def create_db(db_path = "db/pages.db"):

    # Checks if Database exists if nor it creates it

    if os.path.exists(db_path):
        print(f"[-] {db_path} Database Already exists")

    # Creates Database on provided path
    # if not provided uses  "db/pages.db" as default

    else:

        try:
            with open (db_path, "a") as file:
                print(f"[+] File {db_path} has been created")

        except IOError:
            print("[-] Can't create database")
            print(IOError)
            exit(1)

# Loads URLs form file

def load_url(file_name):

    #Variable Defined

    urls = set()

    # Reads from URLs File

    with open(file_name, 'r') as f:
        for line in f:

            # Adds URLS to Set urls()

            urls.add(line.strip())

    print("[+] Loaded URLs")
    print(f"[+] Total Loaded: {len(urls)}")
    print("[+] Loaded URLs:")

    # Display Crawled URLs on console

    for idx, url in enumerate(urls):
        print(f"[+] {idx + 1}/{len(urls)}: {url}")

    print("[+] Loaded URLs Complete\n")

    # Returns Set of crawled URLs

    return urls

# Saves URLs crawled to an output file

def save_urls(urls, out_file):

    # Opens or Create Output file

    with open(out_file, 'a') as f:

        # Writes each URL to output file

        for url in urls:
            f.write(url + '\n')

    print(f"[+] Saved {len(urls)} urls to {out_file}\n")

# Crawling function

def crawl(start_url, max_pages=10):

    # Variables

    queue = deque([start_url])
    visited = set()

    # Queue Definition

    while queue and len(visited) < max_pages:
        url = queue.popleft()
        if url in visited:
            continue

        # Crawls each URL

        try:
            response = requests.get(url, timeout=5)

            if response.status_code != 200:
                continue

            visited.add(url)
            print(f"[+] Crawling: {url}")

            soup = BeautifulSoup(response.text, "html.parser")
            for link_tag in soup.find_all("a", href=True):

                link = urljoin(url, link_tag["href"])

                if urlparse(link).netloc == urlparse(start_url).netloc:
                    queue.append(link)



        except requests.exceptions.RequestException as e:
            print(f"[-] Failed to crawl: {url} ({e})")

    print("[+] Crawling Complete")
    print(f"[+] Total Crawled: {len(visited)}")
    print("[+] Crawled URLs:")

    for url in visited:
        print(" -", url)

    save_urls(list(visited), out_file="crawled.txt")

    return set(visited)

# Connects to Database

def connect_db(db_path):
    if os.path.exists(db_path):
        try:
            conn = sqlite3.connect(db_path)
            c = conn.cursor()
            print(f"[+] Connected to {db_path}")

        except sqlite3.OperationalError as e:
            print(f"[-] ERROR on {db_path} - ", e)
            exit(1)
    else:
        print(f"[-] {db_path} Database Doesn't exist")

# Prints Database Content

def print_db(db_path):
    connect_db(db_path)
    conn = sqlite3.connect(db_path)
    c = conn.cursor()

    print("[+] Printing Database")
    for row in c.execute("SELECT * FROM urls"):
        print(row)

# Adds crawled URLs to Database

def add_to_db(urls, db_path):
    # Create Connector Cursor
    conn = sqlite3.connect(db_path)
    c = conn.cursor()

    # Connect to DB


    for url in visited:
        c.execute("CREATE TABLE IF NOT EXISTS urls (id INTEGER PRIMARY KEY, url TEXT, visited TEXT)")
        c.execute("INSERT INTO urls (url,visited) VALUES (?, ?)", (url,"yes"))
    conn.commit()

    print_db(db_path)


# MAIN

if __name__ == "__main__":

    urls = load_url("urls.txt")
    db_path = "db/pages.db"

    create_db(db_path)
    connect_db(db_path)




    for url in urls:
        visited = set(crawl(url))
        add_to_db(visited, db_path)


