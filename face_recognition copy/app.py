from flask import Flask, render_template, redirect, url_for, request
import pandas as pd
import numpy as np
from scipy import stats
import logging
import datetime
#import os.path
from flask import Markup
import os
from face_recog import train


app=Flask(__name__)
app.config["DEBUG"]= True

@app.route('/login', methods=['POST', 'GET'])
def login():
    print("hello")

    name = train(os.getcwd)
    print(name)
    return render_template('login.html')

@app.route('/signup', methods=['POST', 'GET'])
def signup():
    name=" "
    email=" "
    password=" "
    dob=" "
    username=" "
    gender=" "
    if request.method == 'POST':
        name=request.form['name']
        email=request.form['email']
        password=request.form['password']
        dob=request.form['dob']
        username=request.form['username']
        gender=request.form['gender']
        print(name,email,password,dob,username,gender)
    print("Signed Up")

    # name = train(os.getcwd)
    # print(name)
    return render_template('signup.html')



if __name__ == '__main__': 
  
    # run() method of Flask class runs the application  
    # on the local development server. 
    app.run()