from flask import Flask, jsonify, request, send_file
import datetime
from DatabaseManager import User
from ScheduleManager import matchSchedules
from peewee import *

app = Flask(__name__)
app.debug=True

# Store OAuth tokens as a dictionary linked to user id

OAuth = {}

@app.route('/')
def kek():
    return "kek"


@app.route('/soulmate')
def getSoulMate():
    User = User.get(username=request.json["username"])
    return jsonify(matchSchedules(User.id))

@app.route('/pictures/<int:user_id>/<int:picture_id>')    #int has been used as a filter that only integer will be passed in the url otherwise it will give a 404 error
def serve_profile_pic(user_id, picture_id):
    return send_file("./profiles/{}_{}.png".format(user_id, picture_id))
