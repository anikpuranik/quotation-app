#!/usr/bin/env python3
# Importing modules
import os
import re
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

def get_all_json_files(path):
    #return os.listdir(path)
    return [file[:-5] for file in os.listdir(path) if re.search(".json", file)]

def get_table_level(category):
    curr.execute(f"SELECT Table_Level FROM all_tables_details WHERE Table_Name='{category}';")
    query = curr.fetchall()
    print(query)
    return format_query_series(query)

def get_quotes(table):
    curr.execute(f"SELECT QUOTE FROM {table};")
    query = curr.fetchone()
    return format_query_series(query)

def get_all_anime():
    curr.execute("SELECT DISTINCT(Series_Name) FROM anime_quotes;")
    query = curr.fetchall()
    return format_query_series(query)

def get_all_characters_by_series(series):
    curr.execute(f"SELECT DISTINCT(Character_Name) FROM anime_quotes WHERE Series_Name = '{series}';")
    query = curr.fetchall()
    return format_query_series(query)

def get_quotes_by_character(series, character):
    curr.execute(f"SELECT Quote FROM anime_quotes WHERE Series_name = '{series}' AND Character_Name = '{character}';")
    query = curr.fetchall()
    return format_query_series(query)

def get_quotes(table, clauses=''):
    if clauses:
        curr.execute(f"SELECT Quotes FROM {table} WHERE {clauses};")
    else:
        curr.execute(f"SELECT Quote FROM {table};")
    query = curr.fetchall()
    return format_query_series(query)

def can_get_quotes(category):
    if category == "morning_quotes":
        return True
    return False
        


