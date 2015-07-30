from pol.utils import Serializable

class POLComponent(Serializable):
    def __init__(self,*args, **kwargs):
        Serializable.__init__(self,*args,**kwargs)
