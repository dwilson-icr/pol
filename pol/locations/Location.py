from pol.utils import Serializable
import numpy as np

class Location(Serializable):
    def __init__(self,coords,*args,**kwargs):
        try:
            ndim = coords.ndim
            self.coords = coords
            self.ndim = ndim
        except:
            self.coords = np.array(coords)
            self.ndim = self.coords.ndim

    def GetCoords(self,*args,**kwargs):
        return self.coords


