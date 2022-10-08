from app import app
from flask import render_template
from flask import Flask, request, render_template

@app.route('/')
@app.route('/index')
def index():
	return render_template('index.html')

@app.route('/script')
def script():
	return render_template('script.html')
