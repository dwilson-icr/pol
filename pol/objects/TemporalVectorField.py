from pol.objects import POLComponent
from pol.utils import datetimeToEpoch
from bisect import bisect,bisect_right
import numpy as np
from datetime import datetime, timedelta

def bilinear_interpolation(x,y,x0,x1,y0,y1,f00,f01,f10,f11):

    xt = 0.0
    yt = 0.0

    if (x1 - x0) > 0:
        xt = (x - x0) / (x1 - x0)
    if (y1 - y0) > 0:
        yt = (y - y0) / (y1 - y0)

    if xt == 0.0 and yt == 0.0:
        return f00

    a00 = f00
    a10 = f10 - f00
    a01 = f01 - f00
    a11 = f11 + f00 - (f01 + f10)

    return a00 + a10*x + a01*y + a11*x*y

class TemporalVectorField(POLComponent):
    def __init__(self,U,V,x,y,times,*args,**kwargs):
        POLComponent.__init__(self,*args,**kwargs)
        self.U = np.array(U)
        self.V = np.array(V)
        self.x = np.array(x)
        self.y = np.array(y)
        self.times = np.array(times)

    def Interpolate(self,x,y,t):
        t1_idx = bisect(self.times,t)
        t0_idx = max(0,t1_idx - 1)
        t1_idx = min(t1_idx,len(self.times)-1)


        x1_idx = bisect(self.x,x)
        y1_idx = bisect(self.y,y)
        y0_idx = max(0,y1_idx - 1)
        x0_idx = max(0,x1_idx - 1)
        x1_idx = min(x1_idx,len(self.x)-1)
        y1_idx = min(y1_idx,len(self.y)-1)

        x0 = self.x[x0_idx]
        x1 = self.x[x1_idx]
        y0 = self.y[y0_idx]
        y1 = self.y[y1_idx]

        ts = datetimeToEpoch(t,False)
        t0 = datetimeToEpoch(self.times[t0_idx],False)
        t1 = datetimeToEpoch(self.times[t1_idx],False)

        if t1 - t0 > 0:
            p = (ts - t0) / (t1 - t0)
        else:
            p = 1.0


        u00 = p*self.U[t1_idx,y0_idx,x0_idx] + (1.0 - p)*self.U[t0_idx,y0_idx,x0_idx]
        u01 = p*self.U[t1_idx,y1_idx,x0_idx] + (1.0 - p)*self.U[t0_idx,y1_idx,x0_idx]
        u10 = p*self.U[t1_idx,y0_idx,x1_idx] + (1.0 - p)*self.U[t0_idx,y0_idx,x1_idx]
        u11 = p*self.U[t1_idx,y1_idx,x1_idx] + (1.0 - p)*self.U[t0_idx,y1_idx,x1_idx]

        v00 = p*self.V[t1_idx,y0_idx,x0_idx] + (1.0 - p)*self.V[t0_idx,y0_idx,x0_idx]
        v01 = p*self.V[t1_idx,y1_idx,x0_idx] + (1.0 - p)*self.V[t0_idx,y1_idx,x0_idx]
        v10 = p*self.V[t1_idx,y0_idx,x1_idx] + (1.0 - p)*self.V[t0_idx,y0_idx,x1_idx]
        v11 = p*self.V[t1_idx,y1_idx,x1_idx] + (1.0 - p)*self.V[t0_idx,y1_idx,x1_idx]
     
        u = bilinear_interpolation(x,y,x0,x1,y0,y1,u00,u01,u10,u11)
        v = bilinear_interpolation(x,y,x0,x1,y0,y1,v00,v01,v10,v11)
        
        return u,v


    def InterpolateGrid(self,X,Y,t):
        U,V = np.zeros(X.shape),np.zeros(X.shape)

        for i in range(X.shape[0]):
            for j in range(X.shape[1]):
                x,y = X[i,j],Y[i,j]
                U[i,j],V[i,j] = self.Interpolate(x,y,t)

        return U,V

if __name__ == '__main__':
    import matplotlib.pyplot as plt
    U = np.array([[[0.0,1.0],[0.0,1.0]],[[0.0,1.0],[0.0,1.0]]])
    V = np.array([[[1.0,0.0],[0.0,0.0]],[[1.0,0.0],[0.0,0.0]]])

    x = np.array([0.0,1.0])
    y = np.array([0.0,1.0])

    now = datetime.utcnow()
    times = [now - timedelta(seconds=0.5), now + timedelta(seconds=0.5)]

    TVF = TemporalVectorField(U,V,x,y,times)

    #print TVF.Interpolate(0.5,0.5,now-timedelta(seconds=.25))

    X,Y = np.meshgrid(np.linspace(-.50,1.5,100),np.linspace(-.5,1.5,100))
    
    U,V = TVF.InterpolateGrid(X,Y,now)
    
    plt.figure()
    plt.imshow(U)
    plt.figure()
    plt.imshow(V)
    plt.show()

