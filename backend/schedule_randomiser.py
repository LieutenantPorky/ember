from peewee import *
from playhouse.sqlite_ext import *
import json
import numpy as np
from datetime import  date, datetime, time, timedelta

week = [date(day=20 + i,month=1,year=2020) for i in range(0,5)]

#[print(i.isoformat()) for i in week]

randClasses = [
["9:00", "10:00", "Intro to Minecraft"],
["11:00", "13:00", "Applied Numerology"],
["13:00", "14:00", "Physics of Kitties"],
["15:00", "17:00", "Computational Turbodynamics"],
["17:00", "18:00", "Pro Haxxing 101"],
]


def getRand():
    randSchedule = {"timetable":{}}

    for day in week:
        daySchedule = [{"start_time":i[0], "end_time":i[1], "module":{"name":i[2]}} for i in randClasses if np.random.random() > 0.5]
        randSchedule["timetable"][day.isoformat()] = daySchedule
    return randSchedule
#print(json.dumps(randSchedule, sort_keys=True, indent=4))
#print(json.dumps(randSchedule, sort_keys=True)




usersDB = SqliteDatabase("User.db")

class User(Model):
    username = CharField(unique=True)
    id = AutoField()
    schedule = JSONField()

    class Meta:
        database = usersDB

for i in User.select():
    print(i.username)
    print(i.schedule)
# usersDB.create_tables([User])
#
# for name in ["Bob", "Bill", "Jeb"]:
#     newUser = User(username=name,schedule=json.dumps(getRand()))
#     newUser.save()
