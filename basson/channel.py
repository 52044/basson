from .api import header
from .api.api import BassException
from . import BASS

class Channel():
    def __init__(self, bass:BASS, handle:int):
        self.bass = bass.bass
        ''' Current BASS library'''
        self.HANDLE = handle
        ''' Contain handle of current channel. Uses for any interaction with channel '''
        self.WHOAMI:header.BassChannelType = None
        ''' Tells that a object is '''

        raise TypeError("This class cannot be created directly. Use Streams, Music, Samples for creating this object")

        
    def __delattr__(self, name):
        self.bass.ChannelFree(self.HANDLE)

#region Core functions
    def bytes2seconds(self, bytes:int) -> float:
        ''' Converts bytes to seconds'''
        return self.bass.ChannelBytes2Seconds(self.HANDLE, bytes)
    def seconds2bytes(self, seconds:float):
        ''' Converts seconds to bytes        '''
        return self.bass.ChannelSeconds2Bytes(self.HANDLE, seconds)

    #get3dattributes
    #get3dposition

    def get_data(self, buffer:bytearray, length:header.DataLengthOptions|header.DataFlags|int):
        ''' Retrieves the immediate sample data (or an FFT representation of it) of a sample channel, stream, MOD music, or recording channel.'''
        c_buffer = buffer
        self.bass.ChannelGetData(self.HANDLE, c_buffer, length)
        return c_buffer

    @property
    def device(self) -> int:
        ''' Number of system device, in usage by this channel '''
        return self.bass.ChannelGetDevice(self.HANDLE)
    @device.setter
    def device(self, device:int):
        self.bass.ChannelSetDevice(self.HANDLE, device)

    @property
    def length(self, mode:header.PosOptions=header.PosOptions.BYTE):
        ''' Returns length of channel

        :param mode: Mode of length
        :return: Length of channel
        '''
        return self.bass.ChannelGetLength(self.HANDLE, mode)

    # level (LevelEx)

    @property
    def position(self, mode:header.PosOptions=header.PosOptions.BYTE):
        ''' Returns position of channel

        :param mode: Mode of position
        :return: Position of channel
        '''
        return self.bass.ChannelGetPosition(self.HANDLE, mode)
    @position.setter
    #TODO add BASS_MUSIC_xxx flags
    def position(self, value:int, mode:header.PosOptions=header.PosOptions.BYTE):
        ''' Sets position of channel

        :param value: Position of channel
        :param mode: Mode of position
        '''
        self.bass.ChannelSetPosition(self.HANDLE, value, mode)

    @property
    def status(self):
        ''' Checks if a sample, stream, or MOD music is active (playing) or stalled. Can also check if a recording is in progress. '''
        return self.bass.ChannelIsActive(self.HANDLE)
    
    # IsSliding
    # SlideAtrribute

    def lock(self, lock:bool):
        ''' Locks a channel '''
        self.bass.ChannelLock(self.HANDLE, lock)

    def play(self, restart: bool = False):
        ''' Starts/resumes playback of channel. Same as `start`, but have option start from begining
        
        :param restart: Start playback from begin
        '''
        try:
            self.bass.ChannelPlay(self.HANDLE, restart)
        except BassException as e:
            if e.code == BassException.START:
                self.start()
            else:
                raise e
            
    def pause(self):
        ''' Pauses playback/recording of channel
        '''
        self.bass.ChannelPause(self.HANDLE)

    def stop(self):
        ''' Stops playback/recording of channel
        '''
        self.bass.ChannelStop(self.HANDLE)   

    def start(self):
        ''' Starts/resumes playback/recording of channel
        '''
        self.bass.ChannelStart(self.HANDLE)

    #set/removeDSP
    #set/removeFX
    #set/removeLink
    #set/removeSync
    
# endregion

# region ChannelGetAttibute(ex)
#FIXME нужно писать в value, в возращатся результат выполнения, сейчас пока колхоз
    @property
    def bitrate(self) -> int:
        ''' The average bitrate of a file stream 
        
        :raises ValueError: This channel is not a `Stream`
        '''
        if self.WHOAMI is not header.ChannelType.STREAM:
            raise ValueError('Bitrate is not available for this channel')
        return int(self.bass.ChannelGetAttribute(self.HANDLE, header.ChannelOptions.BITRATE, 0))

    @property
    def buffer(self) -> int:
        ''' The playback buffering length in seconds.\n
        `0` = no buffering. This is automatically capped to the full length of the channel's playback buffer
        '''
        if self.WHOAMI is not header.ChannelType.STREAM or self.WHOAMI is not header.ChannelType.MUSIC:
            raise ValueError('Buffer is not available for this channel')
        return int(self.bass.ChannelGetAttribute(self.HANDLE, header.ChannelOptions.BUFFER, 0))
    @buffer.setter
    def buffer(self, value:int):
        self.bass.ChannelSetAttribute(self.HANDLE, header.ChannelOptions.BUFFER, value)

    @property
    def cpu(self) -> float:
        ''' The CPU usage of a channel in percent.

        :raises ValueError: This channel is not a `Stream` or `Music`
        '''
        if self.WHOAMI is not header.ChannelType.STREAM or self.WHOAMI is not header.ChannelType.MUSIC:
            raise ValueError('CPU is not available for this channel')
        return self.bass.ChannelGetAttribute(self.HANDLE, header.ChannelOptions.CPU, 0)

    @property
    def frequency(self) -> int:
        ''' The sample rate of a channel'''
        return int(self.bass.ChannelGetAttribute(self.HANDLE, header.ChannelOptions.FREQ, 0))
    @frequency.setter
    def frequency(self, value:int):
        self.bass.ChannelSetAttribute(self.HANDLE, header.ChannelOptions.FREQ, value)

    @property
    def samplerate(self) -> int:
        ''' The sample rate of a channel.\n
        Same as `frequency`

        :raises ValueError: This channel is not a `Stream` or `Music`
        '''
        return self.frequency

    @property
    def granule(self) -> float:
        ''' The processing granularity of a channel '''
        if (
            self.WHOAMI is not header.ChannelType.STREAM or
            self.WHOAMI is not header.ChannelType.MUSIC or
            self.WHOAMI is not header.ChannelType.RECORD
        ):
            raise ValueError('Granule is not available for this channel')
        return self.bass.ChannelGetAttribute(self.HANDLE, header.ChannelOptions.GRANULE, 0)
    @granule.setter
    def granule(self, value:float):
        self.bass.ChannelSetAttribute(self.HANDLE, header.ChannelOptions.GRANULE, value)
        
    @property
    def music_active(self) -> int:
        ''' The number of active channels in a MOD music '''
        if (self.WHOAMI is not header.ChannelType.MUSIC):
            raise ValueError('Music Active is not available for this channel')
        return self.bass.ChannelGetAttribute(self.HANDLE, header.ChannelOptions.MUSIC_ACTIVE, 0)

    @property
    def music_amplify(self) -> float:
        ''' The amplification level of a MOD music '''
        if (self.WHOAMI is not header.ChannelType.MUSIC):
            raise ValueError('Music Amplify is not available for this channel')
        return self.bass.ChannelGetAttribute(self.HANDLE, header.ChannelOptions.MUSIC_AMPLIFY, 0)
    @music_amplify.setter
    def music_amplify(self, value:float):
        self.bass.ChannelSetAttribute(self.HANDLE, header.ChannelOptions.MUSIC_AMPLIFY, value)

    @property
    def music_bpm(self) -> int:
        ''' The BPM of a MOD music '''
        if (self.WHOAMI is not header.ChannelType.MUSIC):
            raise ValueError('Music BPM is not available for this channel')
        return int(self.bass.ChannelGetAttribute(self.HANDLE, header.ChannelOptions.MUSIC_BPM, 0))
    @music_bpm.setter
    def music_bpm(self, value:int):
        self.bass.ChannelSetAttribute(self.HANDLE, header.ChannelOptions.MUSIC_BPM, value)
    
    @property
    def music_pansep(self) -> int:
        ''' The pan separation of a MOD music '''
        if (self.WHOAMI is not header.ChannelType.MUSIC):
            raise ValueError('Music PanSep is not available for this channel')
        return int(self.bass.ChannelGetAttribute(self.HANDLE, header.ChannelOptions.MUSIC_PANSEP, 0))
    @music_pansep.setter
    def music_pansep(self, value:int):
        self.bass.ChannelSetAttribute(self.HANDLE, header.ChannelOptions.MUSIC_PANSEP, value)
    
    @property
    def music_position_scaler(self) -> int:
        ''' The position scaler of a MOD music '''
        if (self.WHOAMI is not header.ChannelType.MUSIC):
            raise ValueError('Music Position Scaler is not available for this channel')
        return int(self.bass.ChannelGetAttribute(self.HANDLE, header.ChannelOptions.MUSIC_PSCALER, 0))
    @music_position_scaler.setter
    def music_position_scaler(self, value:int):
        self.bass.ChannelSetAttribute(self.HANDLE, header.ChannelOptions.MUSIC_PSCALER, value)
    
    @property
    def music_speed(self) -> int:
        ''' The speed of a MOD music '''
        if (self.WHOAMI is not header.ChannelType.MUSIC):
            raise ValueError('Music Speed is not available for this channel')
        return int(self.bass.ChannelGetAttribute(self.HANDLE, header.ChannelOptions.MUSIC_SPEED, 0))
    @music_speed.setter
    def music_speed(self, value:int):
        self.bass.ChannelSetAttribute(self.HANDLE, header.ChannelOptions.MUSIC_SPEED, value)
    
    @property
    def music_volume_channel(self) -> float:
        ''' The volume of a certain channel in MOD music '''
        if (self.WHOAMI is not header.ChannelType.MUSIC):
            raise ValueError('Music Volume Channel is not available for this channel')
        return self.bass.ChannelGetAttribute(self.HANDLE, header.ChannelOptions.MUSIC_VOL_CHAN, 0)
    @music_volume_channel.setter
    def music_volume_channel(self, value:float):
        self.bass.ChannelSetAttribute(self.HANDLE, header.ChannelOptions.MUSIC_VOL_CHAN, value)
    
    @property
    def music_volume(self) -> int:
        ''' The global volume of a MOD music '''
        if (self.WHOAMI is not header.ChannelType.MUSIC):
            raise ValueError('Music Volume is not available for this channel')
        return int(self.bass.ChannelGetAttribute(self.HANDLE, header.ChannelOptions.MUSIC_VOL_GLOBAL, 0))
    @music_volume.setter
    def music_volume(self, value:int):
        self.bass.ChannelSetAttribute(self.HANDLE, header.ChannelOptions.MUSIC_VOL_GLOBAL, value)

    @property
    def net_resume(self) -> int:
        ''' The download buffer level required to resume stalled playback. '''
        if (self.WHOAMI is not header.ChannelType.STREAM):
            raise ValueError('Net Resume is not available for this channel')
        return int(self.bass.ChannelGetAttribute(self.HANDLE, header.ChannelOptions.NET_RESUME, 0))
    @net_resume.setter
    def net_resume(self, value:int):
        self.bass.ChannelSetAttribute(self.HANDLE, header.ChannelOptions.NET_RESUME, value)
    
    @property
    def noramp(self) -> int:
        ''' The number of times a channel has been played. '''
        if (self.WHOAMI is not header.ChannelType.STREAM):
            raise ValueError('No Ramp is not available for this channel')
        return int(self.bass.ChannelGetAttribute(self.HANDLE, header.ChannelOptions.NO_RAMP, 0))
    @noramp.setter
    def noramp(self, value:int):
        self.bass.ChannelSetAttribute(self.HANDLE, header.ChannelOptions.NO_RAMP, value)
    
    @property
    def pan(self) -> float:
        ''' The panning position of a channel '''
        return self.bass.ChannelGetAttribute(self.HANDLE, header.ChannelOptions.PAN, 0.0)
    @pan.setter
    def pan(self, value:float):
        self.bass.ChannelSetAttribute(self.HANDLE, header.ChannelOptions.PAN, value)

    @property
    def push_limit(self) -> int:
        ''' The maximum amount of data that a push stream can have queued '''
        if (self.WHOAMI is not header.ChannelType.STREAM):
            raise ValueError('Push Limit is not available for this channel')
        return int(self.bass.ChannelGetAttribute(self.HANDLE, header.ChannelOptions.PUSH_LIMIT, 0))
    @push_limit.setter
    def push_limit(self, value:int):
        self.bass.ChannelSetAttribute(self.HANDLE, header.ChannelOptions.PUSH_LIMIT, value)
    
    @property
    def src(self) -> int:
        ''' The sample rate conversion quality of a channel ''' #TODO flaggs
        return int(self.bass.ChannelGetAttribute(self.HANDLE, header.ChannelOptions.SRC, 0))
    @src.setter
    def src(self, value:int):
        self.bass.ChannelSetAttribute(self.HANDLE, header.ChannelOptions.SRC, value)
    
    @property
    def tail(self) -> float:
        ''' An amount of time to add to the length of a channel '''
        return self.bass.ChannelGetAttribute(self.HANDLE, header.ChannelOptions.TAIL, 0.0)
    @tail.setter
    def tail(self, value:float):
        self.bass.ChannelSetAttribute(self.HANDLE, header.ChannelOptions.TAIL, value)

    @property
    def volume(self) -> float:
        ''' Returns volume of channel '''
        return self.bass.ChannelGetAttribute(self.HANDLE, header.ChannelOptions.VOL, 0.0)
    @volume.setter
    def volume(self, value:float):
        ''' Sets volume of channel'''
        self.bass.ChannelSetAttribute(self.HANDLE, header.ChannelOptions.VOL, value)

    @property
    def dsp_volume(self) -> float:
        ''' The volume level applied in the DSP chain of a channel '''
        return self.bass.ChannelGetAttribute(self.HANDLE, header.ChannelOptions.VOLDSP, 0.0)
    @dsp_volume.setter
    def dsp_volume(self, value:float):
        self.bass.ChannelSetAttribute(self.HANDLE, header.ChannelOptions.VOLDSP, value)

    @property
    def dsp_volume_priority(self) -> int:
        ''' The priority of the volume DSP '''
        return int(self.bass.ChannelGetAttribute(self.HANDLE, header.ChannelOptions.VOLDSP_PRIORITY, 0))
    @dsp_volume_priority.setter
    def dsp_volume_priority(self, value:int):
        self.bass.ChannelSetAttribute(self.HANDLE, header.ChannelOptions.VOLDSP_PRIORITY, value)

    # atrribute DownloadCallback #TODO поскольку работаем в python и мы будем сами писать эти callback, то вызов атрибута скорее всего не понадобится

    # atribute scaninfo

    # atribute user