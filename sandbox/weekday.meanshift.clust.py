# encoding=utf8
import json
import numpy as np
import matplotlib.pyplot as plt
import csv
from sklearn.cluster import MeanShift, estimate_bandwidth
from itertools import cycle
from collections import Counter
from datetime import datetime
import math

data_path = '/Users/carlz/Documents/PythonExamples/pgmtests/dow.time/daybyhour/top/LocationHistory.json'

# opens file

with open(data_path,'r') as fp:
    data = json.load(fp)

    locations = data['locations']


# updates dictionaries with usable data

    for dicts in locations:
        for attributes in dicts:
            time_params = float(dicts.get("timestampMs"))
            time_params *= .001
            dtime = datetime.fromtimestamp(time_params)
            w = datetime.weekday(dtime)
            m = dtime.month
            d = dtime.day
            y = dtime.year
            h = dtime.hour
            min = dtime.minute
            sec = dtime.second
            latlong = (float(dicts["latitudeE7"])*1e-7,\
                        float(dicts["longitudeE7"])*1e-7)
        dicts.update({"dayofweek" : w, "month" : m, "day" : d, "year" : y, "hour" : h,\
			"minute" : min, "second" : sec, "latlong" : latlong})


# filters data into lists by hour and day

dayhour = [ ]
for i in range(24):
    day = filter(lambda locations: locations['hour'] == i, locations)
    for j in range(7):
        dayhour.append(filter(lambda day: day['dayofweek'] == j, day))


# function carries out mean shift clustering algorithm on lat-long pairs

def weekhour(lst,day,hour,num):

    l = [ ]
    for dicts in lst:
        latlong = dicts["latlong"]
        l.append(latlong)
    l = np.array(l)
    l = np.array([x for x in l if x[0] < 40])
    l = np.array([x for x in l if x[1] < -102.0])
    l = np.array([x for x in l if x[0] > 39])
    l = np.array([x for x in l if x[1] > -105.5])

    bandwidth = .001
    ms = MeanShift(bandwidth=bandwidth, bin_seeding=True)
    ms.fit(l)
    labels = ms.labels_
    cluster_centers = ms.cluster_centers_
    labels_unique = np.unique(labels)
    n_clusters_ = len(labels_unique)


    colors = cycle('bgrcmykbgrcmykbgrcmykbgrcmyk')
    for k, col in zip(range(n_clusters_), colors):
        my_members = labels == k
        cluster_center = cluster_centers[k]
        plt.plot(l[my_members,1], l[my_members,0], col + '.')
        plt.plot(cluster_center[1], cluster_center[0], 'x', markerfacecolor=col,\
    markeredgecolor='k', markersize=14)

    num_samples = len(labels)
    list_clust_cents = cluster_centers.tolist()
    num_labels = Counter(labels).most_common()
    top = tuple(num_labels)

    if num > n_clusters_:
        num = n_clusters_

    for i in range(num):
        densest = top[i][1]
        percent = round((float(densest)/float(num_samples))*100,3)
        if densest >= 60:
            import geocoder
            g = geocoder.google(list_clust_cents[i], method='reverse')
            address = g.address
        else:
            address = 0

        with open('weekdayclusterstest.csv', 'a') as csvfile:
            fieldnames = ['day', 'hour', 'densest cluster', 'address', 'percent', 
                          'number of samples', 'number of estimated clusters']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerow({'densest cluster': densest, \
                             'day': day, \
                             'hour': hour, \
                             'address': address, \
                             'percent': percent, \
                             'number of samples': num_samples, \
                             'number of estimated clusters': n_clusters_})



# carries out the function for each day by hour dataset

for i in range(168):
    days = ['0','1','2','3','4','5','6']
    for j in range(len(days)):
        if i % 7 == j:
            day = days[j]
    hours = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13',  
           '14', '15', '16', '17', '18', '19', '20', '21', '22', '23']
    cutoffs = [6+(7*x) for x in range(24)]
    for x in range(len(cutoffs)):
        if i <= cutoffs[x]:
            hour = hours[x]
            break

    weekhour(lst=dayhour[i],day=day,hour=hour,num=10)
