from flask import Flask, jsonify, request
import datetime
from peewee import *
from playhouse.sqlite_ext import *

app = Flask(__name__)
app.config['SECRET_KEY'] = 'lit_haxx3rs'
app.config['JWT_EXPIRATION_DELTA'] = datetime.timedelta(seconds=60 * 1000) #Have the token last for ever
app.debug=True

# Store OAuth tokens as a dictionary linked to user id

OAuth = {}
