from peewee import *
from playhouse.sqlite_ext import *

usersDB = SqliteDatabase("User.db")

class User(Model):
    username = CharField(unique=True)
    id = AutoField()
    schedule = JSONField()

    class Meta:
        database = usersDB

class Picture(Model):
    id = AutoField()
    hash = CharField(unique=True)
    user = ForeignKeyField(User, backref='pictures')

    class Meta:
        database = usersDB

if __name__ == "__main__":
    # usersDB.create_tables([Picture])
    pass