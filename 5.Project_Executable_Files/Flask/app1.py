from flask import Flask, render_template, request  
import numpy as np
import pandas as pd
import os
import pickle

app = Flask(__name__)  

@app.route('/')
def home():
    return render_template('home.html') 

@app.route('/predict', methods=['POST', 'GET'])
def index():
    return render_template("index.html")

@app.route('/submit', methods=['POST', 'GET'])
def submit():
    age = request.form['age']
    gender = request.form['gender']
    tb = request.form['tb']
    db = request.form['db']
    ap = request.form['ap']
    aa1 = request.form['aa1']
    aa2 = request.form['aa2']
    tp = request.form['tp']
    a = request.form['a']
    agr = request.form['agr']
    
    data = [[float(age), float(gender), float(tb), float(db), float(ap), float(aa1), float(aa2), float(tp), float(a), float(agr)]]
    
    model = pickle.load(open(r'C:\Users\hp\Downloads\Smartinternz_project\liver_analysis (1).pk1', 'rb')) 
    scale = pickle.load(open(r'C:\Users\hp\Downloads\Smartinternz_project\scaling (1).pkl', 'rb'))
    scaled_data = scale.transform(data)
    prediction= model.predict(scaled_data)[0]

    if prediction == 1:
        return render_template('chance.html', prediction='You have a liver disease problem, consult a doctor !!!.')
    elif prediction == 2:
        return render_template('chance1.html', prediction='You do not have a liver disease problem \U0001f600 !')

if __name__=='__main__':  
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=False)