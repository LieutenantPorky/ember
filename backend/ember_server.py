from flask import Flask, jsonify, request
import datetime
from peewee import *
from playhouse.sqlite_ext import *
import os
import hashlib
from DatabaseManager import User, Picture, Match, addMatch, getMatched
from ScheduleManager import matchSchedules, getARoom
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

@app.route('/swiped/<username>')
def swiped(username):
    user = User.get(username=username)
    match = User.get(id=request.args.get('id'))
    Match.create(user=user, match=match)
    return { "msg": "ok" }

@app.route('/soulmate/<username>')
def getSoulMate(username):
    user = User.get(username=username)
    return jsonify([[model_to_dict(i[0], backrefs=True),i[1]] for i in matchSchedules(user.id)])


# People who both swyped right and time tables align
@app.route("/matched/<username>")
def get_matched():
    user = User.get(username=username)
    return [model_to_dict(i) for i in getMatched(user)]

# curl -F 'file=@profiles/1_0.png' http://127.0.0.1:8080/upload_photo/1
# Photo upload
@app.route("/upload_photo/<int:id>", methods=['POST'])
def upload(id):
    if 'file' not in request.files:
        return {"msg": "err", "error": "No file part"}

    file = request.files['file']
    if file.filename == '':
        return {"msg": "err", "error": "No selected file"}

    content = file.read()
    new_filename = str(hashlib.sha1(content).hexdigest())
    # TODO: Save the picture in the db
    user = User.get(User.id == id)

    Picture.create(user=user, hash=new_filename)

    with open(os.path.join("./static/", new_filename), "wb") as image:
        image.write(content)

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
    combo = prefetch(users, pictures, matches)
    return {"users": [
        [ model_to_dict(user, backrefs=True)  for user in combo ]
    ]}



@app.route("/book/<int:id1>/<int:id2>")
def book(id1, id2):
    event = getARoom(User.get(id=id1), User.get(id=id2))

    return jsonify([event[0], "room number {} in {}".format(event[1]["roomid"], event[1]["roomname"])])


# Store OAuth tokens as a dictionary linked to user id


if __name__ == "__main__":
    app.run(debug=True, port=8080)
OAuth = {}
