import json, os, sys
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime

data_path = '/home/dwilson/data/LocationHistory.json'
if not os.path.exists(data_path):
    print "LocationHistory.json not found at {0}".format(data_path)
    exit()

def loadData(lon0=-105.296,lon1=-104.612,lat0=39.460,lat1=39.889):
    with open(data_path,'r') as fp:
        data = json.load(fp)

    locations = data['locations']

    N = len(locations)

    locs = [(x['longitudeE7']*1e-7,x['latitudeE7']*1e-7) for x in locations ]
    timestamps = [datetime.fromtimestamp(float(x['timestampMs'])/1000) for x in locations]
    locs = np.array([x for x in locs if x[0] < lon1 and x[1] < lat1])
    locs = np.array([x for x in locs if x[0] > lon0 and x[1] > lat0])

    #lon0,lat0 = np.amin(locs,axis=0)
    #lon1,lat1 = np.amax(locs,axis=0)
    return locs,timestamps
