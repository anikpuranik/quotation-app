#!/usr/bin/env python3
'''This is a demo of the quotation of the app'''
import os
import json
from pathlib import Path
from flask import Flask

# Importing Modules
import helper_functions as f

app = Flask(__name__) #creating Flask class object
title='Quotation'

@app.route('/') #decorator defines the
@app.route('/home')
@app.route('/index')
@app.route('/homepage')
def home():
    '''Hmme page for the quotation-app'''
    categories = [Path(file).stem for file in os.listdir("db")]
    return categories

@app.route('/<category>_quotes.json')
def quotes(category):
    '''Function return the quotes'''
    path = f'db/{category}.json'
    quotations = f.read_quotations_from_file(path)
    return quotations

if __name__ == "__main__":
    app.run(debug=True)
