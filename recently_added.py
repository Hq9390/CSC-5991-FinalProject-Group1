from flask import Flask

import json
import os
import pymongo

# mongo_client = pymongo.MongoClient('mongodb://localhost:27017/')
# mongo_db = mongo_client['w_books']


app = Flask(__name__)

with open("../URL HERE") as f: #replace with db get 
    recently_added = json.load(f)

@app.route("/", methods=['GET'])
def hello():
    return json.dumps({
        "uri": "/",
        "subresource_uris": {
            "recently_added": "/recentlyAdded",
        }
    })


@app.route("/recentlyAdded", methods=['GET'])
def recently_added_list():
    return json.dumps(recently_added)


if __name__ == '__main__':
    #app.secret_key = os.urandom(12)   #needed?
    app.run(host='0.0.0.0', port=5000)
