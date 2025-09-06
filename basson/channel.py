from .basson import Basson
from . import api, header

class Channel():
    def __init__(self, bass:Basson, handle:int):
        self.bass = bass.bass
        ''' Current BASS library'''
        self.HANDLE = handle
        ''' Contain handle of current channel. Uses for any interaction with channel '''
        self.WHOAMI:api.ChannelType = None
        ''' Tells that a object is '''

        raise TypeError("This class cannot be created directly. Use Streams, Music, Samples for creating this object")

        
    def __delattr__(self, name):
        self.bass.ChannelFree(self.HANDLE)

#region Core functions
    def bytes2seconds(self, bytes:int) -> float:
        ''' Converts bytes to seconds'''
        return self.bass.ChannelBytes2Seconds(self.HANDLE, bytes)
    def seconds2bytes(self, seconds:float):
        ''' Converts seconds to bytes'''
        return self.bass.ChannelSeconds2Bytes(self.HANDLE, seconds)

    #get3dattributes
    #get3dposition

    #def get_data(self, buffer:bytearray, length:api.DataLengthOption|api.DataFlag|int):
    #    ''' Retrieves the immediate sample data (or an FFT representation of it) of a sample channel, stream, MOD music, or recording channel.'''
    #    c_buffer = buffer
    #    self.bass.ChannelGetData(self.HANDLE, c_buffer, length)
    #    return c_buffer

    @property
    def device(self) -> int:
        ''' Number of system device, in usage by this channel

        :param device: Device to use\n
            * `0` - no sound
            * `1...` - audio device   
            * `CommonFlag.NODEVICE` - no device
        :raise BASSError.code == DEVICE: `device` is invalid
        :raise BASSError.code == INIT: Requested device has not been initialized
        :raise BASSError.code == NOTAVAIL: Only decoding channels are allowed to use the `CommonFlag.NODEVICE` option
        '''
        return self.bass.ChannelGetDevice(self.HANDLE)
    @device.setter
    def device(self, device:int):
        self.bass.ChannelSetDevice(self.HANDLE, device)

    @property
    def length(self, mode:api.PosModeOption=0):
        ''' Returns length of channel

        :param mode: Mode of length
        :return: Length of channel
        '''
        return self.bass.ChannelGetLength(self.HANDLE, mode)

    # level (LevelEx)

    @property
    def position(self, mode:api.PosModeOption=0):
        ''' Returns position of channel

        :param mode: Mode of position
        :return: Position of channel
        '''
        return self.bass.ChannelGetPosition(self.HANDLE, mode)
    @position.setter
    #TODO add BASS_MUSIC_xxx flags
    def position(self, value:int, mode:api.PosModeOption=0):
        ''' Sets position of channel

        :param value: Position of channel
        :param mode: Mode of position
        '''
        self.bass.ChannelSetPosition(self.HANDLE, value, mode)

    @property
    def status(self):
        #TODO what this return? flag?
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
        except api.BASSError as e:
            if e.code == api.BASSError.START:
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
    def _getconf(self, option):
        value = header.FLOAT()
        self.bass.ChannelGetAttribute(self.HANDLE, option, value)
        return value.value
    def _setconf(self, option, value):
        self.bass.ChannelSetAttribute(self.HANDLE, option, value)

    @property
    def bitrate(self) -> float:
        ''' The average bitrate of a file stream '''
        return self._getconf(api.ChannelOption.BITRATE)

    @property
    def buffer(self) -> float:
        ''' The playback buffering length in seconds.\n
        `0` = no buffering. This is automatically capped to the full length of the channel's playback buffer
        '''
        return self._getconf(api.ChannelOption.BUFFER)
    @buffer.setter
    def buffer(self, value:float):
        self._setconf(api.ChannelOption.BUFFER, value)

    @property
    def cpu(self) -> float:
        ''' The CPU usage of a channel in %'''
        return self._getconf(api.ChannelOption.CPU)

    @property
    def frequency(self) -> float:
        ''' The sample rate of a channel\n
        `0` - original rate'''
        return self._getconf(api.ChannelOption.FREQ)
    @frequency.setter
    def frequency(self, value:float):
        self._setconf(api.ChannelOption.FREQ, value)

    @property
    def granule(self) -> float:
        ''' The processing granularity of a channel '''
        try:
            return self._getconf(api.ChannelOption.GRANULE)
        except api.BASSError as e:
            if e.code == 0: return None
    @granule.setter
    def granule(self, value:float):
        self._setconf( api.ChannelOption.GRANULE, value)
        
    @property
    def music_active(self) -> float:
        ''' The number of active channels in a MOD music '''
        return self._getconf(api.ChannelOption.MUSIC_ACTIVE)

    @property
    def music_amplify(self) -> int:
        ''' The amplification level of a MOD music '''
        return int(self._getconf(api.ChannelOption.MUSIC_AMPLIFY))
    @music_amplify.setter
    def music_amplify(self, value:int):
        self._setconf(api.ChannelOption.MUSIC_AMPLIFY, value)

    @property
    def music_bpm(self) -> int:
        ''' The BPM of a MOD music '''
        return int(self._getconf(api.ChannelOption.MUSIC_BPM))
    @music_bpm.setter
    def music_bpm(self, value:int):
        self._setconf(api.ChannelOption.MUSIC_BPM, value)
    
    @property
    def music_pansep(self) -> int:
        ''' The pan separation of a MOD music '''
        return int(self._getconf(api.ChannelOption.MUSIC_PANSEP))
    @music_pansep.setter
    def music_pansep(self, value:int):
        self._setconf(api.ChannelOption.MUSIC_PANSEP, value)
    
    @property
    def music_position_scaler(self) -> int:
        ''' The position scaler of a MOD music '''
        return int(self._getconf(api.ChannelOption.MUSIC_PSCALER))
    @music_position_scaler.setter
    def music_position_scaler(self, value:int):
        self._setconf(api.ChannelOption.MUSIC_PSCALER, value)
    
    @property
    def music_speed(self) -> int:
        ''' The speed of a MOD music '''
        return int(self._getconf(api.ChannelOption.MUSIC_SPEED))
    @music_speed.setter
    def music_speed(self, value:int):
        self._setconf(api.ChannelOption.MUSIC_SPEED, value)
    
    @property
    def music_volume_channel(self, channel:int) -> float:
        ''' The volume of a certain channel in MOD music\n
        :param channel: Number of channel, where `0` - first channel
        :param volume: Volume level'''
        return self._getconf(api.ChannelOption.MUSIC_VOL_CHAN + channel)
    @music_volume_channel.setter
    def music_volume_channel(self, channel:int, volume:float):
        self._setconf(api.ChannelOption.MUSIC_VOL_CHAN + channel, volume)
    
    @property
    def music_volume(self) -> int:
        ''' The global volume of a MOD music '''
        return int(self._getconf(api.ChannelOption.MUSIC_VOL_GLOBAL))
    @music_volume.setter
    def music_volume(self, value:int):
        self._setconf(api.ChannelOption.MUSIC_VOL_GLOBAL, value)

    @property
    def music_volume_instrument(self, instrument:int) -> float:
        '''Volume level of instrument of a MOD music\n
        :param instument: Number of instrument, where `0` - first instrument
        :param value: Volume level'''
        return self._getconf(header.ChannelOption.MUSIC_VOL_INST + instrument)
    @music_volume_instrument.setter
    def music_volume_instrument(self, instrument:int, volume:float):
        self._selfconf(header.ChannelOption.MUSIC_VOL_INST+instrument, volume)

    @property
    def net_resume(self) -> float:
        ''' The download buffer level required to resume stalled playback, in % '''
        return self._getconf(api.ChannelOption.NET_RESUME)
    @net_resume.setter
    def net_resume(self, value:float):
        self._setconf(api.ChannelOption.NET_RESUME, value)
    
    @property
    def noramp(self) -> header.NorampOption:
        ''' Enable or disable playback ramping '''
        #HACK On some reason for `noramp` and `pan`, if we don't touched yet, BASS_ChannelGetAttribute will return False 
        #   but BASS_ErrorGetCode says OK. So need to exclude raising exception in this situation
        try:
            return int(self._getconf(api.ChannelOption.NORAMP))
        except api.BASSError as e:
            if e.code == api.BASSError.OK:
                return header.NorampOption.ENABLE # default value
            else:
                raise e
    @noramp.setter
    def noramp(self, value:header.NorampOption):
        self._setconf(api.ChannelOption.NORAMP, value)
    
    @property
    def pan(self) -> float:
        ''' The panning position of a channel '''
        #HACK look at `noramp` comment
        try:
            return self._getconf( api.ChannelOption.PAN)
        except api.BASSError as e:
            if e.code == api.BASSError.OK:
                return 0.0 # default value
            else:
                raise e
    @pan.setter
    def pan(self, value:float):
        self._setconf(api.ChannelOption.PAN, value)

    @property
    def push_limit(self) -> int:
        ''' The maximum amount of data that a push stream can have queued '''
        return int(self._getconf(api.ChannelOption.PUSH_LIMIT))
    @push_limit.setter
    def push_limit(self, value:int):
        self._setconf(api.ChannelOption.PUSH_LIMIT, value)
    
    @property
    def src(self) -> header.SamplerateConversionOption:
        ''' The sample rate conversion quality of a channel '''
        return int(self._getconf(api.ChannelOption.SRC))
    @src.setter
    def src(self, value:header.SamplerateConversionOption):
        self._setconf(api.ChannelOption.SRC, value)
    
    @property
    def tail(self) -> float:
        ''' An amount of time to add to the length of a channel '''
        return self._getconf(api.ChannelOption.TAIL)
    @tail.setter
    def tail(self, value:float):
        self._setconf(api.ChannelOption.TAIL, value)

    @property
    def volume(self) -> float:
        ''' Volume of channel '''
        return self._getconf( api.ChannelOption.VOL)
    @volume.setter
    def volume(self, value:float):
        self._setconf( api.ChannelOption.VOL, value)

    @property
    def dsp_volume(self) -> float:
        ''' The volume level applied in the DSP chain of a channel '''
        return self._getconf( api.ChannelOption.VOLDSP)
    @dsp_volume.setter
    def dsp_volume(self, value:float):
        self._setconf( api.ChannelOption.VOLDSP, value)

    @property
    def dsp_volume_priority(self) -> int:
        ''' The priority of the volume DSP '''
        return int(self._getconf(api.ChannelOption.VOLDSP_PRIORITY))
    @dsp_volume_priority.setter
    def dsp_volume_priority(self, value:int):
        self._setconf(api.ChannelOption.VOLDSP_PRIORITY, value)

    # atrribute DownloadCallback #TODO поскольку работаем в python и мы будем сами писать эти callback, то вызов атрибута скорее всего не понадобится

    # atribute scaninfo

    # atribute user