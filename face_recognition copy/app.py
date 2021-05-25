from flask import Flask, render_template, redirect, url_for, request, session
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
from flask import Flask, render_template, request
from chatterbot.trainers import ListTrainer
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

UPLOAD_FOLDER = 'static/uploads/'

app=Flask(__name__)
app.config["DEBUG"]= True
app.config['MYSQL_HOST'] = '127.0.0.1'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'tarp'
app.config["UPLOAD_FOLDER"]=UPLOAD_FOLDER
app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'




bot = ChatBot('Buddy', storage_adapter='chatterbot.storage.SQLStorageAdapter',
            database_uri='sqlite:///database.sqlite3_eng',logic_adapters = [
                 {
                     'import_path': 'chatterbot.logic.BestMatch',
                     'default_response': 'I am sorry, I do not understand. I am still learning. Please contact doctor from our chat window for further assistance.',
                     'maximum_similarity_threshold': 0.90
                 }
             ],
             read_only = True,
             preprocessors=['chatterbot.preprocessors.clean_whitespace',
'chatterbot.preprocessors.unescape_html',
'chatterbot.preprocessors.convert_to_ascii'])


import base64
def save(username,image):
    decodeit = open(os.path.dirname(os.path.realpath(__file__))+"/data/" + username+".jpeg", 'wb') 
    decodeit.write(base64.b64decode((image))) 
    decodeit.close()


mysql = MySQL(app)
@app.route('/', methods=['POST', 'GET'])
def homepage():
    return render_template('index-two.html')

@app.route('/home2',methods=['POST', 'GET'])
def homepage2():
    return render_template('index-three.html')

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
        session['fname'] = name
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
        return redirect(f'/ocr')

    # name = train(os.getcwd)
    # print(name)
    return render_template('signup.html')

@app.route('/ocr', methods=['POST', 'GET'])
def ocr():
    if request.method=="POST":
        uploaded_file = request.files['front']
        back_file = request.files['back']

        if uploaded_file.filename != '' and back_file.filename!='':
            uploaded_file.save(os.path.join(os.path.dirname(os.path.realpath(__file__)))+'/aadhar/'+uploaded_file.filename)
            back_file.save(os.path.join(os.path.dirname(os.path.realpath(__file__)))+'/aadhar/'+back_file.filename)
        
        from aadharcard import aadhar_card_front
        name , co, address, aadhar, gender, dob, region = aadhar_card_front((os.path.join(os.path.dirname(os.path.realpath(__file__)))+'/aadhar/'+uploaded_file.filename),
                                                                                (os.path.join(os.path.dirname(os.path.realpath(__file__)))+'/aadhar/'+back_file.filename))

        session['name'] = name
        session['father'] = co
        session['addr'] = address
        session['aadhar_num'] = aadhar
        session['gender'] = gender
        session['dob'] = dob
        print("Session-Name",name)
        
        return redirect(url_for('aadhaar',name = name,co = co,aadhar = aadhar,address = address,dob = dob))
        #return render_template('aadhaar.html',name = name)
    return render_template('ocr.html')

@app.route('/aadhaar', methods=["POST","GET"])
def aadhaar():
    str1="checking"
    name = request.args.get('name')
    if name==session['fname']:
        str1="login successful"
    else:
        str1="fail"  
    aadhar = request.args.get('aadhar')
    print(session['fname'],name)
    '''
    if request.method == 'POST':
        name = request.args.get('name')
        #name=request.form['name']
        co=request.form['co']
        aadhar=request.form['aadhar']
        address=request.form['address']
    '''
        
          
    return render_template('aadhaar.html',name = request.args.get('name'),co = request.args.get('co'),aadhar = request.args.get('aadhar'),address = request.args.get('address'),dob = request.args.get('dob'),str=str1)

@app.route('/prescription',methods=["POST","GET"])
def prescription():
    
    if request.method=="POST":
        uploaded_file = request.files['upload']
        if uploaded_file.filename != '':
            uploaded_file.save(os.path.join(os.path.dirname(os.path.realpath(__file__)))+'/prescriptions_upload/'+uploaded_file.filename)

        from prescription_ocr import prescriptionn
        Patient, doctor , date, medicine_list  = prescriptionn(os.path.join(os.path.dirname(os.path.realpath(__file__)))+'/prescriptions_upload/'+uploaded_file.filename)
        
        print("Patient Name- ",Patient)
        print("Doctor- ",doctor)
        print("Date- ",date)
        print("Medicine- List- ",medicine_list)


    return render_template('prescription.html')

@app.route("/chatbot")
def home():
    return render_template("chatbot.html")

@app.route("/get")
def get_bot_response():
    user_input = request.args.get('msg')
    return str(bot.get_response(user_input))


if __name__ == '__main__': 
  
    # run() method of Flask class runs the application  
    # on the local development server.
    # check commentg 
    #check
    app.run()
    