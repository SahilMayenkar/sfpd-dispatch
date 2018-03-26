import pandas as pd
import os
from datetime import timedelta

basedir = os.path.abspath(os.path.dirname(__file__))
data = pd.read_csv(os.path.join(basedir,"data/sfpd_dispatch_data_subset.csv"), low_memory=False)

callTypeCounts = {}
watchDateCount = {}
timeDiffs = {
        "Data Entry": [],
        "Dispatch to Unit": [],
        "Unit Acknowledgement": [],
        "Arrive on Scene": [],
        "Begin Transport to Hospital": [],
        "Arrive at Hospital": []
    }
zipCodeTimes = {}

for i in data.index.get_values():
    currentType = data.loc[i,:].values[3]
    if currentType in callTypeCounts:
        callTypeCounts[currentType] += 1
    else:
        if not pd.isnull(currentType):
            callTypeCounts[currentType] = 1

    currentDate = data.loc[i,:].values[5]
    if currentDate in watchDateCount:
        watchDateCount[currentDate] += 1
    else:
        if not pd.isnull(currentDate):
            watchDateCount[currentDate] = 1
    
    for index, key in enumerate(timeDiffs):
        date1 = pd.to_datetime(data.loc[i,:].values[index+6])
        date2 = pd.to_datetime(data.loc[i,:].values[index+7])
        if not pd.isnull(date1) and not pd.isnull(date2):
            timeDiffs[key].append(date2-date1)

    currentZip = data.loc[i,:].values[17]
    date3 = pd.to_datetime(data.loc[i,:].values[9])
    date4 = pd.to_datetime(data.loc[i,:].values[10])
    if currentZip in zipCodeTimes and not pd.isnull(date3) and not pd.isnull(date4):
        zipCodeTimes[currentZip].append(date4-date3)
    else:
        if not pd.isnull(currentZip) and not pd.isnull(date3) and not pd.isnull(date4):
            zipCodeTimes[currentZip] = []
            zipCodeTimes[currentZip].append(date4-date3)

zipCodeAvgs = []

for key, value in zipCodeTimes.items():
    avgTime = (sum(value, timedelta()) / len(value)).total_seconds()/60
    zipCodeAvgs.append([key, avgTime])

zipCodeAvgs = sorted(zipCodeAvgs,key=lambda x:x[1], reverse=True)
zipCodeTops = []
for i in range(3):
    zipCodeTops.append(zipCodeAvgs[i])

avgDispatches = timeDiffs['Arrive on Scene']
avgDispatch = (sum(avgDispatches, timedelta()) / len(avgDispatches)).total_seconds() / 60

zipCodeTops.append(['Average', avgDispatch])
