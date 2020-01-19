from peewee import *
from playhouse.sqlite_ext import *

usersDB = SqliteDatabase("User.db")

class User(Model):
    username = CharField(unique=True)
    id = AutoField()
    schedule = JSONField()

    class Meta:
        database = usersDB

class Match(Model):
    user = ForeignKeyField(User, backref='matches')
    match = ForeignKeyField(User, backref='matchers')
    class Meta:
        database = usersDB

class Picture(Model):
    id = AutoField()
    hash = CharField(unique=True)
    user = ForeignKeyField(User, backref='pictures')

    class Meta:
        database = usersDB


def addMatch(user, other):
    newMatch = Match(user=user, match=other)
    newMatch.create()


if __name__ == "__main__":
    # usersDB.create_tables([Picture])
    # usersDB.create_tables([Match])
    pass
