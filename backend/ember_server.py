from flask import Flask, jsonify, request
import datetime
from peewee import *
from playhouse.sqlite_ext import *
import os
import hashlib
from DatabaseManager import User, Picture, Match
from playhouse.shortcuts import model_to_dict, dict_to_model

app = Flask(__name__, static_folder="./static", static_url_path='/static')
app.config['SECRET_KEY'] = 'lit_haxx3rs'
app.config['JWT_EXPIRATION_DELTA'] = datetime.timedelta(
    seconds=60 * 1000)  # Have the token last for ever
app.debug = True


# Gives the available swypes
@app.route("/available_matches")
def query_matches():
    return {"people": [
        {"name": "Lisa", "score": 0.8}
    ]}

# People who both swyped right and time tables align
@app.route("/matched")
def get_matched():
    return {"people": [
        {"name": "Lisa", "score": 0.7}
    ]}

# Swyped right to that person
@app.route("/match")
def match():
    return {"msg": "ok"}

# Swyped left to that person
@app.route("/nope")
def nope():
    return {"msg": "ok"}

# Get available rooms/library spaces for a time frame.
@app.route("/rooms")
def available_spaces():
    return {"rooms": [
        {"name": "room1", "location": "building1"}
    ]}

# Upload a photo of yourself
# curl -F 'file=@README.md' http://127.0.0.1:8080/upload_photo/1
@app.route("/upload_photo/<int:id>", methods=['POST'])
def upload(id):
    if 'file' not in request.files:
        return {"msg": "err", "error": "No file part"}

    file = request.files['file']
    if file.filename == '':
        return {"msg": "err", "error": "No selected file"}

    new_filename = str(hashlib.sha1(file.read()).hexdigest())
    # TODO: Save the picture in the db
    user = User.get(User.id == id)
    Picture.create(user=user, hash=new_filename)

    file.save(os.path.join("./static/", new_filename))
    return {"msg": "ok"}

# User photos
@app.route("/photos/<int:id>")
def photo_list(id):
    hashes = ["/static/" +
              picture.hash for picture in User.get(User.id == id).pictures]
    return {"photos": [
        hashes
    ]}


@app.route("/users")
def get_users():
    users = User.select()
    pictures = Picture.select()
    matches = Match.select()

    # This will perform two queries.
    combo = prefetch(users, pictures)
    return {"users": [
        [ model_to_dict(user, backrefs=True)  for user in combo ]
    ]}

# Store OAuth tokens as a dictionary linked to user id


if __name__ == "__main__":
    app.run(debug=True, port=8080)
OAuth = {}
