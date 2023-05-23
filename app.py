#!/usr/bin/env python3
'''This is a demo of the quotation of the app'''
from random import randint
from flask import Flask, url_for

app = Flask(__name__) #creating Flask class object

@app.route('/') #decorator defines the
@app.route('/home')
def home():
    '''Hmme page for the quotation-app'''
    home_page_message = "Hello, This is flask app to test the quotes app"
    return home_page_message

def read_quote_from_file(path):
    with open(path, "r") as file:
        quote = file.read().split("\n")[:-1]
    return quote

@app.route('/onepiece_quotes.json')
def onepiece_quotes():
    '''Function return the quotes for the day'''
    path = 'db/onepiece.txt'
    one_quotes = read_quote_from_file(path)
    return {"quote":one_quotes[randint(0, len(one_quotes)-1)]}

@app.route('/morning_quotes.json')
def morning_quotes():
    '''Quotes For Good Morning'''
    path = 'db/morning.txt'
    morning_quotes = read_quote_from_file(path) 
    return {"quote":morning_quotes[randint(0, len(morning_quotes)-1)]}
