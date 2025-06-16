# Very simple player module with volume and position control.

from . import BASS
from . import utils
from . import header as bass
from . import structures

class BassPlayer:
    def __init__(self, lib_path:str|None = None):
        ''' BassPlayer\n
        Simple audioplayer using BASS library
        
        :param lib_path: Path to BASS library file (w/ extension)
        :param safe: If == True, the code will raise a `BassExceptions`, if BASS returns error values '''
        #TODO implement auto-find requied .lib
        self.bass = BASS(lib_path, True)
        self._path = None
        self._handle = None
    
    def __delattr__(self, name):
        #Safe closing
        self.bass.__delattr__(name)

#region Settings
    @property
    def Version(self) -> str:
        ''' Get version of BASS library '''
        return utils.decodeVersion(self.bass.GetVersion())

    def DeviceInfo(self, device:int) -> structures.DeviceInfo:
        ''' Get info about certain device 
        
        :return: Device info - name, his flags and driver'''
        #TODO decode flags
        info = bass.BASS_DEVICEINFO()
        self.bass.GetDeviceInfo(device, info)
        return {
            'name' : utils.safeDecode(info.name),
            'flags' : info.flags,
            'driver' : info.driver,}
    
    @property
    def Device(self) -> int: 
        ''' Contain number of current device '''
        return self.bass.GetDevice()
    @Device.setter
    def Device(self, device:int): self.bass.SetDevice(device)

    def IsInit(self) -> int: 
        ''' Returns BASS device status:\n
        `0` - device not started,\n
        `1` - device active,\n
        `2` - device inactive (nothing playing or `Config.dev_nonstop == False`),\n
        `3` [iOS] - app audio interruped, but only if the output was started prior to the interruption.'''
        return self.bass.IsStarted()
    
    def Init(self, device:int, freq:int, flags:int, win:int):
        ''' Initializes an output device 
        
        :param device: The device to use. `-1` = default device, `0` = no sound, `1 - ...` = output device
        :param freq: Output sample rate
        :param flags: A combination of `BASS_DEVICE` flags 
        :param win: The application's main window. `0` = the desktop window (use this for console applications). This is only needed when using DirectSound output
        '''#TODO decode flags
        self.bass.Init(device, freq, flags, win)
    
    def Update(self):
        ''' Updates the audio engine '''
        self.bass.Update()

#region Playback
    @property
    def File(self) -> str:
        ''' Path to current audiofile or stream'''
        return self._path
    @File.setter
    def File(self, path:str):
        if self._path is not None: self.bass.StreamFree(self._handle)
        self._path = None

        os = utils.getOS()
        self._handle = self.bass.StreamCreateFile(False, 
                        path.encode() if os == 'macos' else path,
                        0, -1, 
                        bass.BASS_UNICODE if os == 'windows' else 0)
        self._path = path

    def Play(self):
        ''' Plays loaded file '''
        self.bass.ChannelPlay(self._handle, False)

    def Stop(self):
        ''' Stops playing file '''
        self.bass.ChannelStop(self._handle)

    @property
    def Position(self) -> int:
        ''' Position of playback (in bytes)'''
        return self.bass.ChannelGetPosition(self._handle, 0)
    @Position.setter
    def Position(self, bytes:int):
        self.bass.ChannelSetPosition(self._handle, bytes, 0)
    
    @property
    def Lenght(self) -> int:
        ''' Lenght of loaded file '''
        return self.bass.ChannelGetLength(self._handle, 0)

    def TimeConvert(self, value:int|float) -> int|float:
        ''' Converts bytes (int) <-> seconds (float) '''
        if isinstance(value, int): 
              return self.bass.ChannelBytes2Seconds(self._handle, value)
        else: return self.bass.ChannelSeconds2Bytes(self._handle, value)

    @property
    def Volume(self) -> float:
        ''' Playback volume (0.0 - 1.0)'''
        val = bass.FLOAT()
        self.bass.ChannelGetAttribute(self._handle, bass.BASS_ATTRIB_VOL, val)
        return val.value
    @Volume.setter
    def Volume(self, volume:float):
        val = bass.FLOAT(); val.value = volume
        self.bass.ChannelSetAttribute(self._handle, bass.BASS_ATTRIB_VOL, val)
