from . import api
from .channel import Channel

from .basson import Basson

# StreamCreate #TODO

# StreamCreateFile
class StreamFile (Channel):
    def __init__(self, basson:Basson, mem:bool, file:str, offset:int=0, length:int=0, 
                 flags:api.SampleFlag|api.StreamFlag|api.CommonFlag=0):
        self.bass = basson.bass 

        self.HANDLE = self.bass.StreamCreateFile(mem, file, offset, length, flags)
        self.WHOAMI = api.ChannelType.STREAM

    def __delattr__(self, name):
        self.bass.StreamFree(self._handle)

# StreamCreateFileUser #TODO

# StreamCreateURL
class StreamURL (Channel):
    def __init__(self, bass:Basson, url:str, offset:int=0, 
                 flags:api.SampleFlag|api.StreamFlag|api.CommonFlag=0,
                 proc:api.DownloadProcType=None, user:api.PTR=None):
        self.bass = bass.bass

        #FIXME не работает передача proc - access violation
        self._proc = api.DOWNLOADPROC(proc) if proc is not None else None
        c_url = url.encode('utf-8')
        
        self.HANDLE = self.bass.StreamCreateURL(c_url, offset, flags, self._proc, user)
        self.WHOAMI = api.ChannelType.STREAM
    
    def __delattr__(self, name):
        self.bass.StreamFree(self._handle)

# StreamGetFilePosition #TODO

# StreamPutData #TODO

# StreamPutFileData #TODO