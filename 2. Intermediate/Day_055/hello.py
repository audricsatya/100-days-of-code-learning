from flask import Flask

app = Flask(__name__)

def make_bold(function):
    def wrapper():
        return "<b>" + function() + "</b>"
    return wrapper

def make_emphasis(function):
    def wrapper():
        return "<em>" + function() + "</em>"
    return wrapper

def make_underlined(function):
    def wrapper():
        return "<u>" + function() + "</u>"
    return wrapper

@app.route('/')
def hello_world():
    return '<h1 style="text-align: center;">Hello, World!</h1>' \
           '<p>This is a simple Flask application.</p>' \
           '<img src="https://media.giphy.com/media/3o7aD22z4k3b7c5a8g/giphy.gif" width="300">'

@app.route('/username/<name>/<int:age>')
def greet_user(name, age):
    return f'Hello, {name}! You are {age} years old!'

@app.route('/bye')
@make_bold
@make_emphasis
@make_underlined
def say_bye():
    return 'Goodbye!'

if __name__ == '__main__':
    app.run(debug=True) 