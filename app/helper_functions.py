#!/usr/bin/env python3
# Importing modules
import os
import json
import psycopg2

conn = psycopg2.connect(user=os.getenv("POSTGRES_USER"), password=os.getenv("POSTGRES_PASSWORD"), 
                        host=os.getenv("POSTGRES_HOST"), port=os.getenv("POSTGRES_PORT"))
curr = conn.cursor()

def format_query_series(query_output):
    output_list = []
    for output in query_output:
        output_list.append(*output)
    return output_list

def read_quotations_from_file(path):
    with open(path, "r") as file:
        quotations = json.load(file)
    return quotations

def get_all_categories():
    curr.execute("SELECT DISTINCT(Character_Name) FROM onepiece ORDER BY Character_Name;")
    members = curr.fetchall()
    return format_query_series(members)

def get_quotes_by_character(character):
    curr.execute(f"SELECT quotes FROM onepiece WHERE Character_Name = '{character}'")
    quotes = curr.fetchall()
    return format_query_series(quotes)
