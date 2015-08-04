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

    class openfp:
        def __init__(self,typestr='r'):
            self.typestr=typestr
        def __call__(self,f):
            def wrapped(*args,**kwargs):
                try:
                    args[1].seek(0)
                    return f(*args,**kwargs)
                except:
                    with open(args[1],self.typestr) as fp:
                        return f(args[0],fp,*(args[2:]),**kwargs)
            wrapped.__name__ = f.__name__
            wrapped.__doc__ = f.__doc__
            return wrapped


    
    def Export(self,fp,export_type=None,**kwargs):
        try:
            exporter = self.__getattribute__('Export_{0}'.format(export_type))
        except AttributeError:
            exporter = self.Export_pickle
        exporter(fp)

    def Exports(self,export_type=None,**kwargs):
        try:
            exporter = self.__getattribute__('Exports_{0}'.format(export_type))
        except AttributeError:
            exporter = self.Exports_pickle
        return exporter()

    def Import(self,fp,import_type=None,**kwargs):
        try:
            importer = self.__getattribute__('Import_{0}'.format(import_type))
            importer(fp)
        except AttributeError:
            importer = self.Import_pickle
        importer(fp)

    def Imports(self,st,import_type=None,**kwargs):
        try:
            importer = self.__getattribute__('Imports_{0}'.format(import_type))
        except AttributeError:
            importer = self.Imports_pickle
        importer(st)

    @openfp('w')
    def Export_pickle(self,fp):
        pickle.dump(self,fp)

    @openfp('r')
    def Import_pickle(self,fp):
        self_obj = pickle.load(fp)

        for k,v in self_obj.__dict__.items():
            self.__setattr__(k,v) 

















