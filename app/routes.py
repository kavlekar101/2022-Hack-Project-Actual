from app import app
from flask import render_template
from flask import Flask, request, render_template

@app.route('/')
@app.route('/index')
def index():
	return render_template('index.html')

@app.route('/', methods =["GET", "POST"])
def gfg():
    if request.method == "POST":
       # getting input with name = fname in HTML form
       first_name = request.form.get("fname")
       # getting input with name = lname in HTML form
       last_name = request.form.get("lname")
       return "Your name is "+first_name + last_name
    return render_template("form.html")
 
if __name__=='__main__':
   app.run()