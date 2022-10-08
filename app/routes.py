from app import app
from flask import Flask, redirect, url_for, render_template, session
from flask_wtf import FlaskForm
from wtforms.fields import DateField
from wtforms.validators import DataRequired
from wtforms import validators, SubmitField
from flask import render_template
from flask import Flask, render_template, request, url_for, flash, redirect
import WebScrape
import time

@app.route('/')
@app.route('/index')
def index():
	return render_template('index.html')


class InfoForm(FlaskForm):
	startdate = DateField('Start Date', format='%Y-%m-%d', validators=(validators.DataRequired(),))
	submit = SubmitField('Submit')


@app.route('/script', methods=('GET', 'POST'))
def script():
	form = InfoForm()
	if form.validate_on_submit():
		building = request.form['building']
		startT = request.form['appt1']
		endT = request.form['appt2']
		day = str(form.startdate.data.month) + "/" + str(form.startdate.data.day) + "/" + str(form.startdate.data.year)
		WebScrape.test(building, day, startT, endT)
		return redirect(url_for('script'))
	return render_template('script.html', form=form)


	
