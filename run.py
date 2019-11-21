import os
import json
from flask import Flask, render_template, request, flash

app = Flask(__name__)
app.secret_key = 'something_stupid'

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
    
@app.route('/database')
def database():
    data = []
    with open("data/comics.json","r") as json_data:
        data = json.load(json_data)
    return render_template("database.html", page_title="Database", comics=data)
    
@app.route('/database/<comic_title>')
def database_comic(comic_title):
    comic = {}
    
    with open("data/comics.json", "r") as json_data:
        data = json.load(json_data)
        for obj in data:
            if obj["url"] == comic_title:
                comic = obj
                
    return render_template("comic.html", comic=comic)
                
    
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