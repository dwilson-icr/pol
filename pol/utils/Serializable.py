import pickle
from uuid import uuid4

class Serializable(object):
    _typename = 'serializable'

    def __init__(self,uuid=None):
        if uuid is None:
            uuid = uuid4()
        self.uuid = uuid

    def __repr__(self):
        return self._typename+' {0}'.format(self.uuid)

    def Export(self,fp,export_type=None):
        try:
            exporter = self.__getattribute__('Export_{0}'.format(export_type))
            exporter(fp)
        except AttributeError:
            pickle.dump(self,fp)

    def Exports(self,export_type=None):
        try:
            exporter = self.__getattribute__('Exports_{0}'.format(export_type))
            return exporter()
        except AttributeError:
            return pickle.dumps(self)
