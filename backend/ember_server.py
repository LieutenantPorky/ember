from flask import Flask, jsonify, request
import datetime
from peewee import *
from playhouse.sqlite_ext import *
import os
import hashlib
from DatabaseManager import User, Picture, Match, addMatch, getMatched
from ScheduleManager import matchSchedules
from playhouse.shortcuts import model_to_dict, dict_to_model
import json

app = Flask(__name__, static_folder="./static", static_url_path='/static')
app.debug = True
# Store OAuth tokens as a dictionary linked to user id

OAuth = {}

@app.route('/',methods=['POST'])
def kek():
    print(request.data)
    return "hello"

@app.route('/swiped')
def swiped():
    user = User.get(username=request.json["username"])
    match = User.get(id=request.json["other"])
    addMatch(user, match)


@app.route('/soulmate',methods=['POST'])
def getSoulMate():
    print(request.data)
    user = User.get(username=json.loads(request.data)["username"])
    return jsonify([[i[0],model_to_dict(i[1], backrefs=True)] for i in matchSchedules(user.id)])


# People who both swyped right and time tables align
@app.route("/matched")
def get_matched():
    user = User.get(username=request.json["username"])
    return [model_to_dict(i) for i in getMatched(user)]

# Photo upload
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
    return {"msg": "ok", "value": new_filename}

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
