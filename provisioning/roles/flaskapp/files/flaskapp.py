import hashlib
from flask import Flask, request
from flask.ext.pymongo import PyMongo

# Initializing the Flask application
app = Flask(__name__)

# MongoDB configuration
app.config['MONGODB_db'] = 'testcase-flask'
app.config['MONGODB_HOST'] = 'localhost'
app.config['MONGODB_PORT'] = 27017
app.config['SECRET_KEY'] = 'somesecretkey'

# Initializing DB
mongo = PyMongo(app)

# POST endpoint
@app.route('/post', methods=['POST'])
def add_record():
    if request.method == 'POST':
        json = request.json
        uid = json["uid"]
        name = json["name"]
        date = json["date"]
        md5checksum = json["md5checksum"]

        m = hashlib.md5()
        m.update(uid + name + date)
        if m.hexdigest() == md5checksum:
            mongo.db.testcase.insert({ "uid":uid, "name":name, "date":date })
            return 'Record was successfully saved \n'
        else:
            return "MD5 checksum is not valid \n"

# GET endpoint
@app.route('/get', methods=['GET'])
def getInfo():
    if request.method == 'GET':
        json = request.json
        uid = json["uid"]
        date = json["date"]

        occurrences = mongo.db.testcase.find({ "uid": uid, "date":date }).count()
        return str(occurrences) + "\n"

# Run
if __name__ == '__main__':
    app.run(
        host = "localhost",
        port = 8080,
    )
