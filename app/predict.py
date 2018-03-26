import pandas as pd
from math import sin, cos, asin, acos, radians
from datetime import datetime, time
from app.dataprocess import data, indices
import sys

def predict(latitude, longitude, timestr):
    inputTime = format_time(timestr)
    unitTypeCounts = {}
    for i in indices:
        currentLat = data.loc[i,:].values[34]
        currentLng = data.loc[i,:].values[35]
        if not (pd.isnull(currentLat) or pd.isnull(currentLng)):
            dist = dist_calc(latitude, longitude, currentLat, currentLng)
            if dist <= 1:
                currentDateTime = pd.to_datetime(data.loc[i,:].values[6])
                if not pd.isnull(currentDateTime):
                    if inputTime.hour > 21 and currentDateTime.hour < 2:
                        comparableDate = datetime(2018, 1, currentDateTime.day - 1,
                                                  inputTime.hour, inputTime.minute)                
                    elif inputTime.hour < 2 and currentDateTime.hour > 21:
                        comparableDate = datetime(2018, 1, currentDateTime.day + 1,
                                                  inputTime.hour, inputTime.minute)                
                    else:
                        comparableDate = datetime(2018, 1, currentDateTime.day,
                                                  inputTime.hour, inputTime.minute)
                    if (comparableDate - currentDateTime).days == 0:
                        if (comparableDate - currentDateTime).seconds // 3600 < 2:
                            currentUnitType = data.loc[i,:].values[27]
                            if currentUnitType in unitTypeCounts:
                                unitTypeCounts[currentUnitType] += 1
                            else:
                                if not pd.isnull(currentUnitType):
                                    unitTypeCounts[currentUnitType] = 1
                    elif (currentDateTime - comparableDate).days == 0:
                        if (currentDateTime - comparableDate).seconds // 3600 < 2:
                            currentUnitType = data.loc[i,:].values[27]
                            if currentUnitType in unitTypeCounts:
                                unitTypeCounts[currentUnitType] += 1
                            else:
                                if not pd.isnull(currentUnitType):
                                    unitTypeCounts[currentUnitType] = 1
    result = ''
    topCount = 0
    
    for key, value in unitTypeCounts.items():
        if value > topCount:
            topCount = value
            result = key
        elif value == topCount:
            result = result + ", " + key
    print(unitTypeCounts, file=sys.stderr)
    
    return result


def format_time(timestr):
    timestr = timestr.split( )
    timestr[0] = timestr[0].split(':')
    hour = int(timestr[0][0])
    if timestr[1] == 'PM' and hour < 12:
        hour = hour + 12
    elif timestr[1] == 'AM' and hour == 12:
        hour = 0
    hour = hour + 8
    if hour > 23:
        hour = hour - 24
    mins = int(timestr[0][1])
    return time(hour, mins)

def dist_calc(lat1, lng1, lat2, lng2):
    lat1 = radians(float(lat1))
    lng1 = radians(float(lng1))
    lat2 = radians(float(lat2))
    lng2 = radians(float(lng2))
    r = 3959
    dist = acos(sin(lat1) * sin(lat2) + cos(lat1) * cos(lat2) * cos(lng1 - lng2)) * r
    return dist
