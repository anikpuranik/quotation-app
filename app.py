#!/usr/bin/env python3
'''This is a demo of the quotation of the app'''
from random import randint
from flask import Flask

app = Flask(__name__) #creating Flask class object

@app.route('/') #decorator defines the
def home():
    '''Hmme page for the quotation-app'''
    return "Hello, This is flask app to test the quotes app"

@app.route('/quotes')
def quotes():
    '''Function return the quotes for the day'''
    lis = ("Scars On The Back Are A Swordsman's Shame. - Roronoa Zoro", 
            "How Can We Look Any Of You In The Eyes And Say That Wano Is Safe With Us? - Kozuki Momonosuke", 
            "The New Era Of Daring Ones Is Coming With An Unstoppable Swell!- Trafalgar D. Law", 
            "People’s Dreams... Have No Ends — Marshall D. Teach",
            "One Piece Does Exist! — Edward 'Whitebeard' Newgate")
    output = lis[randint(0, len(lis))]
    print(output)
    return output

if __name__ =='__main__':
    app.run(port=8000, debug = True)
