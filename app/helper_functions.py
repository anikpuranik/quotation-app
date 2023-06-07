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
    curr.execute("SELECT category FROM categories;")
    query = curr.fetchall()
    return format_query_series(query)

def get_all_characters_by_series(series):
    curr.execute(f"SELECT DISTINCT(Character_Name) FROM {series} ORDER BY Character_Name;")
    query = curr.fetchall()
    return format_query_series(query)

def get_quotes_by_character(character):
    curr.execute(f"SELECT quotes FROM anime_quotes WHERE Character_Name = '{character}'")
    query = curr.fetchall()
    return format_query_series(query)
