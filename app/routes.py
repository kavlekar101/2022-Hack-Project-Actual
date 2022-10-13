from app import app
from flask import Flask, redirect, url_for, render_template, session, jsonify
from flask_wtf import FlaskForm
from wtforms.fields import DateField
from wtforms.validators import DataRequired
from wtforms import validators, SubmitField
from flask import render_template
from flask import Flask, render_template, request, url_for, flash, redirect
import WebScrape
import time
import os, json
import socket
import requests


class InfoForm(FlaskForm):
	startdate = DateField('Start Date', format='%Y-%m-%d', validators=(validators.DataRequired(),))
	submit = SubmitField('Submit')


@app.route('/', methods=('GET', 'POST'))
def base():
	form = InfoForm()
	results = []
	buildings = ['BE', 'DL', 'CL', 'AA']
	response = requests.get('http://ipinfo.io/loc')
	lat, lng = response.content.decode("utf-8").split(",")

	print(lng[:len(lng)-1])
	
	if form.validate_on_submit():
		building = request.form['building']
		startT = request.form['appt1']
		endT = request.form['appt2']
		day = str(form.startdate.data.month) + "/" + str(form.startdate.data.day) + "/" + str(form.startdate.data.year)
		results = WebScrape.test(building, day, startT, endT)
	return render_template('base.html', form=form, buildings=buildings, lat=lat, lng=lng[:len(lng)-1])


	
