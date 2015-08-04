from datetime import datetime, timedelta

EPOCH = datetime(1970,1,1,0,0,0)

def datetimeToEpoch(dt,days=False):
    secs = (dt - EPOCH).total_seconds()
    if days: return secs / 3600.0 / 24.0
    return secs

def epochToDatetime(secs):
    return datetime.utcfromtimestamp(secs)

if __name__ == '__main__':
    now = datetime.utcnow()
    print now
    secs = datetimeToEpoch(datetime.utcnow())
    print epochToDatetime(secs)
