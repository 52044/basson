
from .channel import Channel
from .api import header, types
from . import BASS

# StreamCreate #TODO

# StreamCreateFile
class StreamFile (Channel):
    def __init__(self, bass:BASS, mem:bool, file:str, offset:int=0, length:int=0, 
                 flags:header.SampleFlags|header.StreamFlags|header.CommonFlags=0):
        self.bass = bass.bass 

        self.HANDLE = self.bass.StreamCreateFile(mem, file, offset, length, flags)
        self.WHOAMI = header.ChannelType.STREAM

    def __delattr__(self, name):
        self.bass.StreamFree(self._handle)

# StreamCreateFileUser #TODO

# StreamCreateURL
class StreamURL (Channel):
    def __init__(self, bass:BASS, url:str, offset:int=0, 
                 flags:header.SampleFlags|header.StreamFlags|header.CommonFlags=0,
                 proc:types.DownloadProcType=None, user:types.PTR=None):
        self.bass = bass.bass

        #FIXME не работает передача proc - access violation
        self._proc = types.DOWNLOADPROC(proc) if proc is not None else None
        c_url = url.encode('utf-8')
        
        self.HANDLE = self.bass.StreamCreateURL(c_url, offset, flags, self._proc, user)
        self.WHOAMI = header.ChannelType.STREAM
    
    def __delattr__(self, name):
        self.bass.StreamFree(self._handle)

# StreamGetFilePosition #TODO

# StreamPutData #TODO

# StreamPutFileData #TODO