

from flask import Flask, render_template, jsonify
import requests
import json
from flask import Flask, render_template, redirect, url_for, request, session
app = Flask(__name__)
 
@app.route('/hospital')
def hospital():
    data1 = request.args.get('data')
    return render_template('hospitals.html',data=data1)

@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        city = request.form['city']
        print(city)
        session['city'] = city
        return redirect(url_for('hospital',city=city))
    return render_template('hospital_form.html')
 


@app.route('/hospitals', methods=['POST', 'GET'])
def hospitals():
    city_name = session['city']
    url = "http://indian-hospital.herokuapp.com/api/v1/hospitals/?city="+city_name+"&format=json"
    req = requests.get(url)
    print("Data",req.json())
    data = {
    "data": req.json()
    }
    return jsonify(data)
    



 
if __name__ == '__main__':

    app.secret_key = 'super secret key'
    app.config['SESSION_TYPE'] = 'filesystem'

    
    app.run()

