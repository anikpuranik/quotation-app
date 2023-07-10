#!/usr/bin/env python3
'''This is a demo of the quotation of the app'''
import os
from flask import Flask, render_template

# Importing Modules
import helper_functions as f

app = Flask(__name__) #creating Flask class object
path = 'db'
'''
@app.route('/') #decorator defines the
@app.route('/home')
def home():
    categories = f.get_all_categories()
    return {"categories": categories}
'''
@app.route('/web')
@app.route('/homeweb')
def web_home():
    all_list = f.get_all_json_files('db')
    return render_template("home.html", all_list=all_list)

@app.route('/<category>')
def web_fun(category):
    quotes = f.read_quotations_from_file(path+f"/{category}")
    return render_template("home.html", quotes=quotes)

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')
