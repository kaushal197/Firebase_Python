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
    #data = {"id": "1", "type": "found", "breed": "", "location": "Toronto"}
    #db.push(data)
    all_data = db.get()
    data = []
    for piece in all_data.each():
        data.append(piece.key())
        data.append(piece.val())
    return print(data)
#
#Data page
@app.route('/data')
def names():
    data = {"names": ["John", "Jacob", "Julie", "Jennifer"]}
    return jsonify(data)


if __name__ == '__main__':
    app.run()
