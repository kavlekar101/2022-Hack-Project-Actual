from app import app
from flask import render_template
from flask import Flask, render_template, request, url_for, flash, redirect


@app.route('/')
@app.route('/index')
def index():
	return render_template('index.html')

messages = []
@app.route('/script', methods=('GET', 'POST'))
def script():
	if request.method == 'POST':
		building = request.form['building']
		day = request.form['day']
		startT = request.form['startT']
		endT = request.form['endT']
		if not building:
			flash('Title is required!')
		elif not day:
			flash('Content is required!')
		elif not startT:
			flash("Start Time is required!")
		elif not endT:
			flash("End Time is required!")
		else:
			messages.clear()
			messages.append({'building': building, 'day': day, 'startT': startT, 'endT': endT})
			print(messages)

			return redirect(url_for('script'))

		

	return render_template('script.html')
