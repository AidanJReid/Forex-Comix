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

@app.route('/addcomic')
def addcomic():
    return render_template('addcomic.html', page_title='Add Comic', 
    languages=mongo.db.Languages.find(),
    condition=mongo.db.condition.find(),
    genre=mongo.db.genre.find(),
    difficulty=mongo.db.difficulty.find(),
    description=mongo.db.description.find(),
    owner=mongo.db.owner.find())
    
@app.route('/insert_comic', methods=['POST'])
def insert_comic():
    DBComix = mongo.db.DBComix
    DBComix.insert_one(request.form.to_dict())
    return redirect(url_for('database'))
    
@app.route('/database', methods=['GET'])
def database():
    return render_template('database.html', page_title='Database', DBComix=mongo.db.DBComix.find())
    
@app.route('/get_comic/<DBComix_id>', methods=['GET'])
def get_comic(DBComix_id):
    get_comic=mongo.db.DBComix.find_one({'_id': ObjectId(DBComix_id)})
    print(get_comic)
    return render_template('comic.html', comic=get_comic)
    
@app.route('/edit_comic/<DBComix_id>')
def edit_comic(DBComix_id):
    the_comic = mongo.db.DBComix.find_one({'_id': ObjectId(DBComix_id)})
    all_languages = mongo.db.Languages.find() 
    all_genres = mongo.db.genre.find()
    all_difficulty = mongo.db.difficulty.find()
    all_condition = mongo.db.condition.find()
    all_description = mongo.db.description.find()
    return render_template('editcomic.html',
        comic=the_comic, languages=all_languages, genres=all_genres, difficulty = all_difficulty, condition = all_condition, description = all_description, 
        page_title='Edit Comic')

@app.route('/update_comic/<DBComix_id>', methods=['POST'])
def update_comic(DBComix_id):
    DBComix = mongo.db.DBComix
    DBComix.update({'_id': ObjectId(DBComix_id)},
    {
        'language': request.form.get('language'),
        'genre': request.form.get('genre'),
        'condition': request.form.get('condition'),
        'difficulty': request.form.get('difficulty'),
        'is_owner': request.form.get('is_owner'),
        'description': request.form.get('description'),
        'title': request.form.get('title'),
        'character': request.form.get('character'),
        'image_source': request.form.get('image_source')
    })
    return redirect(url_for('database'))

@app.route('/delete_comic/<DBComix_id>')
def delete_comic(DBComix_id):
    mongo.db.DBComix.remove({'_id': ObjectId(DBComix_id)})
    return redirect(url_for('database'))
                
if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)
            
# Debug=true should be removed on submission!