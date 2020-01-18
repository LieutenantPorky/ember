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


randSchedule = {"timetable":{}}

for day in week:
    daySchedule = [{"start_time":i[0], "end_time":i[1], "module":{"name":i[2]}} for i in randClasses if np.random.random() > 0.5]
    randSchedule["timetable"][day.isoformat()] = daySchedule

print(json.dumps(randSchedule, sort_keys=True, indent=4))
