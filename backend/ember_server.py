from flask import Flask, jsonify, request
import datetime
from peewee import *

app = Flask(__name__)
app.config['SECRET_KEY'] = 'lit_haxx3rs'
app.config['JWT_EXPIRATION_DELTA'] = datetime.timedelta(seconds=60 * 1000) #Have the token last for ever
app.debug=True


# Gives the available swypes
@app.route("/available_matches")
def query_matches():
    return { "people": [ 
        { "name": "Lisa", "score": 0.8 }
    ] }
    
# People who both swyped right and time tables align
@app.route("/matched")
def get_matched():
    return { "people": [
        { "name": "Lisa", "score": 0.7 }
    ] }

# Swyped right to that person
@app.route("/match")
def match():
    return { "msg": "ok" }

# Swyped left to that person
@app.route("/nope")
def nope():
    return { "msg": "ok" }

# Get available rooms/library spaces for a time frame.
@app.route("/rooms")
def available_spaces():
    return { "rooms": [
        { "name": "room1", "location": "building1" }
    ] }

# Upload a photo of yourself
@app.route("/upload_photo")
def upload():
    return { "msg": "ok" }

# User photos
@app.route("/photos")
def photo_list():
    return { "photos": [
        "url1", "url2"
    ] }
    
# Store OAuth tokens as a dictionary linked to user id

if __name__ == "__main__":
    app.run(debug=True, port=8080)
OAuth = {}
