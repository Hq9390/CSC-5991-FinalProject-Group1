from flask import Flask, request, render_template, session, abort, flash
import json
import os
import pymongo
from bson.json_util import dumps, loads

mongo_client = pymongo.MongoClient('mongodb://db:27017/')
mongo_db = mongo_client['w_books']
ratings = mongo_db['rating']

app = Flask(__name__)

@app.route("/addRating", methods=['POST'])
def recently_added_list():
    result = ratings.insert_one({
        'ISBN': request.form['ISBN'],
        'reviewer': request.form['review']
    }).inserted_id

    reviewRecord = ratings.find_one(result)
    return dumps(reviewRecord)

@app.route('/ratings/isbn/<ISBN>', methods=['GET'])
def book_info(isbn):
    book_data = ratings.find({"ISBN": isbn})
    return dumps(book_data)



if __name__ == '__main__':
    #app.secret_key = os.urandom(12)   #needed?
    app.run(host='0.0.0.0', port=5009)
