# a is a list of location dictionaries
a = [{
    "timestampMs" :
    "latitudeE7" :
    "longitudeE7" :
    "accuracy" :
  }
  ]
import time
from datetime import date

for dicts in a:
    for attributes in dicts:
        time_params = float(dicts.get("timestampMs"))
        # w, m, d, Y, h convert timestampMs into day of week, month, day, year
        # and hour of day, respectively
        w = time.strftime("%w", time.localtime(time_params / 1000.0))
        m = time.strftime("%m", time.localtime(time_params / 1000.0))
        d = time.strftime("%d", time.localtime(time_params / 1000.0))
        Y = time.strftime("%Y", time.localtime(time_params / 1000.0))
        h = time.strftime("%H", time.localtime(time_params / 1000.0))
        # creates a pair of lat-long coordinates
        latlong = (float(dicts["latitudeE7"])*1e-7,\
                    float(dicts["longitudeE7"])*1e-7)
    # update dictionaries with relevant information and deletes irrelavant info
    dicts.update({"day of week": w, "month": m, "day": d, "year": Y, "hour": h,\
                "lat-long": latlong})
    del dicts["timestampMs"]
    del dicts["latitudeE7"]
    del dicts["longitudeE7"]

import json
with open("manipulatedata.json","w") as fp:
    json.dump(a,fp, indent=1)
