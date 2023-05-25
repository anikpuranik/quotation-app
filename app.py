#!/usr/bin/env python3
'''This is a demo of the quotation of the app'''
import os
from pathlib import Path
from flask import Flask, render_template

app = Flask(__name__) #creating Flask class object
title='Quotation'

@app.route('/') #decorator defines the
@app.route('/home')
@app.route('/base')
@app.route('/index')
@app.route('/homepage')
def home():
    '''Hmme page for the quotation-app'''
    categories = [Path(file).stem for file in os.listdir("db")]
    return render_template('home.html', categories=categories, title=title)

def read_quotations_from_file(path):
    with open(path, "r") as file:
        quotations = file.read().split("\n")[:-1]
    return quotations

@app.route('/<category>_quotes.json')
def quotes(category):
    '''Function return the quotes'''
    path = f'db/{category}.txt'
    quotations = read_quotations_from_file(path)
    return render_template("quotes.html", category=category.upper(), 
                            quotations=quotations, title=f'{category} quotes')

if __name__ == "__main__":
    app.run(debug=True)
