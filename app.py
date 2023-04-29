#!/usr/bin/env python3
from flask import Flask  
from random import randint

app = Flask(__name__) #creating the Flask class object   
 
@app.route('/') #decorator drfines the   
def home():  
    return "Hello, This is flask app to test the quotes app";  

@app.route('/quotes')
def quotes():
    lis = ("Father", "Mother", "Son", "GrandFather", "GrandMother")
    output = lis[randint(0, len(lis))]
    print(output)
    return output

if __name__ =='__main__':  
    app.run(port=8000, debug = True)
