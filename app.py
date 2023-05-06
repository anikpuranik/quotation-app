#!/usr/bin/env python3
'''This is a demo of the quotation of the app'''
from random import randint
from flask import Flask

app = Flask(__name__) #creating Flask class object

@app.route('/') #decorator defines the
def home():
    '''Hmme page for the quotation-app'''
    return "Hello, This is flask app to test the quotes app"

def read_quote_from_file(path):
    with open(path, "r") as file:
        quote = file.read().split("\n")
    return quote

@app.route('/onepiece_quotes.json')
def onepiece_quotes():
    '''Function return the quotes for the day'''
    path = '/home/asus/Desktop/python/quotation-app/db/onepiece.txt'
    one_quotes = read_quote_from_file(path)
    return {"quote":one_quotes[randint(0, len(one_quotes))]}

@app.route('/morning_quotes.json')
def morning_quotes():
    '''Quotes For Good Morning'''
    path = '/home/asus/Desktop/python/quotation-app/db/morning.txt'
    morning_quotes = read_quote_from_file(path)    
    return {"quote":morning_quotes[randint(0, len(morning_quotes))]}

if __name__ =='__main__':
    app.run(port=5000, debug = True)
