from flask import Flask, request, render_template, session, abort, flash
import os
import pymongo
from datetime import datetime
import json
from bson.json_util import dumps, loads
from bson.objectid import ObjectId

app = Flask(__name__)


@app.route('/rent', methods=['POST'])
def topten():
    mongo_client = pymongo.MongoClient('mongodb://db:27017/')
    mongoDb = mongo_client['w_books']
    originalBooks = mongoDb['books']
    originalBooks.update_one({'_id': ObjectId(request.form['book_id'])}, {'$inc': {'rental_count':1}})
    bookCollection = mongoDb['books_rentals']
    result = bookCollection.insert_one({
        'book_id': request.form['book_id'],
        'renter_name': request.form['renter_name'],
        'rental_date': datetime.now(),
        'is_returned': 0,
        'return_date': 0
    }).inserted_id

    rentalRecord = bookCollection.find_one(result)
    return dumps(rentalRecord)


if __name__ == '__main__':
    app.secret_key = os.urandom(12)
    app.run(host='0.0.0.0', port=5006)
