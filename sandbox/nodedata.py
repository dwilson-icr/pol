d = {
    "V": ["day of week", "month", "year", "day", "lat-long", "accuracy"],

    "E": [["day of week", "lat-long"], ["month", "lat-long"],\
            ["year", "lat-long"], ["day", "lat-long"], \
            ["lat-long", "accuracy"]],

    "Vdata": {
        "month": {
            "vals": None,
            "parents": None,
            "children": None,
            "cprob": None
        },
        "day of week": {
            "vals": None,
            "parents": None,
            "children": None,
            "cprob": None
        },
        "year": {
            "vals": None,
            "parents": None,
            "children": None,
            "cprob": None
        },
        "day": {
            "vals": None,
            "parents": None,
            "children": None,
            "cprob": None
        },
        "lat-long": {
            "vals": None,
            "parents": None,
            "children": None,
            "cprob": None
        },
        "accuracy":{
            "vals": None,
            "parents": None,
            "children": None,
            "cprob": None
        }
    }
  }

import json
with open("nodedata.json","w") as fp:
    json.dump(d,fp, indent=1)
