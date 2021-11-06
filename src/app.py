'''
CS321
Project 3
Yixuan Qiu & Luhang Sun
'''

from flask import Flask, render_template, request, url_for, redirect
# from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)

to_do_list = []

@app.route("/")
def index():
	now = datetime.now()
	date_time = now.strftime("%m/%d/%Y, %H:%M")
	return render_template("base.html", 
							title="Home", 
							date_time=date_time,
							to_do_list=to_do_list)

@app.route("/about")
def about():
	return "A to-do app"

@app.route("/add", methods=["POST"])
def add():
	item = request.form.get("item")
	to_do_list.append(item)
	print(to_do_list[-1])

	return redirect(url_for("index"))

@app.route("/remove/<string:name>")
def remove(name):
	to_do_list.remove(name)
	return redirect(url_for("index"))



if __name__ == "__main__":
	app.run(debug=True) 