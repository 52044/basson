from typing import TypedDict

from .api import header 

class DeviceInfo(TypedDict):
    ''' Dictionary for using with `Device` and `RecordDevice` properties'''
    name: str
    ''' Description of the device '''
    flags: header.DeviceFlags
    ''' The device's current status, a combination of flags''' #TODO describe flags
    driver: str 
    ''' Driver identification '''

class Info(TypedDict):
    ''' Dictionary for using with `Info` property'''
    flags: header.DeviceFlags
    ''' The device's DirectSound capabilities, a combination of flags''' #TODO describe flags
    minbuf: int
    ''' The minimum buffer length (rounded up to the nearest millisecond) to avoid stuttering playback '''
    dsver: header.DXVersionOptions
    '''DirectSound version.\n 
    `9` = DX9/8/7/5 features are available,\n 
    `8` = DX8/7/5 features are available,\n 
    `7` = DX7/5 features are available,\n 
    `5` = DX5 features are available,\n 
    `0` = none of the DX9/8/7/5 features are available'''
    latency: int
    ''' The average delay (rounded up to the nearest millisecond) for channel playback to start and be heard '''
    initflags: header.DeviceFlags
    ''' The flags parameter of the `Init` call. This will include any flags that were applied automatically'''
    speakers: int
    ''' The number of available speakers, which can be accessed via the speaker assignment flags '''
    freq: int
    ''' The output rate '''

class ChannelInfo(TypedDict):
    ''' Dictionary for using with `ChannelInfo` property'''
    freq:int
    ''' Default samplerate'''
    chans:int
    ''' Number of channels'''

