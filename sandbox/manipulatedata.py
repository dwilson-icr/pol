# a is a list of location dictionaries
a = [
{
    "timestampMs" : ,
    "latitudeE7" : ,
    "longitudeE7" : ,
    "accuracy" : 
  }
 ]

from datetime import datetime
import geocoder

for dicts in a:
    for attributes in dicts:
        # changes timestampMs into a usable format
        time_params = float(dicts.get("timestampMs"))
        time_params *= .001
        # datetime.fromtimestamp gives date and time data from a timestamp
        dtime = datetime.fromtimestamp(time_params)
        w = datetime.weekday(dtime)
        m = dtime.month
        d = dtime.day
        Y = dtime.year
        h = dtime.hour
        # creates a pair of lat-long coordinates
        latlong = (float(dicts["latitudeE7"])*1e-7,\
                    float(dicts["longitudeE7"])*1e-7)
        # g.address gives address corresponding to lat-long pair
        g = geocoder.google(latlong, method='reverse')
        g = g.address
    # update dictionaries with relevant information and deletes irrelavant info
    dicts.update({"day of week": w, "month": m, "day": d, "year": Y, "hour": h,\
                "address": g})
    # deletes unused attributes in dicts to expedite libpgm process
    del dicts["timestampMs"]
    del dicts["latitudeE7"]
    del dicts["longitudeE7"]
    if "activitys" in dicts:
        del dicts["activitys"]
    if "velocity" in dicts:
        del dicts["velocity"]
    if "heading" in dicts:
        del dicts["heading"]
    if "altitude" in dicts:
        del dicts["altitude"]

import json
with open("manipulatedata.json","w") as fp:
    json.dump(a,fp, indent=1)
