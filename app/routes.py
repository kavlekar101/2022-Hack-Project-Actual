from app import app
from flask import Flask, redirect, url_for, render_template, session, jsonify
from flask_wtf import FlaskForm
from wtforms.fields import DateField
from wtforms.validators import DataRequired
from wtforms import validators, SubmitField, TextAreaField
from flask import render_template, Response
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
	buildingMap = {'Agricultural Administration': 'AA', 
				'Agricultural Engineering Building': 'AE', 
				'Animal Science Building': 'AS', 
				'Arps Hall': 'AP', 
				'Baker Systems Engineering': 'BE', 
				'Bolz Hall': 'BO', 
				'Caldwell Laboratory': 'CL', 
				'Campbell Hall': 'CM', 'CBEC': 
				'CB', 
				'Cockins Hall': 'CH', 
				'Cunz Hall': 'CZ', 
				'Denney Hall': 'DE', 
				'Derby Hall': 'DB', 
				'Dreese Laboratories': 'DL', 
				'Dulles Hall': 'DU', 
				'Enarson Classroom Building': 'EC', 
				'Evans Laboratory': 'EL', 
				'Fontana Laboratories': 'FL', 
				'Hagerty Hall': 'HH', 
				'Hayes Hall': 'HA', 
				'Hitchcock Hall': 'HI', 
				'Hopkins Hall': 'HC', 
				'Independence Hall': 'IH', 
				'Jennings Hall': 'JE', 
				'Journalism Building': 'JR', 
				'Knowlton Hall': 'KN', 
				'Kottman Hall': 'KH', 
				'Lazenby Hall': 'LZ', 
				'McPherson Chemical Laboratory': 'MP', 
				'Orton Hall': 'OR', 
				'Page Hall': 'PA', 
				'Parks Hall': 'PK', 
				'Physical Activity and Education Services - PAES': 'PE', 
				'Pomerene Hall': 'PO', 
				'Psychology Building': 'PS', 
				'Ramseyer Hall': 'RA', 
				'Schoenbaum Hall': 'SB', 
				'Scott Laboratory': 'SO', 
				'Smith Laboratory': 'SM', 
				'Stillman Hall': 'SH', 
				'Sullivant Hall': 'SU', 
				'Townshend Hall': 'TO', 
				'University Hall': 'UH'}
	response = requests.get('http://ipinfo.io/loc')
	lat, lng = response.content.decode("utf-8").split(",")

	# print(lng[:len(lng)-1])
	
	if form.validate_on_submit():
		building = buildingMap[request.form['buildingnames']]
		startT = request.form['appt1']
		endT = request.form['appt2']
		day = str(form.startdate.data.month) + "/" + str(form.startdate.data.day) + "/" + str(form.startdate.data.year)
		results = WebScrape.test(building, day, startT, endT)
	return render_template('base.html', form=form, buildings=buildingMap.keys(), results=results, lat=lat, lng=lng[:len(lng)-1])


	
