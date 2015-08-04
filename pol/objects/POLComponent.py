from pol.utils import Serializable, datetimeToEpoch

class POLComponent(dict,Serializable):
    def __init__(self,*args, **kwargs):
        Serializable.__init__(self,*args,**kwargs)
        dict.__init__(self,*args,**kwargs)

        location=None
        timestamp=None
        deltat=None

    def GetStartTime(self,asfloat=True,days=False):
        if asfloat:
            return datetimeToEpoch(self.timestamp,days)
        return self.timestamp    

    def GetCoords(self,*args,**kwargs):
        return self.location.GetCoords(*args,**kwargs)

    def Set(self,**kwargs):
        for k,v in kwargs.items():
            self.__setattr__(k,v)
