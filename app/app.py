#!/usr/bin/env python3
'''This is a demo of the quotation of the app'''
import os
from flask import Flask

# Importing Modules
import helper_functions as f

app = Flask(__name__) #creating Flask class object

@app.route('/') #decorator defines the
@app.route('/home')
def home():
    categories = f.get_all_categories()
    return {"categories": categories}

@app.route('/<series>_quotes.json')
def series_data(series):
    quotes = f.get_all_characters_by_series(series)
    return {"series": series}

@app.route('/<character>_quotes.json')
def character_data(character):
    quotes = f.get_quotes_by_character(character)
    return {"quotes": quotes}

if __name__ == "__main__":
    app.run(debug=True)
