from flask import Flask, render_template, redirect, url_for, request
import pandas as pd
import numpy as np
from scipy import stats
import logging
import datetime
import os.path
from flask import Markup
import os
from face_recog import train
from flask_mysqldb import MySQL

UPLOAD_FOLDER = 'static/uploads/'

app=Flask(__name__)
app.config["DEBUG"]= True
app.config['MYSQL_HOST'] = '127.0.0.1'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'tarp'
app.config["UPLOAD_FOLDER"]=UPLOAD_FOLDER

import base64
def save(username,image):
    decodeit = open("data/" + username+".jpeg", 'wb') 
    decodeit.write(base64.b64decode((image))) 
    decodeit.close()


mysql = MySQL(app)

@app.route('/login', methods=['POST', 'GET'])
def login():
    print("hello")
    if request.method == 'POST':
        username=request.form['username']
        print(username)
        s="/data/"+username+".jpeg"
        name = train(os.getcwd)
        print(name)
        if name==s:
            print(name)
            return redirect(f'/signup')
            
    
    return render_template('login.html')

@app.route('/signup', methods=['POST', 'GET'])
def signup():
    name=" "
    email=" "
    password=" "
    dob=" "
    username=" "
    gender=" "
    image=" "
    if request.method == 'POST':
        name=request.form['name']
        image=request.form['image']
        email=request.form['email']
        password=request.form['password']
        dob=request.form['dob']
        username=request.form['username']
        gender=request.form['gender']
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO users(name,email,username,password,dob,gender) VALUES(%s,%s,%s,%s,%s,%s)", (name, email,username,password,dob,gender))
        mysql.connection.commit()
        cur.close()
        l=image.split(",")
        save(username,l[1])
        print(name,email,password,dob,username,gender,"image",image)

    # name = train(os.getcwd)
    # print(name)
    return render_template('signup.html')

@app.route('/ocr', methods=['POST', 'GET'])
def ocr():
    if request.method=="POST":
        uploaded_file = request.files['front']

        if uploaded_file.filename != '':
            uploaded_file.save(uploaded_file.filename)
    return render_template('upload.html')

if __name__ == '__main__': 
  
    # run() method of Flask class runs the application  
    # on the local development server. 
    app.run()