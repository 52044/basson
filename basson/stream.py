
from .channel import Channel
from .api import header, types
from . import BASS


#StreamCreateFile
class StreamFile (Channel):
    def __init__(self, bass:BASS, mem:bool, file:str, offset:int=0, length:int=0, 
                 flags:header.BassSampleFlags|header.BassStreamFlags|header.BassCommonFlags=0):
        self.bass = bass.bass 
        self._handle = self.bass.StreamCreateFile(mem, file, offset, length, flags)

    def __delattr__(self, name):
        self.bass.StreamFree(self._handle)

class StreamURL (Channel):
    def __init__(self, bass:BASS, url:str, offset:int=0, 
                 flags:header.BassSampleFlags|header.BassStreamFlags|header.BassCommonFlags=0,
                 proc:types.DownloadProcType=None, user:types.PTR=None):
        self.bass = bass.bass

        #FIXME не работает передача proc - access violation
        self._proc = types.DOWNLOADPROC(proc) if proc is not None else None
        c_url = url.encode('utf-8')
        
        self._handle = self.bass.StreamCreateURL(c_url, offset, flags, self._proc, user)