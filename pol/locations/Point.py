from pol.locations import Location
import numpy as np

class Point(Location):
    def __init__(self,x,y,z=0):
        self.coords = np.array([x,y,z])
        self.ndim = 1
