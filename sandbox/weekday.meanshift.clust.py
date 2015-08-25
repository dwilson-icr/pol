# encoding=utf8
import json
import numpy as np
import matplotlib.pyplot as plt
import csv
from sklearn.cluster import MeanShift, estimate_bandwidth
from itertools import cycle
from collections import Counter
from datetime import datetime

data_path = '/Users/carlz/Documents/PythonExamples/pgmtests/dow.time/daybyhour/LocationHistory.json'


with open(data_path,'r') as fp:
    data = json.load(fp)

    locations = data['locations']


    for dicts in locations:

        for attributes in dicts:

            # changes timestampMs into a usable format

            time_params = float(dicts.get("timestampMs"))
            time_params *= .001


            # datetime.fromtimestamp gives date and time data from a timestamp

            dtime = datetime.fromtimestamp(time_params)
            w = datetime.weekday(dtime)
            m = dtime.month
            d = dtime.day
            y = dtime.year
            h = dtime.hour
            min = dtime.minute
            sec = dtime.second


            # creates a pair of lat-long coordinates

            latlong = (float(dicts["latitudeE7"])*1e-7,\
                        float(dicts["longitudeE7"])*1e-7)


        # update dictionaries

        dicts.update({"dayofweek" : w, "month" : m, "day" : d, "year" : y, "hour" : h,\
			"minute" : min, "second" : sec, "latlong" : latlong})




# extracts Monday’s from total list of location data

mon = [d for d in locations if d['dayofweek'] == 0]

# extracts hourly locations from Monday’s list

mon00 = [t for t in mon if t['hour'] == 0]
mon01 = [t for t in mon if t['hour'] == 1]
mon02 = [t for t in mon if t['hour'] == 2]
mon03 = [t for t in mon if t['hour'] == 3]
mon04 = [t for t in mon if t['hour'] == 4]
mon05 = [t for t in mon if t['hour'] == 5]
mon06 = [t for t in mon if t['hour'] == 6]
mon07 = [t for t in mon if t['hour'] == 7]
mon08 = [t for t in mon if t['hour'] == 8]
mon09 = [t for t in mon if t['hour'] == 9]
mon10 = [t for t in mon if t['hour'] == 10]
mon11 = [t for t in mon if t['hour'] == 11]
mon12 = [t for t in mon if t['hour'] == 12]
mon13 = [t for t in mon if t['hour'] == 13]
mon14 = [t for t in mon if t['hour'] == 14]
mon15 = [t for t in mon if t['hour'] == 15]
mon16 = [t for t in mon if t['hour'] == 16]
mon17 = [t for t in mon if t['hour'] == 17]
mon18 = [t for t in mon if t['hour'] == 18]
mon19 = [t for t in mon if t['hour'] == 19]
mon20 = [t for t in mon if t['hour'] == 20]
mon21 = [t for t in mon if t['hour'] == 21]
mon22 = [t for t in mon if t['hour'] == 22]
mon23 = [t for t in mon if t['hour'] == 23]


# extracts Tuesdays’s from total list of location data

tues = [d for d in locations if d['dayofweek'] == 1]

# extracts hourly locations from Tuesday’s list

tues00 = [t for t in tues if t['hour'] == 0]
tues01 = [t for t in tues if t['hour'] == 1]
tues02 = [t for t in tues if t['hour'] == 2]
tues03 = [t for t in tues if t['hour'] == 3]
tues04 = [t for t in tues if t['hour'] == 4]
tues05 = [t for t in tues if t['hour'] == 5]
tues06 = [t for t in tues if t['hour'] == 6]
tues07 = [t for t in tues if t['hour'] == 7]
tues08 = [t for t in tues if t['hour'] == 8]
tues09 = [t for t in tues if t['hour'] == 9]
tues10 = [t for t in tues if t['hour'] == 10]
tues11 = [t for t in tues if t['hour'] == 11]
tues12 = [t for t in tues if t['hour'] == 12]
tues13 = [t for t in tues if t['hour'] == 13]
tues14 = [t for t in tues if t['hour'] == 14]
tues15 = [t for t in tues if t['hour'] == 15]
tues16 = [t for t in tues if t['hour'] == 16]
tues17 = [t for t in tues if t['hour'] == 17]
tues18 = [t for t in tues if t['hour'] == 18]
tues19 = [t for t in tues if t['hour'] == 19]
tues20 = [t for t in tues if t['hour'] == 20]
tues21 = [t for t in tues if t['hour'] == 21]
tues22 = [t for t in tues if t['hour'] == 22]
tues23 = [t for t in tues if t['hour'] == 23]


# extracts Wednesday’s from total list of location data

wed = [d for d in locations if d['dayofweek'] == 2]

# extracts hourly locations from Wednesday’s list

wed00 = [t for t in wed if t['hour'] == 0]
wed01 = [t for t in wed if t['hour'] == 1]
wed02 = [t for t in wed if t['hour'] == 2]
wed03 = [t for t in wed if t['hour'] == 3]
wed04 = [t for t in wed if t['hour'] == 4]
wed05 = [t for t in wed if t['hour'] == 5]
wed06 = [t for t in wed if t['hour'] == 6]
wed07 = [t for t in wed if t['hour'] == 7]
wed08 = [t for t in wed if t['hour'] == 8]
wed09 = [t for t in wed if t['hour'] == 9]
wed10 = [t for t in wed if t['hour'] == 10]
wed11 = [t for t in wed if t['hour'] == 11]
wed12 = [t for t in wed if t['hour'] == 12]
wed13 = [t for t in wed if t['hour'] == 13]
wed14 = [t for t in wed if t['hour'] == 14]
wed15 = [t for t in wed if t['hour'] == 15]
wed16 = [t for t in wed if t['hour'] == 16]
wed17 = [t for t in wed if t['hour'] == 17]
wed18 = [t for t in wed if t['hour'] == 18]
wed19 = [t for t in wed if t['hour'] == 19]
wed20 = [t for t in wed if t['hour'] == 20]
wed21 = [t for t in wed if t['hour'] == 21]
wed22 = [t for t in wed if t['hour'] == 22]
wed23 = [t for t in wed if t['hour'] == 23]


# extracts Thursdays’s from total list of location data

thurs = [d for d in locations if d['dayofweek'] == 3]

# extracts hourly locations from Thursday’s list

thurs00 = [t for t in thurs if t['hour'] == 0]
thurs01 = [t for t in thurs if t['hour'] == 1]
thurs02 = [t for t in thurs if t['hour'] == 2]
thurs03 = [t for t in thurs if t['hour'] == 3]
thurs04 = [t for t in thurs if t['hour'] == 4]
thurs05 = [t for t in thurs if t['hour'] == 5]
thurs06 = [t for t in thurs if t['hour'] == 6]
thurs07 = [t for t in thurs if t['hour'] == 7]
thurs08 = [t for t in thurs if t['hour'] == 8]
thurs09 = [t for t in thurs if t['hour'] == 9]
thurs10 = [t for t in thurs if t['hour'] == 10]
thurs11 = [t for t in thurs if t['hour'] == 11]
thurs12 = [t for t in thurs if t['hour'] == 12]
thurs13 = [t for t in thurs if t['hour'] == 13]
thurs14 = [t for t in thurs if t['hour'] == 14]
thurs15 = [t for t in thurs if t['hour'] == 15]
thurs16 = [t for t in thurs if t['hour'] == 16]
thurs17 = [t for t in thurs if t['hour'] == 17]
thurs18 = [t for t in thurs if t['hour'] == 18]
thurs19 = [t for t in thurs if t['hour'] == 19]
thurs20 = [t for t in thurs if t['hour'] == 20]
thurs21 = [t for t in thurs if t['hour'] == 21]
thurs22 = [t for t in thurs if t['hour'] == 22]
thurs23 = [t for t in thurs if t['hour'] == 23]


# extracts Friday’s from total list of location data

fri = [d for d in locations if d['dayofweek'] == 4]

# extracts hourly locations from Friday’s list

fri00 = [t for t in fri if t['hour'] == 0]
fri01 = [t for t in fri if t['hour'] == 1]
fri02 = [t for t in fri if t['hour'] == 2]
fri03 = [t for t in fri if t['hour'] == 3]
fri04 = [t for t in fri if t['hour'] == 4]
fri05 = [t for t in fri if t['hour'] == 5]
fri06 = [t for t in fri if t['hour'] == 6]
fri07 = [t for t in fri if t['hour'] == 7]
fri08 = [t for t in fri if t['hour'] == 8]
fri09 = [t for t in fri if t['hour'] == 9]
fri10 = [t for t in fri if t['hour'] == 10]
fri11 = [t for t in fri if t['hour'] == 11]
fri12 = [t for t in fri if t['hour'] == 12]
fri13 = [t for t in fri if t['hour'] == 13]
fri14 = [t for t in fri if t['hour'] == 14]
fri15 = [t for t in fri if t['hour'] == 15]
fri16 = [t for t in fri if t['hour'] == 16]
fri17 = [t for t in fri if t['hour'] == 17]
fri18 = [t for t in fri if t['hour'] == 18]
fri19 = [t for t in fri if t['hour'] == 19]
fri20 = [t for t in fri if t['hour'] == 20]
fri21 = [t for t in fri if t['hour'] == 21]
fri22 = [t for t in fri if t['hour'] == 22]
fri23 = [t for t in fri if t['hour'] == 23]


# extracts Saturday’s from total list of location data

sat = [d for d in locations if d['dayofweek'] == 5]

# extracts hourly locations from Saturday’s list

sat00 = [t for t in sat if t['hour'] == 0]
sat01 = [t for t in sat if t['hour'] == 1]
sat02 = [t for t in sat if t['hour'] == 2]
sat03 = [t for t in sat if t['hour'] == 3]
sat04 = [t for t in sat if t['hour'] == 4]
sat05 = [t for t in sat if t['hour'] == 5]
sat06 = [t for t in sat if t['hour'] == 6]
sat07 = [t for t in sat if t['hour'] == 7]
sat08 = [t for t in sat if t['hour'] == 8]
sat09 = [t for t in sat if t['hour'] == 9]
sat10 = [t for t in sat if t['hour'] == 10]
sat11 = [t for t in sat if t['hour'] == 11]
sat12 = [t for t in sat if t['hour'] == 12]
sat13 = [t for t in sat if t['hour'] == 13]
sat14 = [t for t in sat if t['hour'] == 14]
sat15 = [t for t in sat if t['hour'] == 15]
sat16 = [t for t in sat if t['hour'] == 16]
sat17 = [t for t in sat if t['hour'] == 17]
sat18 = [t for t in sat if t['hour'] == 18]
sat19 = [t for t in sat if t['hour'] == 19]
sat20 = [t for t in sat if t['hour'] == 20]
sat21 = [t for t in sat if t['hour'] == 21]
sat22 = [t for t in sat if t['hour'] == 22]
sat23 = [t for t in sat if t['hour'] == 23]


# extracts Sunday’s from total list of location data

sun = [d for d in locations if d['dayofweek'] == 6]

# extracts hourly locations from Sunday’s list

sun00 = [t for t in sun if t['hour'] == 0]
sun01 = [t for t in sun if t['hour'] == 1]
sun02 = [t for t in sun if t['hour'] == 2]
sun03 = [t for t in sun if t['hour'] == 3]
sun04 = [t for t in sun if t['hour'] == 4]
sun05 = [t for t in sun if t['hour'] == 5]
sun06 = [t for t in sun if t['hour'] == 6]
sun07 = [t for t in sun if t['hour'] == 7]
sun08 = [t for t in sun if t['hour'] == 8]
sun09 = [t for t in sun if t['hour'] == 9]
sun10 = [t for t in sun if t['hour'] == 10]
sun11 = [t for t in sun if t['hour'] == 11]
sun12 = [t for t in sun if t['hour'] == 12]
sun13 = [t for t in sun if t['hour'] == 13]
sun14 = [t for t in sun if t['hour'] == 14]
sun15 = [t for t in sun if t['hour'] == 15]
sun16 = [t for t in sun if t['hour'] == 16]
sun17 = [t for t in sun if t['hour'] == 17]
sun18 = [t for t in sun if t['hour'] == 18]
sun19 = [t for t in sun if t['hour'] == 19]
sun20 = [t for t in sun if t['hour'] == 20]
sun21 = [t for t in sun if t['hour'] == 21]
sun22 = [t for t in sun if t['hour'] == 22]
sun23 = [t for t in sun if t['hour'] == 23]



# function weekhour -creates a list of lat-long pairs of locations in “Metro Denver”
#                    -uses MeanShift class from sklearn.cluster module
#                    -MeanShift parameters: bandwidth, bin_seeding
#                     bandwidth is the radius of the cluster
#                     bin_seeding=true forces initial kernel locations to to be the 
#                                      locations of the discretized version of points



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

    plt.figure(day+1)
    plt.clf()

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

        with open('weekdayclusters.csv', 'a') as csvfile:
            fieldnames = ['day', 'hour', 'densest cluster', 'address', 'percent', 
                          'number of samples', 'number of estimated clusters']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerow({'day': day, 'hour': hour, \
                             'densest cluster': densest, \
                             'address': address, \
                             'percent': percent, \
                             'number of samples': num_samples, \
                             'number of estimated clusters': n_clusters_})




    plt.title('Estimated number of clusters: %d' % n_clusters_)




weekhour(lst=mon00,day=0,hour=0,num=10)
weekhour(lst=mon01,day=0,hour=1,num=10)
weekhour(lst=mon02,day=0,hour=2,num=10)
weekhour(lst=mon03,day=0,hour=3,num=10)
weekhour(lst=mon04,day=0,hour=4,num=10)
weekhour(lst=mon05,day=0,hour=5,num=10)
weekhour(lst=mon06,day=0,hour=6,num=10)
weekhour(lst=mon07,day=0,hour=7,num=10)
weekhour(lst=mon08,day=0,hour=8,num=10)
weekhour(lst=mon09,day=0,hour=9,num=10)
weekhour(lst=mon10,day=0,hour=10,num=10)
weekhour(lst=mon11,day=0,hour=11,num=10)
weekhour(lst=mon12,day=0,hour=12,num=10)
weekhour(lst=mon13,day=0,hour=13,num=10)
weekhour(lst=mon14,day=0,hour=14,num=10)
weekhour(lst=mon15,day=0,hour=15,num=10)
weekhour(lst=mon16,day=0,hour=16,num=10)
weekhour(lst=mon17,day=0,hour=17,num=10)
weekhour(lst=mon18,day=0,hour=18,num=10)
weekhour(lst=mon19,day=0,hour=19,num=10)
weekhour(lst=mon20,day=0,hour=20,num=10)
weekhour(lst=mon21,day=0,hour=21,num=10)
weekhour(lst=mon22,day=0,hour=22,num=10)
weekhour(lst=mon23,day=0,hour=23,num=10)
weekhour(lst=tues00,day=1,hour=0,num=10)
weekhour(lst=tues01,day=1,hour=1,num=10)
weekhour(lst=tues02,day=1,hour=2,num=10)
weekhour(lst=tues03,day=1,hour=3,num=10)
weekhour(lst=tues04,day=1,hour=4,num=10)
weekhour(lst=tues05,day=1,hour=5,num=10)
weekhour(lst=tues06,day=1,hour=6,num=10)
weekhour(lst=tues07,day=1,hour=7,num=10)
weekhour(lst=tues08,day=1,hour=8,num=10)
weekhour(lst=tues09,day=1,hour=9,num=10)
weekhour(lst=tues10,day=1,hour=10,num=10)
weekhour(lst=tues11,day=1,hour=11,num=10)
weekhour(lst=tues12,day=1,hour=12,num=10)
weekhour(lst=tues13,day=1,hour=13,num=10)
weekhour(lst=tues14,day=1,hour=14,num=10)
weekhour(lst=tues15,day=1,hour=15,num=10)
weekhour(lst=tues16,day=1,hour=16,num=10)
weekhour(lst=tues17,day=1,hour=17,num=10)
weekhour(lst=tues18,day=1,hour=18,num=10)
weekhour(lst=tues19,day=1,hour=19,num=10)
weekhour(lst=tues20,day=1,hour=20,num=10)
weekhour(lst=tues21,day=1,hour=21,num=10)
weekhour(lst=tues22,day=1,hour=22,num=10)
weekhour(lst=tues23,day=1,hour=23,num=10)
weekhour(lst=wed00,day=2,hour=0,num=10)
weekhour(lst=wed01,day=2,hour=1,num=10)
weekhour(lst=wed02,day=2,hour=2,num=10)
weekhour(lst=wed03,day=2,hour=3,num=10)
weekhour(lst=wed04,day=2,hour=4,num=10)
weekhour(lst=wed05,day=2,hour=5,num=10)
weekhour(lst=wed06,day=2,hour=6,num=10)
weekhour(lst=wed07,day=2,hour=7,num=10)
weekhour(lst=wed08,day=2,hour=8,num=10)
weekhour(lst=wed09,day=2,hour=9,num=10)
weekhour(lst=wed10,day=2,hour=10,num=10)
weekhour(lst=wed11,day=2,hour=11,num=10)
weekhour(lst=wed12,day=2,hour=12,num=10)
weekhour(lst=wed13,day=2,hour=13,num=10)
weekhour(lst=wed14,day=2,hour=14,num=10)
weekhour(lst=wed15,day=2,hour=15,num=10)
weekhour(lst=wed16,day=2,hour=16,num=10)
weekhour(lst=wed17,day=2,hour=17,num=10)
weekhour(lst=wed18,day=2,hour=18,num=10)
weekhour(lst=wed19,day=2,hour=19,num=10)
weekhour(lst=wed20,day=2,hour=20,num=10)
weekhour(lst=wed21,day=2,hour=21,num=10)
weekhour(lst=wed22,day=2,hour=22,num=10)
weekhour(lst=wed23,day=2,hour=23,num=10)
weekhour(lst=thurs00,day=3,hour=0,num=10)
weekhour(lst=thurs01,day=3,hour=1,num=10)
weekhour(lst=thurs02,day=3,hour=2,num=10)
weekhour(lst=thurs03,day=3,hour=3,num=10)
weekhour(lst=thurs04,day=3,hour=4,num=10)
weekhour(lst=thurs05,day=3,hour=5,num=10)
weekhour(lst=thurs06,day=3,hour=6,num=10)
weekhour(lst=thurs07,day=3,hour=7,num=10)
weekhour(lst=thurs08,day=3,hour=8,num=10)
weekhour(lst=thurs09,day=3,hour=9,num=10)
weekhour(lst=thurs10,day=3,hour=10,num=10)
weekhour(lst=thurs11,day=3,hour=11,num=10)
weekhour(lst=thurs12,day=3,hour=12,num=10)
weekhour(lst=thurs13,day=3,hour=13,num=10)
weekhour(lst=thurs14,day=3,hour=14,num=10)
weekhour(lst=thurs15,day=3,hour=15,num=10)
weekhour(lst=thurs16,day=3,hour=16,num=10)
weekhour(lst=thurs17,day=3,hour=17,num=10)
weekhour(lst=thurs18,day=3,hour=18,num=10)
weekhour(lst=thurs19,day=3,hour=19,num=10)
weekhour(lst=thurs20,day=3,hour=20,num=10)
weekhour(lst=thurs21,day=3,hour=21,num=10)
weekhour(lst=thurs22,day=3,hour=22,num=10)
weekhour(lst=thurs23,day=3,hour=23,num=10)
weekhour(lst=fri00,day=4,hour=0,num=10)
weekhour(lst=fri01,day=4,hour=1,num=10)
weekhour(lst=fri02,day=4,hour=2,num=10)
weekhour(lst=fri03,day=4,hour=3,num=10)
weekhour(lst=fri04,day=4,hour=4,num=10)
weekhour(lst=fri05,day=4,hour=5,num=10)
weekhour(lst=fri06,day=4,hour=6,num=10)
weekhour(lst=fri07,day=4,hour=7,num=10)
weekhour(lst=fri08,day=4,hour=8,num=10)
weekhour(lst=fri09,day=4,hour=9,num=10)
weekhour(lst=fri10,day=4,hour=10,num=10)
weekhour(lst=fri11,day=4,hour=11,num=10)
weekhour(lst=fri12,day=4,hour=12,num=10)
weekhour(lst=fri13,day=4,hour=13,num=10)
weekhour(lst=fri14,day=4,hour=14,num=10)
weekhour(lst=fri15,day=4,hour=15,num=10)
weekhour(lst=fri16,day=4,hour=16,num=10)
weekhour(lst=fri17,day=4,hour=17,num=10)
weekhour(lst=fri18,day=4,hour=18,num=10)
weekhour(lst=fri19,day=4,hour=19,num=10)
weekhour(lst=fri20,day=4,hour=20,num=10)
weekhour(lst=fri21,day=4,hour=21,num=10)
weekhour(lst=fri22,day=4,hour=22,num=10)
weekhour(lst=fri23,day=4,hour=23,num=10)
weekhour(lst=sat00,day=5,hour=0,num=10)
weekhour(lst=sat01,day=5,hour=1,num=10)
weekhour(lst=sat02,day=5,hour=2,num=10)
weekhour(lst=sat03,day=5,hour=3,num=10)
weekhour(lst=sat04,day=5,hour=4,num=10)
weekhour(lst=sat05,day=5,hour=5,num=10)
weekhour(lst=sat06,day=5,hour=6,num=10)
weekhour(lst=sat07,day=5,hour=7,num=10)
weekhour(lst=sat08,day=5,hour=8,num=10)
weekhour(lst=sat09,day=5,hour=9,num=10)
weekhour(lst=sat10,day=5,hour=10,num=10)
weekhour(lst=sat11,day=5,hour=11,num=10)
weekhour(lst=sat12,day=5,hour=12,num=10)
weekhour(lst=sat13,day=5,hour=13,num=10)
weekhour(lst=sat14,day=5,hour=14,num=10)
weekhour(lst=sat15,day=5,hour=15,num=10)
weekhour(lst=sat16,day=5,hour=16,num=10)
weekhour(lst=sat17,day=5,hour=17,num=10)
weekhour(lst=sat18,day=5,hour=18,num=10)
weekhour(lst=sat19,day=5,hour=19,num=10)
weekhour(lst=sat20,day=5,hour=20,num=10)
weekhour(lst=sat21,day=5,hour=21,num=10)
weekhour(lst=sat22,day=5,hour=22,num=10)
weekhour(lst=sat23,day=5,hour=23,num=10)
weekhour(lst=sun00,day=6,hour=0,num=10)
weekhour(lst=sun01,day=6,hour=1,num=10)
weekhour(lst=sun02,day=6,hour=2,num=10)
weekhour(lst=sun03,day=6,hour=3,num=10)
weekhour(lst=sun04,day=6,hour=4,num=10)
weekhour(lst=sun05,day=6,hour=5,num=10)
weekhour(lst=sun06,day=6,hour=6,num=10)
weekhour(lst=sun07,day=6,hour=7,num=10)
weekhour(lst=sun08,day=6,hour=8,num=10)
weekhour(lst=sun09,day=6,hour=9,num=10)
weekhour(lst=sun10,day=6,hour=10,num=10)
weekhour(lst=sun11,day=6,hour=11,num=10)
weekhour(lst=sun12,day=6,hour=12,num=10)
weekhour(lst=sun13,day=6,hour=13,num=10)
weekhour(lst=sun14,day=6,hour=14,num=10)
weekhour(lst=sun15,day=6,hour=15,num=10)
weekhour(lst=sun16,day=6,hour=16,num=10)
weekhour(lst=sun17,day=6,hour=17,num=10)
weekhour(lst=sun18,day=6,hour=18,num=10)
weekhour(lst=sun19,day=6,hour=19,num=10)
weekhour(lst=sun20,day=6,hour=20,num=10)
weekhour(lst=sun21,day=6,hour=21,num=10)
weekhour(lst=sun22,day=6,hour=22,num=10)
weekhour(lst=sun23,day=6,hour=23,num=10)
