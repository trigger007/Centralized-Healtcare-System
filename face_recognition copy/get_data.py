# from flask import Flask, render_template, redirect, url_for, request, session
# import requests
# import json
# city = input("Enter Your City:")



# req = requests.get("http://indian-hospital.herokuapp.com/api/v1/hospitals/?city=Ranchi&format=json")
# url = "http://indian-hospital.herokuapp.com/api/v1/hospitals/?city="+city+"&format=json"
# req=requests.get(url)

# print(req.content)

# app=Flask(__name__)
# @app.route('/', methods=['POST', 'GET'])
# def index():
#     req = requests.get("http://indian-hospital.herokuapp.com/api/v1/hospitals/?city=Ranchi&format=json")
#     print(req.content)
#     return render_template('hello')

from flask import Flask, render_template, jsonify
import requests
import json
from flask import Flask, render_template, redirect, url_for, request, session
app = Flask(__name__)
 
@app.route('/index')
@app.route('/')
def index():
  return render_template('hospitals.html')
 
@app.route('/index_get_data')
def stuff():
  # Assume data comes from somewhere else

  req = requests.get("http://indian-hospital.herokuapp.com/api/v1/hospitals/?city=Mumbai&format=json")
  print("Data",req.json())


  data = {
    "data": req.json()
  }
  return jsonify(data)
 
 
if __name__ == '__main__':
  app.run()