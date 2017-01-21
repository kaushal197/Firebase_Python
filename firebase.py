#import flask and pyrebase for firebase
from flask import Flask, jsonify
import pyrebase

#Add firebase config
config = {
    "apiKey": "AIzaSyDPxaPjaztIPoI_Hb6YiDGv8KXWkwoHHz8",
    "authDomain": "doggone-8d332.firebaseapp.com",
    "databaseURL": "https://doggone-8d332.firebaseio.com",
    "storageBucket": "doggone-8d332.appspot.com",
    "messagingSenderId": "430271372447"
  }

#initialize firebase with config and pyrebase
firebase = pyrebase.initialize_app(config)

#create db object
db = firebase.database()

app = Flask(__name__)


#index page
@app.route('/')
def index():
    data = {"id": 1, "name": "", "breed_manual": "", "breed_auto": "", "last_location": ""}
    db.child('lost').push(data)
    data = db.get()
    return jsonify(str(data.val()))
#
#Data page
@app.route('/data')
def names():
    dataset = db.child('found').get().each()
    data = {}
    for piece in dataset:
        data[piece.key()] = piece.val()
    return str(data)


if __name__ == '__main__':
    app.run()
