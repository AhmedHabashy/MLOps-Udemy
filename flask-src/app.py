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
    return render_template('index.html')

@app.route('/about')
def index():
    return render_template('about.html')


if __name__ == '__main__':
    app.run(debug=True)