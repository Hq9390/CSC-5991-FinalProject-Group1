from flask import Flask, request, render_template, session, abort, flash
import os
import pymongo
from datetime import datetime
import json
from bson.json_util import dumps, loads

app = Flask(__name__)


@app.route('/return', methods=['POST'])
def returned():
    mongo_client = pymongo.MongoClient('mongodb://db:27017/')
    mongoDb = mongo_client['w_books']
    bookCollection = mongoDb['books_rentals']

    query = {
        'book_id': request.form['book_id'],
        'renter_name': request.form['renter_name']}
    updates = {"$set": {'is_returned': 1, 'return_date': datetime.now()}}

    bookCollection.update_one(query, updates)

    return dumps(bookCollection.find())


if __name__ == '__main__':
    app.secret_key = os.urandom(12)
    app.run(host='0.0.0.0', port=5007)
