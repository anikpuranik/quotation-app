#!/usr/bin/env python3
'''This is a demo of the quotation of the app'''
from random import randint
from flask import Flask

app = Flask(__name__) #creating the Flask class object

@app.route('/') #decorator defines the
def home():
    '''Hmme page for the quotation-app'''
    return "Hello, This is flask app to test the quotes app"

@app.route('/quotes')
def quotes():
    '''Function return the quotes for the day'''
    lis = ("Father", "Mother", "Son", "GrandFather", "GrandMother")
    output = lis[randint(0, len(lis))]
    print(output)
    return output

if __name__ =='__main__':
    app.run(port=8000, debug = True)
