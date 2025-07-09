from flask import Flask, render_template
import random
import datetime as dt
import requests
import json

app = Flask(__name__)

@app.route('/')
def home():
    random_number = random.randint(1, 10)
    current_year = dt.datetime.now().year
    return render_template('index.html', num = random_number, copy_year=current_year)

@app.route('/guess/<name>')
def guess(name):
    url = f"https://api.genderize.io/?name={name}"
    response = requests.get(url)
    data_gender = response.json().get('gender')
    url = f"https://api.agify.io/?name=audric"
    response = requests.get(url)
    data_age = response.json().get('age')
    data = {
        'name': name,
        'gender': data_gender,
        'age': data_age
    }
    return render_template('guess.html', data=data)

if __name__ == "__main__":
    app.run(debug=True)
