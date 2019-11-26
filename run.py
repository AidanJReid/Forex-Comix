import os

from flask import Flask, render_template, request, url_for, redirect, flash
from flask_pymongo import PyMongo
from bson.objectid import ObjectId

app = Flask(__name__)

app.config["MONGO_DBNAME"] = 'ForexComix'
app.config["MONGO_URI"] = 'mongodb+srv://natureboy:ttDFW9m3@myfirstcluster-fbekj.mongodb.net/ForexComix?retryWrites=true&w=majority'

mongo = PyMongo(app)

@app.route('/')
def index():
    return render_template("index.html")
    
@app.route('/learner')
def learner():
    return render_template("learner.html", page_title="Learner")
    
@app.route('/bookseller')
def bookseller():
    return render_template("bookseller.html", page_title="Bookseller")

@app.route('/school')
def school():
    return render_template("school.html", page_title="School")

@app.route('/login')
def login():
    return render_template("login.html", page_title="Login")
    
@app.route('/addcomic')
def addcomic():
    return render_template("addcomic.html", page_title="Add Comic")
    
@app.route('/database', methods=["GET", "POST"])
def database():
    return render_template("database.html", page_title="Database", DBComix=mongo.db.DBComix.find())
    
@app.route('/database/<comic_title>')
def database_comic(comic_title):
    return render_template("comic.html", DBComix=mongo.db.DBComix.find())
                
    
@app.route('/contact', methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        flash("Thanks {}, I got your message, loud and clear!".format(
              request.form["name"]))
    return render_template("contact.html", page_title="Contact")
    
if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)
            
# Debug=true should be removed on submission!