import pandas as pd
import os
from datetime import timedelta
from config import basedir

data = pd.read_csv(os.path.join(basedir,"app/data/sfpd_dispatch_data_subset.csv"), low_memory=False)

indices = data.index.get_values()
callTypeCount = {}
watchDateCount = {}
timeDiffs = {
        "received-entry": [],
        "entry-dispatch": [],
        "dispatch-response": [],
        "response-on_scene": [],
        "on_scene-transport": [],
        "transport-hospital": []
    }

for i in indices:
    currentType = data.loc[i,:].values[3]
    if currentType in callTypeCount:
        callTypeCount[currentType] += 1
    else:
        if not pd.isnull(currentType):
            callTypeCount[currentType] = 1

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
