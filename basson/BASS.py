from .api import api
from .api import header
from . import structures

class BASS():
    def __init__(self, dll_path:str|None=None):
        ''' Python-frendly wrapper over BASS library
        
        :param dll_path: Path to BASS dll
        :param safe_execution: If BASS after execution command returns `error` value, code will raise exception'''

        if dll_path == None: raise NotImplementedError('Autodetection of dll is not implemented yet.')#TODO
        self.bass = api.BASS(dll_path, True)
        
        self.config = structures.BassConfig(self.bass)

    def __delattr__(self, name):
        #Safe closing
        self.bass.__delattr__(name)

    @property
    def error_code(self) -> int:
        ''' Returns error code for the last recent BASS function call'''
        return self.bass.ErrorGetCode()

    @property
    def cpu_usage(self) -> float:
        ''' CPU usage of BASS library '''
        return self.bass.GetCPU()
    
    @property
    def device(self) -> int:
        ''' Number of current audio device '''
        return self.bass.GetDevice()
    @device.setter
    def device(self, number:int): 
        self.bass.SetDevice(number)

    @property
    def volume(self) -> float:
        ''' Master (system) volume level '''
        return self.bass.GetVolume()
    @volume.setter
    def volume(self, level:float):
        self.bass.SetVolume(level)

    @property
    def version(self) -> int:
        ''' Version of loaded BASS library\n
        For human redability please use `basson.utils.decode_version(int)`'''
        return self.bass.GetVersion()

    def pause(self):
        ''' Stops output, pausing all handles (music/samples/streams) '''
        self.bass.Pause()

    def start(self):
        ''' Starts/resumes output '''
        self.bass.Start()
    
    def stop(self):
        ''' Stops output, stops all handles (music/samples/streams)'''
        self.bass.Stop()

    def update(self, length:int):
        ''' Updates `HStream` and `HMusic` channels playback buffers
        
        :param length: Amount of data to render, in ms'''
        self.bass.Update(length)
    
    def init(self, device:int, samplerate:int, flags:header.BassDeviceFlags):
        ''' Initialize output device 
        
        :param device: Number of desirable audio device.\n
            Set to `-1` to default device, `0` - no output
        :param samplerate: Samplerate of output audiostreams
        :param flags: Combinations of `BassDeviceFlags`'''
        self.bass.Init(device, samplerate, flags, 0, None)

    @property
    def status(self) -> header.BassStatusOptions:
        ''' Status of output device '''
        return self.bass.IsStarted()
    
    #getdeviceinfo
    #getinfo
#endregion