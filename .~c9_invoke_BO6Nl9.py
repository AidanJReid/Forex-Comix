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
    return render_template('index.html')
    
@app.route('/learner')
def learner():
    return render_template('learner.html', page_title='Learner')
    
@app.route('/bookseller')
def bookseller():
    return render_template('bookseller.html', page_title='Bookseller')

@app.route('/school')
def school():
    return render_template('school.html', page_title='School')

@app.route('/login')
def login():
    return render_template('login.html', page_title='Login')
    
@app.route('/addcomic')
def addcomic():
    return render_template('addcomic.html', page_title='Add Comic', 
    languages=mongo.db.Languages.find(),
    condition=mongo.db.conditions.find(),
    genre=mongo.db.genre.find(),
    owner=mongo.db.owner.find())
    
@app.route('/insert_comic', methods=['POST'])
def insert_comic():
    DBComix = mongo.db.DBComix
    DBComix.insert_one(request.form.to_dict())
    return redirect(url_for('database'))
    
@app.route('/database', methods=['GET'])
def database():
    return render_template('database.html', page_title='Database', DBComix=mongo.db.DBComix.find())
    
@app.route('/database/<comic_title>', methods=['GET'])
def database_comic(comic_title):
    return render_template('comic.html', DBComix=mongo.db.DBComix.find_one())
    
@app.route('/edit_comic/<DBComix_id>')
def edit_comic(DBComix_id):
    the_comic = mongo.db.DBComix.find_one({"_id": ObjectId(DBComix_id)})
    all_comics = mongo.db.language.find(), mongo.db.genre.find(), mongo.db.condition.find(), mongo.db.owner.find()
    return render_template('editcomic.html',
        comic=the_comic, language=all_comics, condition=all_comics, owner=all_comics, page_title='Edit Comic')


@app.route('/delete_comic/<DBComix_id>')
def delete_comic(DBComix_id):
    mongo.db.DBComix.remove({'_id': ObjectId(DBComix_id)})
    return redirect(url_for('database'))
                
if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)
            
# Debug=true should be removed on submission!