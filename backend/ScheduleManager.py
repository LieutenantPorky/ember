from peewee import *
#from DatabaseManager import User
import json
from datetime import  date, datetime, time, timedelta

# given a user, figure out who has a similar schedule, and possible meeting times

def getFreeTime(schedule):
    # given a schedule, return an array of free hours during the week
    freeHours = []
    for i in schedule:
        dayHours = []
        for hour in [(datetime.combine(date.today(),time(hour=9)) + timedelta(minutes=30) +timedelta(hours=1) * i).time() for i in range(0,9)]:
            for event in i:
                if i[0] < hour and i[1] > hour:
                    break
            else:
                dayHours.append(hour)
        freeHours.append(freeHours)
    return freeHours

def matchSchedule(s1,s2):
    free1 = getFreeTime(s1)
    free2 = getFreeTime(s2)

    combinedFree = [list(set(free1[i]) & set(free2[i])) for i in range(0, len(free1))]

    return len(combinedFree) / len(free1)

def matchSchedules(id):
    mySchedule = json.loads(User.get(id=id).schedule) #User's schedule
    otherSchedules = [i.schedule for i in User.select()]




def scheduleToArray(scheduleObj):
    result=[]

    for day, schedule in scheduleObj:
        block=[date.fromisoformat(day), []]

        for event in schedule:
            block[1].append([time.fromisoformat(schedule["start_time"]), time.fromisoformat(schedule["end_time"]), schedule["module"]["name"]])

    return result
