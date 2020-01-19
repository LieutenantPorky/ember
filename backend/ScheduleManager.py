from peewee import *
from playhouse.sqlite_ext import *
from DatabaseManager import User
import json
from datetime import  date, datetime, time, timedelta
import requests


def scheduleToArray(scheduleObj): #Transform a schedule dict to a nicer-to-read array
    result=[]
    for day, schedule in scheduleObj.items():
        block=[datetime.strptime(day, '%Y-%M-%d').date(), []]
        for event in schedule:
            block[1].append([datetime.strptime(event["start_time"],'%H:%M').time(), datetime.strptime(event["end_time"],'%H:%M').time(), event["module"]["name"]])
        result.append(block)
    return result


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
                dayHours.append((datetime.combine(date.today(), hour) - timedelta(minutes=30)).time())
        freeHours.append(dayHours)
    return freeHours

def matchSchedule(s1,s2): # calculate compatibility between two schedules
    free1 = getFreeTime(s1)
    free2 = getFreeTime(s2)

    combinedFree = [list(set([j.isoformat() for j in free1[i]]) & set([j.isoformat() for j in free2[i]])) for i in range(0, len(free1))]
    return sum([len(i) for i in combinedFree]) / sum([len(i) for i in free1])

def matchSchedules(id): # given a User id, return compatibility with other schedules
    mySchedule = scheduleToArray(json.loads(User.get(id=id).schedule)["timetable"]) #User's schedule
    otherSchedules = [[i, scheduleToArray(json.loads(i.schedule)["timetable"])] for i in User.select()]

    return sorted([[other[0], matchSchedule(mySchedule, other[1])] for other in otherSchedules], key = lambda x : x[1])


def getDateTimes(s1,s2):
    free1 = getFreeTime(s1)
    free2 = getFreeTime(s2)

    combinedFree = [list(set([j.isoformat() for j in free1[i]]) & set([j.isoformat() for j in free2[i]])) for i in range(0, len(free1))]

    return [[datetime.strptime(d,'%H:%M:%S').time() for d in t] for t in combinedFree]




def getFreeRooms(timeSlots):
    #First, figure out which day of the week it is
    weekDay = datetime.today().weekday()
    current_best = None
    current_score = 0
    current_time = None
    #Give preference to smaller places? (more cozy)
    for i in [min(weekDay,5)%5, (min(weekDay,5)%5 + 1)%5]:
        delta = 0
        while (weekDay + delta) % 7 != i:
            delta += 1
        possible_rooms = []
        for t in timeSlots[i]:
            t = datetime.strptime(t,'%H:%M:%S').time()
            params = {
              "token": "uclapi-18eefea61aa8f4b-3ee8f19755065c5-4531c2d5bd84479-d325162d470dda7",
              "start_datetime": (datetime.combine(date.today(), t) + timedelta(days=delta)).isoformat(),
              "end_datetime": (datetime.combine(date.today(), t) + timedelta(days=delta, hours=1)).isoformat()
            }
            if datetime.now().time() < t or i > 0:
                r = requests.get("https://uclapi.com/roombookings/freerooms", params=params)
                result = r.json()["free_rooms"]
                for room in result:
                    if room["classification"] == "SS":
                        score = (10 + weekDay - i) * 10
                        score += t.hour * 5
                        score *= 10/(10 + int(room["capacity"]))
                        print(score)
                        if score > current_score:
                            current_best = room
                            current_score = score
                            current_time = datetime.combine(date.today(), t) + timedelta(days=delta)

    return current_best, current_time

def getARoom(u1, u2):
    s1 = scheduleToArray(json.loads(u1.schedule)["timetable"])
    s2 = scheduleToArray(json.loads(u2.schedule)["timetable"])
    print(s1)
    free1 = getFreeTime(s1)
    free2 = getFreeTime(s2)
    combinedFree = [list(set([j.isoformat() for j in free1[i]]) & set([j.isoformat() for j in free2[i]])) for i in range(0, len(free1))]

    place, time = getFreeRooms(combinedFree)

    return[time, place]




if __name__=="__main__":
    s1=scheduleToArray(json.loads(User.get(username="Bob").schedule)["timetable"])
    s2=scheduleToArray(json.loads(User.get(username="Bill").schedule)["timetable"])

    print(getFreeRooms(getDateTimes(s1,s2)))
