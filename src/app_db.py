"""
CS321
Project 3
Yixuan Qiu & Luhang Sun
Extension: Use a database along with Flask
"""

from flask import Flask, render_template, request, url_for, redirect
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
db = SQLAlchemy(app)

class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    content = db.Column(db.String(200), nullable=False)

@app.route('/', methods=['POST','GET'])
def index():
    if request.method == 'POST':
        return add()
    else:
        items = db.session.query(Todo).all()
        return render_template("index.html", title="Home", items=items)

def add():
    item = Todo(content=request.form['content'])
    db.session.add(item)
    db.session.commit()
    return redirect(url_for("index"))


@app.route('/remove/<int:id>')
def remove(id):
    db.session.query(Todo).filter_by(id=id).delete()
    db.session.commit()
    return redirect(url_for("index"))


if __name__ == "__main__":
    app.run(debug=True)
