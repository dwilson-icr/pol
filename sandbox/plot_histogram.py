import json, os, sys
import numpy as np
import matplotlib.pyplot as plt
import smopy
from datetime import datetime

data_path = '/home/dwilson/data/LocationHistory.json'
if not os.path.exists(data_path):
    print "LocationHistory.json not found at {0}".format(data_path)
    exit()

with open(data_path,'r') as fp:
    data = json.load(fp)

locations = data['locations']

N = len(locations)

locs = [(x['longitudeE7']*1e-7,x['latitudeE7']*1e-7) for x in locations ]
timestamps = [datetime.fromtimestamp(float(x['timestampMs'])/1000) for x in locations]
#locs = np.array([x for x in locs if x[0] < -90.0 and x[1] > 38.0])
locs = np.array([x for x in locs if x[0] < -104.612 and x[1] < 39.8891])
locs = np.array([x for x in locs if x[0] > -105.296 and x[1] > 39.460])

lon0,lat0 = np.amin(locs,axis=0)
lon1,lat1 = np.amax(locs,axis=0)


plt.figure()
#plt.plot(locs[:,0],locs[:,1],'g-')
#maps = smopy.Map((lat0,lon0,lat1,lon1),z=10)
#ax = maps.show_mpl()
#ax.plot(locs[:,0],locs[:,1],'g-')
plt.hexbin(locs[:,0],locs[:,1],bins='log',gridsize=5000,marginals=True,mincnt=25,cmap=plt.cm.jet)
plt.show()

