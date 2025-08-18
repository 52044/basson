from .api import header
from .api.api import BassError
from .bass import BASS

class Channel():
    def __init__(self, bass:BASS, handle:int):
        self.bass = bass.bass
        self._handle = handle
        
    @property
    def handle(self):
        ''' Contain handle(int) of current channel. Uses for any interaction with channel '''
        return self._handle

    def __delattr__(self, name):
        self.bass.ChannelFree(self._handle)

    def play(self, restart: bool = False):
        ''' Starts/resumes playback of channel. Same as `start`, but have option start from begining
        
        :param restart: Start playback from begin
        '''
        try:
            self.bass.ChannelPlay(self._handle, restart)
        except BassError as e:
            if e.code == BassError.START:
                self.start()
            else:
                raise e
    def pause(self):
        ''' Pauses playback/recording of channel
        '''
        self.bass.ChannelPause(self._handle)
    def stop(self):
        ''' Stops playback/recording of channel
        '''
        self.bass.ChannelStop(self._handle)   
    def start(self):
        ''' Starts/resumes playback/recording of channel
        '''
        self.bass.ChannelStart(self._handle)
    
    @property
    def position(self, mode:header.BassPosOptions=header.BassPosOptions.BYTE):
        ''' Returns position of channel

        :param mode: Mode of position
        :return: Position of channel
        '''
        return self.bass.ChannelGetPosition(self._handle, mode)
    @position.setter
    #TODO add BASS_MUSIC_xxx flags
    def position(self, value:int, mode:header.BassPosOptions=header.BassPosOptions.BYTE):
        ''' Sets position of channel

        :param value: Position of channel
        :param mode: Mode of position
        '''
        self.bass.ChannelSetPosition(self._handle, value, mode)

    @property
    def length(self, mode:header.BassPosOptions=header.BassPosOptions.BYTE):
        ''' Returns length of channel

        :param mode: Mode of length
        :return: Length of channel
        '''
        return self.bass.ChannelGetLength(self._handle, mode)

    def bytes2seconds(self, bytes:int) -> float:
        ''' Converts bytes to seconds'''
        return self.bass.ChannelBytes2Seconds(self._handle, bytes)
    def seconds2bytes(self, seconds:float):
        ''' Converts seconds to bytes        '''
        return self.bass.ChannelSeconds2Bytes(self._handle, seconds)

    @property
    def volume(self) -> float:
        ''' Returns volume of channel'''
        value = 0.0
        return self.bass.ChannelGetAttribute(self._handle, header.BassChannelOptions.VOL, value)
        return value
    @volume.setter
    def volume(self, value:float):
        ''' Sets volume of channel'''
        self.bass.ChannelSetAttribute(self._handle, header.BassChannelOptions.VOL, value)

    #flags
    #get3dattributes
    #get3dposition
    #getattribute(ex)
    #getdata
    #getdevice
    #info
    #getlength
    #getlevel(ex)
    #gettags
    #isactive
    #issliding
    #lock
    #removedsp
    #removefx
    #removelink
    #removesync
    #set3dattributes
    #set3dpositin
    #setatribute(ex)
    #setdevice
    #setdsp
    #setgx
    #setlink
    #setsync
    #slideattribute
    #update