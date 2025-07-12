from flask import Flask, render_template
import random
import datetime as dt
import requests

app = Flask(__name__)
CURRENT_YEAR = dt.datetime.now().year

@app.route('/')
def home():
    random_number = random.randint(1, 10)
    return render_template('index.html', num = random_number, copy_year=CURRENT_YEAR)

@app.route('/guess/<name>')
def guess(name):
    url = f"https://api.genderize.io/?name={name}"
    response = requests.get(url)
    data_gender = response.json().get('gender')
    url = f"https://api.agify.io/?name={name}"
    response = requests.get(url)
    data_age = response.json().get('age')
    data = {
        'name': name,
        'gender': data_gender,
        'age': data_age
    }
    return render_template('guess.html', data=data, copy_year=CURRENT_YEAR)

@app.route('/blog/<int:post_id>')
def get_blog(post_id):
    url = "https://api.npoint.io/308fff4c8c069fd8cd54"
    response = requests.get(url)
    blog_data = response.json()
    return render_template('blog.html', posts=blog_data, copy_year=CURRENT_YEAR, post_id=post_id)

if __name__ == "__main__":
    app.run(debug=True)
