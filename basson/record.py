from .basson import Basson
from .channel import Channel
from . import api

class Record(Channel):
    def __init__(self, basson:Basson, device:int=-1, freq:int=0, chans:int=2, flags:api.RecordFlag=0, callback=None):
        self.bass = basson.bass
        self._proc = api.RECORDPROC(callback) if callback else None

        self.bass.RecordInit(device)
        self.HANDLE = self.bass.RecordStart(freq, chans, flags, self._proc, None)
        self.WHOAMI = api.ChannelType.RECORD

        super().__init__()

    def __del__(self, name):
        self.bass.RecordFree(self.HANDLE)

    def stop(self):
        super().__init__()
        self = None

#getdevice
#deviceinfo
#getinput
#getinputname
#setdevice
#setinput
