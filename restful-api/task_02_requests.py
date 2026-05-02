#!/usr/bin/python3
"""restful apii"""
import requests
import csv
import json


def fetch_and_print_posts():
    """butun basliqlari ekrana cixarir"""
    resp = requests.get("https://jsonplaceholder.typicode.com/posts")
    sc = rsp.status_code
    r_json = resp.json()
    print(f"Status Code: {sc}")
    for i in r_json:
        print(i["title"])

def fetch_and_save_posts():
    """Function to fetch and save posts."""

    resp = requests.get("https://jsonplaceholder.typicode.com/posts")
    sc = resp.status_code
    header = ["id", "title", "body"]
    r_json = resp.json()

    if (sc == 200):
        with open("posts.csv", "w") as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=header)
            writer.writeheader()
            
            for post in r_json:
                row = {}
                for field in header:
                    row[field] = post[field]
                    writer.writerow(row)
