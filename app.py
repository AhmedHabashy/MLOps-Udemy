from flask import Flask #WSGI Application
from flask import render_template #responsible for redirecting to the html page

'''
It creates an instance of Flask class,
which will be our WSGI(Web Server Gateway Interface) application.
'''

# WSGI application
app = Flask(__name__)

@app.route('/')
def welcome():
    return "welcome to MLOps-Udemy. This course should be Great!"

@app.route('/index')
def index():
    return "Welcome to MLOps-Udemy Index. This course should be Great!"



if __name__ == '__main__':
    app.run(debug=True)