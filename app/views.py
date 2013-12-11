from flask import render_template
from app import app


@app.route('/')
def home():
    result = {'ipaddress':'127.0.0.1','hostname':'localhost','proxypath':'localhost.thoughtworks.com'}
    return render_template('index.html', result=result)
