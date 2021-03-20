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

@app.route('/', methods=['POST', 'GET'])
def home():
    print("hello")

    name = train(os.getcwd)
    print(name)
    return render_template('test.html')

if __name__ == '__main__': 
  
    # run() method of Flask class runs the application  
    # on the local development server. 
    app.run()