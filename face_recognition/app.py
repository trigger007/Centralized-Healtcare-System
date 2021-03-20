from flask import Flask, render_template, redirect, url_for, request
import pandas as pd
import numpy as np
from scipy import stats
import logging
import datetime
import os.path
from flask import Markup


app=Flask(__name__)
app.config["DEBUG"]= True

@app.route('/', methods=['POST', 'GET'])
def home():
    print("hello")