from peewee import *
from playhouse.sqlite_ext import *
from DatabaseManager import User
import json
from datetime import  date, datetime, time, timedelta

# given a user, figure out who has a similar schedule, and possible meeting times

def getFreeTime(schedule):
    # given a schedule, return an array of free hours during the week
    freeHours = []
    for i in schedule:
        dayHours = []
        for hour in [(datetime.combine(date.today(),time(hour=9)) + timedelta(minutes=30) +timedelta(hours=1) * i).time() for i in range(0,9)]:
            for event in i[1]:
                if event[0] < hour and event[1] > hour:
                    break
            else:
                dayHours.append(hour)
        freeHours.append(dayHours)
    return freeHours

def matchSchedule(s1,s2):
    free1 = getFreeTime(s1)
    free2 = getFreeTime(s2)

    combinedFree = [list(set([j.isoformat() for j in free1[i]]) & set([j.isoformat() for j in free2[i]])) for i in range(0, len(free1))]
    return sum([len(i) for i in combinedFree]) / sum([len(i) for i in free1])

def matchSchedules(id):
    mySchedule = json.loads(User.get(id=id).schedule)["timetable"] #User's schedule
    otherSchedules = [[i.username, json.loads(i.schedule)["timetable"]] for i in User.select()]

    for other in otherSchedules:
        print("score for {}: {}".format(other[0], matchSchedule(mySchedule, other[1])))




def scheduleToArray(scheduleObj):
    result=[]
    for day, schedule in scheduleObj.items():
        block=[datetime.strptime(day, '%Y-%M-%d').date(), []]
        for event in schedule:
            block[1].append([datetime.strptime(event["start_time"],'%H:%M').time(), datetime.strptime(event["end_time"],'%H:%M').time(), event["module"]["name"]])
        result.append(block)
    return result

if __name__=="__main__":
    s1=scheduleToArray(json.loads(User.get(username="Bob").schedule)["timetable"])
    s2=scheduleToArray(json.loads(User.get(username="Bill").schedule)["timetable"])

    print(matchSchedules(1))
