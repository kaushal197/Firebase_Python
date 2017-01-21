#import flask and pyrebase for firebase
from flask import Flask, jsonify
import pyrebase

#Add firebase config
config = {
    "apiKey": "AIzaSyDPxaPjaztIPoI_Hb6YiDGv8KXWkwoHHz8",
    "authDomain": "doggone-8d332.firebaseapp.com",
    "databaseURL": "https://doggone-8d332.firebaseio.com",
    "storageBucket": "doggone-8d332.appspot.com"
  }

#initialize firebase with config and pyrebase
firebase = pyrebase.initialize_app(config)

#create db object
db = firebase.database()

app = Flask(__name__)


#index page
@app.route('/')
def index():
    print(db)
    return 'ass'

#Data page
@app.route('/data')
def names():
    data = {"names": ["John", "Jacob", "Julie", "Jennifer"]}
    return jsonify(data)


if __name__ == '__main__':
    app.run()
