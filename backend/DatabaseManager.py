from peewee import *
from playhouse.sqlite_ext import *

usersDB = SqliteDatabase("User.db")

class User(Model):
    username = CharField(unique=True)
    id = AutoField()
    schedule = JSONField()

    class Meta:
        database = usersDB
