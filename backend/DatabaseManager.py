from peewee import *
from playhouse.sqlite_ext import *
import numpy as np

usersDB = SqliteDatabase("User.db")

class User(Model):
    username = CharField(unique=True)
    id = AutoField()
    schedule = JSONField()
    bio = TextField()

    class Meta:
        database = usersDB

class Match(Model):
    user = ForeignKeyField(User, backref='matches')
    match = ForeignKeyField(User, backref='matchers')
    class Meta:
        database = usersDB

class Picture(Model):
    id = AutoField()
    hash = CharField()
    user = ForeignKeyField(User, backref='pictures')

    class Meta:
        database = usersDB


def addMatch(user, other):
    newMatch = Match(user=user, match=other)
    newMatch.create()

def getMatched(user):
    good_matches = []
    for match in user.matches:
        if Match.get_or_none(user=match.match, match= user):
            good_matches.append(match.match)

    return good_matches

# if __name__ == "__main__":
#     # usersDB.create_tables([Picture])
#     for i in User.select():
#         # if i.username=="Mark the Zucc Zuccson":
#         #     profile= Picture(user=i, hash='zucc1.jpeg')
#         #     profile.save()
#         #     profile= Picture(user=i, hash='zucc2.jpeg')
#         #     profile.save()
#         #
#         # else:
#         #     profile= Picture(user=i, hash='{}.jpeg'.format(['a','b','c','d','e','f','g'][np.random.randint(7)]))
#         #     profile.save()
#     # usersDB.create_tables([Match])
#
#     pass
