from .basson import Basson
from .channel import Channel
from . import api

class Music(Channel):
    def __init__(self, basson:Basson, mem:bool, file:str, offset:int = 0, length:int = 0, 
                 flags:api.SampleFlag|api.MusicFlag|api.SpeakerFlag|api.CommonFlag=api.MusicFlag.PRESCAN,
                 freq:api.MusicFreqOption=0):
        self.bass = basson.bass

        self.HANDLE = self.bass.MusicLoad(mem, file, offset, length, flags, freq)
        self.WHOAMI = api.ChannelType.MUSIC

        super().__init__()

    def __delattr__(self, name):
        self.bass.MusicFree(self.HANDLE)