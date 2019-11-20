import os
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")
    
@app.route('/learner')
def learner():
    return render_template("learner.html")
    
@app.route('/seller')
def seller():
    return render_template("seller.html")

@app.route('/school')
def school():
    return render_template("school.html")

@app.route('/login')
def login():
    return render_template("login.html")
    
@app.route('/database')
def database():
    return render_template("database.html")
    
@app.route('/contact')
def contact():
    return render_template("contact.html")
    
if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)
            
# Debug=true should be removed on submission!