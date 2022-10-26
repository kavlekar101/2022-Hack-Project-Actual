from app import app
from flask import Flask, redirect, url_for, render_template, session, jsonify
from flask_wtf import FlaskForm
from wtforms.fields import DateField
from wtforms.validators import DataRequired
from wtforms import validators, SubmitField, TextAreaField
from flask import render_template, Response
from flask import Flask, render_template, request, url_for, flash, redirect
import WebScrape, GetMap
import time
import os, json
import socket
import re
import requests


class InfoForm(FlaskForm):
	startdate = DateField('Start Date', format='%Y-%m-%d', validators=(validators.DataRequired(),))
	submit = SubmitField('Submit')


@app.route('/', methods=('GET', 'POST'))
def base():
	form = InfoForm()
	results = []
	url = "https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3056.4107492069456!2d-83.01753292419441!3d39.999271771509825!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x88388e97cf3ebe3f%3A0xb53b7b3cbb455305!2sThompson%20Library!5e0!3m2!1sen!2sus!4v1666227706654!5m2!1sen!2sus"
	buildingMap = {'Agricultural Administration': 'AA', 
				'Agricultural Engineering Building': 'AE', 
				'Animal Science Building': 'AS', 
				'Arps Hall': 'AP', 
				'Baker Systems Engineering': 'BE', 
				'Bolz Hall': 'BO', 
				'Caldwell Laboratory': 'CL', 
				'Campbell Hall': 'CM', 
				'CBEC': 'CB', 
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
		building = request.form['buildingnames']
		startT = request.form['appt1']
		endT = request.form['appt2']
		day = str(form.startdate.data.month) + "/" + str(form.startdate.data.day) + "/" + str(form.startdate.data.year)
		results = WebScrape.test(buildingMap[building], day, startT, endT)
		url = GetMap.getInfo(building)[13:-132]
	return render_template('base.html', form=form, buildings=buildingMap.keys(), results=results, lat=lat, lng=lng[:len(lng)-1], url=url)


	
