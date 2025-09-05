"""
This file contains all API for BASS library
"""

from .header import *

BASSAPI = 0x204
""" BASS API version """

#region BASS instance
class BASS:
    """ BASS API provider"""
    def __init__(self, dll_path:str, safe=True):
        """ Creates a new instance of the BASS library\n
        * On Windows, use `BASS.dll`
        * On MacOS, use `libbass.dylib`
        * On Linux, use `libbass.so`
        
        :param dll_path: Path to the BASS library. 
        :param safe: If True, wrapper will be raise errors, if BASS returns an error value
        """

        # Load the library
        from . import utils
        match utils.get_os():
            case 'windows':
                self.dll = ctypes.WinDLL(dll_path)
                """ `ctypes` library object"""
            case 'macos':
                self.dll = ctypes.CDLL(dll_path)
            case 'linux':
                self.dll = ctypes.CDLL(dll_path)
            case _:
                raise OSError('Unsupported OS')
        
        # Define the functions
        self._define_functions()

        self.safe = safe
        """ If True, wrapper will be raise errors, if BASS returns an error value"""

    def _define_functions(self):
        """ Defines the functions of the BASS library """

        # BASS / Config
        self.dll.BASS_GetConfig.argtypes = [DWORD]
        self.dll.BASS_GetConfig.restype = DWORD

        self.dll.BASS_GetConfigPtr.argtypes = [DWORD]
        self.dll.BASS_GetConfigPtr.restype = PTR

        self.dll.BASS_SetConfig.argtypes = [DWORD, DWORD]
        self.dll.BASS_SetConfig.restype = BOOL

        self.dll.BASS_SetConfigPtr.argtypes = [DWORD, PTR]
        self.dll.BASS_SetConfigPtr.restype = BOOL

        # BASS / Plugins
        self.dll.BASS_PluginEnable.argtypes = [HPLUGIN, BOOL]
        self.dll.BASS_PluginEnable.restype = BOOL

        self.dll.BASS_PluginFree.argtypes = [HPLUGIN]
        self.dll.BASS_PluginFree.restype = BOOL

        self.dll.BASS_PluginGetInfo.argtypes = [HPLUGIN]
        self.dll.BASS_PluginGetInfo.restype = ctypes.POINTER(BASS_PLUGININFO)

        self.dll.BASS_PluginLoad.argtypes = [CHARP, DWORD]
        self.dll.BASS_PluginLoad.restype = DWORD

        # BASS /  Initialization, info, etc...
        self.dll.BASS_ErrorGetCode.argtypes = []
        self.dll.BASS_ErrorGetCode.restype = INT

        self.dll.BASS_Free.argtypes = []
        self.dll.BASS_Free.restype = BOOL
        
        self.dll.BASS_GetCPU.argtypes = []
        self.dll.BASS_GetCPU.restype = FLOAT

        self.dll.BASS_GetDevice.argtypes = []
        self.dll.BASS_GetDevice.restype = DWORD

        self.dll.BASS_GetDeviceInfo.argtypes = [DWORD, ctypes.POINTER(BASS_DEVICEINFO)]
        self.dll.BASS_GetDeviceInfo.restype = BOOL

        self.dll.BASS_GetInfo.argtypes = [ctypes.POINTER(BASS_INFO)]
        self.dll.BASS_GetInfo.restype = BOOL

        self.dll.BASS_GetVersion.argtypes = []
        self.dll.BASS_GetVersion.restype = DWORD
        
        self.dll.BASS_GetVolume.argtypes = []
        self.dll.BASS_GetVolume.restype = FLOAT

        self.dll.BASS_Init.argtypes = [INT, DWORD, DWORD, PTR, PTR]
        self.dll.BASS_Init.restype = BOOL
        
        self.dll.BASS_IsStarted.argtypes = []
        self.dll.BASS_IsStarted.restype = DWORD

        self.dll.BASS_Pause.argtypes = []
        self.dll.BASS_Pause.restype = BOOL

        self.dll.BASS_SetDevice.argtypes = [DWORD]
        self.dll.BASS_SetDevice.restype = BOOL

        self.dll.BASS_SetVolume.argtypes = [FLOAT]
        self.dll.BASS_SetVolume.restype = BOOL

        self.dll.BASS_Start.argtypes = []
        self.dll.BASS_Start.restype = BOOL

        self.dll.BASS_Stop.argtypes = []
        self.dll.BASS_Stop.restype = BOOL

        self.dll.BASS_Update.argtypes = [DWORD]
        self.dll.BASS_Update.restype = BOOL

        # BASS / 3D
        self.dll.BASS_Apply3D.argtypes = []
        self.dll.BASS_Apply3D.restype = None

        self.dll.BASS_Get3DFactors.argtypes = [ctypes.POINTER(FLOAT), ctypes.POINTER(FLOAT), ctypes.POINTER(FLOAT)]
        self.dll.BASS_Get3DFactors.restype = BOOL

        self.dll.BASS_Get3DPosition.argtypes = [ctypes.POINTER(BASS_3DVECTOR), ctypes.POINTER(BASS_3DVECTOR), ctypes.POINTER(BASS_3DVECTOR), ctypes.POINTER(BASS_3DVECTOR)]
        self.dll.BASS_Get3DPosition.restype = BOOL

        self.dll.BASS_Set3DFactors.argtypes = [FLOAT, FLOAT, FLOAT]
        self.dll.BASS_Set3DFactors.restype = BOOL

        self.dll.BASS_Set3DPosition.argtypes = [ctypes.POINTER(BASS_3DVECTOR), ctypes.POINTER(BASS_3DVECTOR), ctypes.POINTER(BASS_3DVECTOR), ctypes.POINTER(BASS_3DVECTOR)]
        self.dll.BASS_Set3DPosition.restype = BOOL

        # BASS / Samples
        self.dll.BASS_SampleCreate.argtypes = [DWORD, DWORD, DWORD, DWORD, DWORD]
        self.dll.BASS_SampleCreate.restype = HSAMPLE

        self.dll.BASS_SampleFree.argtypes = [HSAMPLE]
        self.dll.BASS_SampleFree.restype = BOOL

        self.dll.BASS_SampleGetChannel.argtypes = [HSAMPLE, DWORD]
        self.dll.BASS_SampleGetChannel.restype = DWORD

        self.dll.BASS_SampleGetChannels.argtypes = [HSAMPLE, HCHANNEL]
        self.dll.BASS_SampleGetChannels.restype = DWORD

        self.dll.BASS_SampleGetData.argtypes = [HSAMPLE, PTR]
        self.dll.BASS_SampleGetData.restype = BOOL

        self.dll.BASS_SampleGetInfo.argtypes = [HSAMPLE, ctypes.POINTER(BASS_SAMPLE)]
        self.dll.BASS_SampleGetInfo.restype = BOOL

        self.dll.BASS_SampleLoad.argtypes = [BOOL, PTR, QWORD, DWORD, DWORD, DWORD]
        self.dll.BASS_SampleLoad.restype = HSAMPLE

        self.dll.BASS_SampleSetData.argtypes = [HSAMPLE, PTR]
        self.dll.BASS_SampleSetData.restype = BOOL

        self.dll.BASS_SampleSetInfo.argtypes = [HSAMPLE, ctypes.POINTER(BASS_SAMPLE)]
        self.dll.BASS_SampleSetInfo.restype = BOOL

        self.dll.BASS_SampleStop.argtypes = [HSAMPLE]
        self.dll.BASS_SampleStop.restype = BOOL

        # BASS / Streams
        self.dll.BASS_StreamCreate.argtypes = [DWORD, DWORD, DWORD, STREAMPROC, PTR]
        self.dll.BASS_StreamCreate.restype = HSTREAM

        self.dll.BASS_StreamCreateFile.argtypes = [BOOL, PTR, QWORD, QWORD, DWORD]
        self.dll.BASS_StreamCreateFile.restype = HSTREAM

        self.dll.BASS_StreamCreateFileUser.argtypes = [DWORD, DWORD, ctypes.POINTER(BASS_FILEPROCS), PTR]
        self.dll.BASS_StreamCreateFileUser.restype = HSTREAM

        self.dll.BASS_StreamCreateURL.argtypes = [CHARP, DWORD, DWORD, ctypes.POINTER(DOWNLOADPROC), PTR]
        self.dll.BASS_StreamCreateURL.restype = HSTREAM

        self.dll.BASS_StreamFree.argtypes = [HSTREAM]
        self.dll.BASS_StreamFree.restype = BOOL

        self.dll.BASS_StreamGetFilePosition.argtypes = [HSTREAM, DWORD]
        self.dll.BASS_StreamGetFilePosition.restype = QWORD

        self.dll.BASS_StreamPutData.argtypes = [HSTREAM, PTR, DWORD]
        self.dll.BASS_StreamPutData.restype = DWORD

        self.dll.BASS_StreamPutFileData.argtypes = [HSTREAM, PTR, DWORD]
        self.dll.BASS_StreamPutFileData.restype = DWORD

        # BASS / MOD/MO3 music
        self.dll.BASS_MusicFree.argtypes = [HMUSIC]
        self.dll.BASS_MusicFree.restype = BOOL

        self.dll.BASS_MusicLoad.argtypes = [BOOL, PTR, QWORD, DWORD, DWORD, DWORD]
        self.dll.BASS_MusicLoad.restype = HMUSIC

        # BASS / Recording
        self.dll.BASS_RecordFree.argtypes = []
        self.dll.BASS_RecordFree.restype = BOOL

        self.dll.BASS_RecordGetDevice.argtypes = []
        self.dll.BASS_RecordGetDevice.restype = DWORD

        self.dll.BASS_RecordGetDeviceInfo.argtypes = [DWORD, ctypes.POINTER(BASS_DEVICEINFO)]
        self.dll.BASS_RecordGetDeviceInfo.restype = BOOL

        self.dll.BASS_RecordGetInfo.argtypes = [ctypes.POINTER(BASS_RECORDINFO)]
        self.dll.BASS_RecordGetInfo.restype = BOOL

        self.dll.BASS_RecordGetInput.argtypes = [INT, ctypes.POINTER(FLOAT)]
        self.dll.BASS_RecordGetInput.restype = DWORD

        self.dll.BASS_RecordGetInputName.argtypes = [INT]
        self.dll.BASS_RecordGetInputName.restype = CHARP

        self.dll.BASS_RecordInit.argtypes = [INT]
        self.dll.BASS_RecordInit.restype = BOOL

        self.dll.BASS_RecordSetDevice.argtypes = [DWORD]
        self.dll.BASS_RecordSetDevice.restype = BOOL

        self.dll.BASS_RecordSetInput.argtypes = [INT, DWORD, FLOAT]
        self.dll.BASS_RecordSetInput.restype = BOOL

        self.dll.BASS_RecordStart.argtypes = [DWORD, DWORD, DWORD, ctypes.POINTER(RECORDPROC), PTR]
        self.dll.BASS_RecordStart.restype = HRECORD

        # BASS / Channels
        self.dll.BASS_ChannelBytes2Seconds.argtypes = [DWORD, QWORD]
        self.dll.BASS_ChannelBytes2Seconds.restype = DOUBLE

        self.dll.BASS_ChannelFlags.argtypes = [DWORD, DWORD, DWORD]
        self.dll.BASS_ChannelFlags.restype = DWORD

        self.dll.BASS_ChannelFree.argtypes = [DWORD]
        self.dll.BASS_ChannelFree.restype = BOOL

        self.dll.BASS_ChannelGet3DAttributes.argtypes = [DWORD, ctypes.POINTER(DWORD), ctypes.POINTER(DWORD), ctypes.POINTER(FLOAT), ctypes.POINTER(FLOAT), ctypes.POINTER(DWORD), ctypes.POINTER(DWORD), ctypes.POINTER(FLOAT)]
        self.dll.BASS_ChannelGet3DAttributes.restype = BOOL

        self.dll.BASS_ChannelGet3DPosition.argtypes = [DWORD, ctypes.POINTER(BASS_3DVECTOR), ctypes.POINTER(BASS_3DVECTOR), ctypes.POINTER(BASS_3DVECTOR)]
        self.dll.BASS_ChannelGet3DPosition.restype = BOOL

        self.dll.BASS_ChannelGetAttribute.argtypes = [DWORD, DWORD, ctypes.POINTER(FLOAT)]
        self.dll.BASS_ChannelGetAttribute.restype = DOUBLE

        self.dll.BASS_ChannelGetAttributeEx.argtypes = [DWORD, DWORD, PTR, DWORD]
        self.dll.BASS_ChannelGetAttributeEx.restype = DOUBLE

        self.dll.BASS_ChannelGetData.argtypes = [DWORD, PTR, DWORD]
        self.dll.BASS_ChannelGetData.restype = DWORD

        self.dll.BASS_ChannelGetDevice.argtypes = [DWORD]
        self.dll.BASS_ChannelGetDevice.restype = DWORD

        self.dll.BASS_ChannelGetInfo.argtypes = [DWORD, ctypes.POINTER(BASS_CHANNELINFO)]
        self.dll.BASS_ChannelGetInfo.restype = BOOL

        self.dll.BASS_ChannelGetLength.argtypes = [DWORD, DWORD]
        self.dll.BASS_ChannelGetLength.restype = QWORD

        self.dll.BASS_ChannelGetLevel.argtypes = [DWORD]
        self.dll.BASS_ChannelGetLevel.restype = DWORD

        self.dll.BASS_ChannelGetLevelEx.argtypes = [DWORD, ctypes.POINTER(FLOAT), FLOAT, DWORD]
        self.dll.BASS_ChannelGetLevelEx.restype = BOOL

        self.dll.BASS_ChannelGetPosition.argtypes = [DWORD, DWORD]
        self.dll.BASS_ChannelGetPosition.restype = QWORD

        self.dll.BASS_ChannelGetTags.argtypes = [DWORD, DWORD]
        self.dll.BASS_ChannelGetTags.restype = CHARP

        self.dll.BASS_ChannelIsActive.argtypes = [DWORD]
        self.dll.BASS_ChannelIsActive.restype = DWORD

        self.dll.BASS_ChannelIsSliding.argtypes = [DWORD, DWORD]
        self.dll.BASS_ChannelIsSliding.restype = BOOL

        self.dll.BASS_ChannelLock.argtypes = [DWORD, BOOL]
        self.dll.BASS_ChannelLock.restype = BOOL

        self.dll.BASS_ChannelPause.argtypes = [DWORD]
        self.dll.BASS_ChannelPause.restype = BOOL

        self.dll.BASS_ChannelPlay.argtypes = [DWORD, BOOL]
        self.dll.BASS_ChannelPlay.restype = BOOL

        self.dll.BASS_ChannelRemoveDSP.argtypes = [DWORD, HDSP]
        self.dll.BASS_ChannelRemoveDSP.restype = BOOL

        self.dll.BASS_ChannelRemoveFX.argtypes = [DWORD, HFX]
        self.dll.BASS_ChannelRemoveFX.restype = BOOL

        self.dll.BASS_ChannelRemoveLink.argtypes = [DWORD, DWORD]
        self.dll.BASS_ChannelRemoveLink.restype = BOOL

        self.dll.BASS_ChannelRemoveSync.argtypes = [DWORD, HSYNC]
        self.dll.BASS_ChannelRemoveSync.restype = BOOL

        self.dll.BASS_ChannelSeconds2Bytes.argtypes = [DWORD, DOUBLE]
        self.dll.BASS_ChannelSeconds2Bytes.restype = QWORD

        self.dll.BASS_ChannelSet3DAttributes.argtypes = [DWORD, INT, FLOAT, FLOAT, INT, INT, FLOAT]
        self.dll.BASS_ChannelSet3DAttributes.restype = BOOL

        self.dll.BASS_ChannelSet3DPosition.argtypes = [DWORD, ctypes.POINTER(BASS_3DVECTOR), ctypes.POINTER(BASS_3DVECTOR), ctypes.POINTER(BASS_3DVECTOR)]
        self.dll.BASS_ChannelSet3DPosition.restype = BOOL

        self.dll.BASS_ChannelSetAttribute.argtypes = [DWORD, DWORD, FLOAT]
        self.dll.BASS_ChannelSetAttribute.restype = BOOL

        self.dll.BASS_ChannelSetAttributeEx.argtypes = [DWORD, DWORD, PTR, DWORD]
        self.dll.BASS_ChannelSetAttributeEx.restype = BOOL

        self.dll.BASS_ChannelSetDevice.argtypes = [DWORD, DWORD]
        self.dll.BASS_ChannelSetDevice.restype = BOOL

        self.dll.BASS_ChannelSetDSP.argtypes = [DWORD, ctypes.POINTER(DSPPROC), PTR, INT]
        self.dll.BASS_ChannelSetDSP.restype = HDSP

        self.dll.BASS_ChannelSetFX.argtypes = [DWORD, DWORD, INT]
        self.dll.BASS_ChannelSetFX.restype = HFX

        self.dll.BASS_ChannelSetLink.argtypes = [DWORD, DWORD]
        self.dll.BASS_ChannelSetLink.restype = BOOL

        self.dll.BASS_ChannelSetPosition.argtypes = [DWORD, QWORD, DWORD]
        self.dll.BASS_ChannelSetPosition.restype = BOOL

        self.dll.BASS_ChannelSetSync.argtypes = [DWORD, DWORD, DWORD, ctypes.POINTER(SYNCPROC), PTR]
        self.dll.BASS_ChannelSetSync.restype = HSYNC

        self.dll.BASS_ChannelSlideAttribute.argtypes = [DWORD, DWORD, FLOAT, DWORD]
        self.dll.BASS_ChannelSlideAttribute.restype = BOOL

        self.dll.BASS_ChannelStart.argtypes = [DWORD]
        self.dll.BASS_ChannelStart.restype = BOOL

        self.dll.BASS_ChannelStop.argtypes = [DWORD]
        self.dll.BASS_ChannelStop.restype = BOOL

        self.dll.BASS_ChannelUpdate.argtypes = [DWORD, DWORD]
        self.dll.BASS_ChannelUpdate.restype = BOOL

        # BASS / Effects
        self.dll.BASS_FXGetParameters.argtypes = [HFX, PTR]
        self.dll.BASS_FXGetParameters.restype = BOOL

        self.dll.BASS_FXReset.argtypes = [DWORD]
        self.dll.BASS_FXReset.restype = BOOL

        self.dll.BASS_FXSetParameters.argtypes = [HFX, PTR]
        self.dll.BASS_FXSetParameters.restype = BOOL

        self.dll.BASS_FXSetPriority.argtypes = [HFX, INT]
        self.dll.BASS_FXSetPriority.restype = BOOL

    def _raise_error(self, name):
        """ Raises a BASSError if fucntion returns "failed" value """
        raise BASSError(self.ErrorGetCode(), name)

    def __delattr__(self):
        try: self.Free()
        except BASSError as err:
            if err.code != 8: raise err # BASS_Init never called (err 8), so whatever

    #region BASS / Config
    def GetConfig(self, option: DWORD) -> DWORD:
        """ Retrieves the current value of a configuration option.\n
        https://www.un4seen.com/doc/#bass/BASS_GetConfig.html"""
        result = self.dll.BASS_GetConfig(option)
        if self.safe and result == MINUSONE: self._raise_error('BASS_GetConfig')
        return result
    
    def GetConfigPtr(self, option: DWORD) -> PTR:
        """ Retrieves the current value of a configuration option.\n
        https://www.un4seen.com/doc/#bass/BASS_GetConfigPtr.html"""
        result = self.dll.BASS_GetConfigPtr(option)
        if self.safe and result == None: self._raise_error('BASS_GetConfigPtr')
        return result
    
    def SetConfig(self, option: DWORD, value: DWORD) -> BOOL:
        """ Sets the value of a config option.\n
        https://www.un4seen.com/doc/#bass/BASS_SetConfig.html"""
        result = self.dll.BASS_SetConfig(option, value)
        if self.safe and result == 0: self._raise_error('BASS_SetConfig')
        return result

    def SetConfigPtr(self, option: DWORD, value: PTR) -> BOOL:
        """ Sets the value of a config option.\n
        https://www.un4seen.com/doc/#bass/BASS_SetConfigPtr.html"""
        result = self.dll.BASS_SetConfigPtr(option, value)
        if self.safe and result == 0: self._raise_error('BASS_SetConfigPtr')
        return result
    #endregion

    #region BASS / Plugins
    def PluginEnable(self, handle:HPLUGIN, enable:BOOL) -> BOOL:
        """ Enables or disables an add-on\n
        https://www.un4seen.com/doc/#bass/BASS_PluginEnable.html"""
        result = self.dll.BASS_PluginEnable(handle, enable)
        if self.safe and result == 0: self._raise_error('BASS_PluginEnable')
        return result

    def PluginFree(self, handle:HPLUGIN) -> BOOL:
        """ Unplugs an add-on.\n
        https://www.un4seen.com/doc/#bass/BASS_PluginFree.html"""
        result = self.dll.BASS_PluginFree(handle)
        if self.safe and result == 0: self._raise_error('BASS_PluginFree')
        return result

    def PluginGetInfo(self, handle:HPLUGIN) -> BASS_PLUGININFO:
        """ Retrieves information about an add-on.\n
        https://www.un4seen.com/doc/#bass/BASS_PluginGetInfo.html"""
        result = self.dll.BASS_PluginGetInfo(handle)
        if self.safe and result == None: self._raise_error('BASS_PluginGetInfo')
        return result
    
    def PluginLoad(self, file:CHARP, flags:DWORD) -> HPLUGIN:
        """ Plugs an "add-on" into the standard stream and sample creation functions.\n
        https://www.un4seen.com/doc/#bass/BASS_PluginLoad.html"""
        result = self.dll.BASS_PluginLoad(file, flags)
        if self.safe and result == 0: self._raise_error('BASS_PluginLoad')
        return result
    #endregion

    #region BASS / Initialization, info, etc...
    def ErrorGetCode(self) -> INT:
        """ Retrieves the error code for the most recent BASS function call in the current thread.\n
        https://www.un4seen.com/doc/#bass/BASS_ErrorGetCode.html."""
        return self.dll.BASS_ErrorGetCode()

    def Free(self) -> BOOL:
        """ Frees all resources used by the output device, including all its samples, streams and MOD musics\n
        https://www.un4seen.com/doc/#bass/BASS_Free.html"""
        result = self.dll.BASS_Free()
        if self.safe and result == 0: self._raise_error('BASS_Free')
        return result

    def GetCPU(self) -> FLOAT:
        """ Retrieves the current CPU usage of BASS.\n
        https://www.un4seen.com/doc/#bass/BASS_GetCPU.html"""
        result = self.dll.BASS_GetCPU()
        return result

    def GetDevice(self) -> DWORD:
        """ Retrieves the current output device.\n
        https://www.un4seen.com/doc/#bass/BASS_GetDevice.html"""
        result = self.dll.BASS_GetDevice()
        if self.safe and result == MINUSONE: self._raise_error('BASS_GetDevice')
        return result

    def GetDeviceInfo(self, device:DWORD, info: BASS_DEVICEINFO|None) -> BOOL:
        """ Retrieves information on an output device.\n
        https://www.un4seen.com/doc/#bass/BASS_GetDeviceInfo.html"""
        result = self.dll.BASS_GetDeviceInfo(device, ctypes.byref(info))
        if self.safe and result == 0: self._raise_error('BASS_GetDeviceInfo')
        return result

    def GetInfo(self, info:BASS_INFO|None) -> BOOL:
        """ Retrieves information on the device being used.\n
        https://www.un4seen.com/doc/#bass/BASS_GetInfo.html"""
        result = self.dll.BASS_GetInfo(ctypes.byref(info))
        if self.safe and result == 0: self._raise_error('BASS_GetInfo')
        return result

    def GetVersion(self) -> DWORD:
        """ Retrieves the version of BASS that is loaded.\n
        https://www.un4seen.com/doc/#bass/BASS_GetVersion.html"""
        result = self.dll.BASS_GetVersion()
        return result

    def GetVolume(self) -> FLOAT:
        """ Retrieves the current master volume level.\n
        https://www.un4seen.com/doc/#bass/BASS_GetVolume.html"""
        result = self.dll.BASS_GetVolume()
        if self.safe and result == MINUSONE: self._raise_error('BASS_GetVolume')
        return result

    def Init(self, device:INT, freq:DWORD, flags:DWORD, win:INT, clsid:PTR|None=None) -> BOOL:
        """ Initializes an output device.\n
        https://www.un4seen.com/doc/#bass/BASS_Init.html"""
        result = self.dll.BASS_Init(device, freq, flags, win, clsid)
        if self.safe and result == 0: self._raise_error('BASS_Init')
        return result

    def IsStarted(self) -> DWORD:
        """ Checks if the output has been started and is active.\n
        https://www.un4seen.com/doc/#bass/BASS_IsStarted.html"""
        result = self.dll.BASS_IsStarted()
        return result

    def Pause(self) -> BOOL:
        """ Stops the output, pausing all musics/samples/streams on it.\n
        https://www.un4seen.com/doc/#bass/BASS_Pause.html"""
        result = self.dll.BASS_Pause()
        if self.safe and result == FALSE: self._raise_error('BASS_Pause')
        return result

    def SetDevice(self, device:DWORD) -> BOOL:
        """ Sets the device to use for subsequent calls in the current thread.
        https://www.un4seen.com/doc/#bass/BASS_SetDevice.html"""
        result = self.dll.BASS_SetDevice(device)
        if self.safe and result == FALSE: self._raise_error('BASS_SetDevice')
        return result

    def SetVolume(self, volume:FLOAT) -> BOOL:
        """ Sets the output master volume.\n
        https://www.un4seen.com/doc/#bass/BASS_SetVolume.html"""
        result = self.dll.BASS_SetVolume(volume)
        if self.safe and result == 0: self._raise_error('BASS_SetVolume')
        return result

    def Start(self) -> BOOL:
        """ Starts/resumes the output.\n
        https://www.un4seen.com/doc/#bass/BASS_Start.html"""
        result = self.dll.BASS_Start()
        if self.safe and result == 0: self._raise_error('BASS_Start')
        return result

    def Stop(self) -> BOOL:
        """ Stops the output, pausing all musics/samples/streams on it.\n
        https://www.un4seen.com/doc/#bass/BASS_Stop.html"""
        result = self.dll.BASS_Stop()
        if self.safe and result == 0: self._raise_error('BASS_Stop')
        return result

    def Update(self, length:DWORD) -> BOOL:
        """ Updates the `HSTREAM` and `HMUSIC` channel playback buffers.
        https://www.un4seen.com/doc/#bass/BASS_Update.html"""
        result = self.dll.BASS_Update(length)
        if self.safe and result == 0: self._raise_error('BASS_Update')
        return
    #endregion

    #region BASS / 3D
    def Apply3D(self) -> None:
        """ Applies changes made to the 3D system.\n
        https://www.un4seen.com/doc/#bass/BASS_Apply3D.html
        """
        self.dll.BASS_Apply3D()

    def Get3DFactors(self, distf:FLOAT|None=None, rollf:FLOAT|None=None, doppf:FLOAT|None=None) -> BOOL:
        """ Retrieves the factors that affect the calculations of 3D sound.\n
        https://www.un4seen.com/doc/#bass/BASS_Get3DFactors.html"""
        result = self.dll.BASS_Get3DFactors(ctypes.byref(distf), ctypes.byref(rollf), ctypes.byref(doppf))
        if self.safe and result == 0: self._raise_error('BASS_Get3DFactors')
        return result
    
    def Get3DPosition(self, pos:BASS_3DVECTOR|None=None, vel:BASS_3DVECTOR|None=None, front:BASS_3DVECTOR|None=None, top:BASS_3DVECTOR|None=None) -> BOOL:
        """ Retrieves the position, velocity, and orientation of the listener.\n
        https://www.un4seen.com/doc/#bass/BASS_Get3DPosition.html"""
        result = self.dll.BASS_Get3DPosition(ctypes.byref(pos), ctypes.byref(vel), ctypes.byref(front), ctypes.byref(top))
        if self.safe and result == 0: self._raise_error('BASS_Get3DPosition')
        return result
    
    def Set3DFactors(self, distf:FLOAT, rollf:FLOAT, doppf:FLOAT) -> BOOL:
        """ Sets the factors that affect the calculations of 3D sound.\n
        https://www.un4seen.com/doc/#bass/BASS_Set3DFactors.html"""
        result = self.dll.BASS_Set3DFactors(distf, rollf, doppf)
        if self.safe and result == 0: self._raise_error('BASS_Set3DFactors')
        return result

    def Set3DPosition(self, pos:BASS_3DVECTOR|None=None, vel:BASS_3DVECTOR|None=None, front:BASS_3DVECTOR|None=None, top:BASS_3DVECTOR|None=None) -> BOOL:
        """Sets the position, velocity, and orientation of the listener (ie. the player).\n
        https://www.un4seen.com/doc/#bass/BASS_Set3DPosition.html"""
        result = self.dll.BASS_Set3DPosition(ctypes.byref(pos), ctypes.byref(vel), ctypes.byref(front), ctypes.byref(top))
        if self.safe and result == 0: self._raise_error('BASS_Set3DPosition')
        return result
    #endregion

    #region BASS / Samples
    def SampleCreate(self, length:DWORD, freq:DWORD, chans:DWORD, max:DWORD, flags:DWORD) -> HSAMPLE:
        """Creates a new sample.\n
        https://www.un4seen.com/doc/#bass/BASS_SampleCreate.html"""
        result = self.dll.BASS_SampleCreate(length, freq, chans, max, flags)
        if self.safe and result == 0: self._raise_error('BASS_SampleCreate')
        return result
    
    def SampleFree(self, handle:HSAMPLE) -> BOOL:
        """Frees a sample's resources.\n
        https://www.un4seen.com/doc/#bass/BASS_SampleFree.html"""
        result = self.dll.BASS_SampleFree(handle)
        if self.safe and result == 0: self._raise_error('BASS_SampleFree')
        return result
    
    def SampleGetChannel(self, handle:HSAMPLE, flags:DWORD) -> HCHANNEL:
        """Creates a new channel from a sample.\n
        https://www.un4seen.com/doc/#bass/BASS_SampleGetChannel.html"""
        result = self.dll.BASS_SampleGetChannel(handle, flags)
        if self.safe and result == None: self._raise_error('BASS_SampleGetChannel')
        return result
    
    def SampleGetChannels(self, handle:HSAMPLE, channels:HCHANNEL|None) -> DWORD:
        """Retrieves all a sample's existing channels.\n
        https://www.un4seen.com/doc/#bass/BASS_SampleGetChannels.html"""
        result = self.dll.BASS_SampleGetChannels(handle, ctypes.byref(channels))
        if self.safe and result == MINUSONE: self._raise_error('BASS_SampleGetChannels')
        return result
    
    def SampleGetData(self, handle:HSAMPLE, buffer:PTR|None) -> BOOL:
        """Retrieves a copy of a sample's data.\n
        https://www.un4seen.com/doc/#bass/BASS_SampleGetData.html"""
        result = self.dll.BASS_SampleGetData(handle, ctypes.byref(buffer))
        if self.safe and result == 0: self._raise_error('BASS_SampleGetData')
        return result
    
    def SampleGetInfo(self, handle:HSAMPLE, info:BASS_SAMPLE|None) -> BOOL:
        """ Retrieves a sample's default attributes and other information.\n
        https://www.un4seen.com/doc/#bass/BASS_SampleGetInfo.html"""
        result = self.dll.BASS_SampleGetInfo(handle, ctypes.byref(info))
        if self.safe and result == 0: self._raise_error('BASS_SampleGetInfo')
        return result
    
    def SampleLoad(self, mem:BOOL, file:PTR|None, offset:QWORD, length:DWORD, max:DWORD, flags:DWORD) -> HSAMPLE:
        """Loads a WAV, AIFF, MP3, MP2, MP1, OGG or plugin supported sample.\n
        https://www.un4seen.com/doc/#bass/BASS_SampleLoad.html"""
        result = self.dll.BASS_SampleLoad(mem, ctypes.byref(file), offset, length, max, flags)
        if self.safe and result == 0: self._raise_error('BASS_SampleLoad')
        return result
    
    def SampleSetData(self, handle:HSAMPLE, buffer:PTR|None) -> BOOL:
        """ Sets a sample's data.\n
        https://www.un4seen.com/doc/#bass/BASS_SampleSetData.html"""
        result = self.dll.BASS_SampleSetData(handle, ctypes.byref(buffer))
        if self.safe and result == 0: self._raise_error('BASS_SampleSetData')
        return result

    def SampleSetInfo(self, handle:HSAMPLE, info:BASS_SAMPLE|None) -> BOOL:
        """Sets a sample's default attributes.\n
        https://www.un4seen.com/doc/#bass/BASS_SampleSetInfo.html"""
        result = self.dll.BASS_SampleSetInfo(handle, ctypes.byref(info))
        if self.safe and result == 0: self._raise_error('BASS_SampleSetInfo')
        return result

    def SampleStop(self, handle:HSAMPLE) -> BOOL:
        """Stops and frees all of a sample's channels (HCHANNEL).\n
        https://www.un4seen.com/doc/#bass/BASS_SampleStop.html"""
        result = self.dll.BASS_SampleStop(handle)
        if self.safe and result == 0: self._raise_error('BASS_SampleStop')
        return result
    #endregion

    #region BASS / Streams
    def StreamCreate(self, freq:DWORD, chans:DWORD, flags:DWORD, proc:StreamProcType|None, user:PTR|None) -> HSTREAM:
        """Creates a user sample stream.\n
        https://www.un4seen.com/doc/#bass/BASS_StreamCreate.html"""
        c_proc = STREAMPROC(proc)
        result = self.dll.BASS_StreamCreate(freq, chans, flags, c_proc, user)
        if self.safe and result == 0: self._raise_error('BASS_StreamCreate')
        return result
    
    def StreamCreateFile(self, mem:BOOL, file:str, offset:QWORD, length:QWORD, flags:DWORD) -> HSTREAM:
        """Creates a sample stream from an MP3, MP2, MP1, OGG, WAV, AIFF or plugin supported file.\n
        https://www.un4seen.com/doc/#bass/BASS_StreamCreateFile.html"""
        result = self.dll.BASS_StreamCreateFile(mem, file, offset, length, flags)#FIXME locator to buffer
        if self.safe and result == 0: self._raise_error('BASS_StreamCreateFile')
        return result
    
    def StreamCreateFileUser(self, system:DWORD, flags:DWORD, proc:BASS_FILEPROCS|None, user:PTR|None) -> HSTREAM:
        """Creates a user sample stream from a file.\n
        https://www.un4seen.com/doc/#bass/BASS_StreamCreateFileUser.html"""
        result = self.dll.BASS_StreamCreateFileUser(system, flags, ctypes.byref(proc), user)
        if self.safe and result == 0: self._raise_error
        return result
    
    def StreamCreateURL(self, url:PTR, offset:QWORD, flags:DWORD, proc:DownloadProcType|None, user:PTR|None) -> HSTREAM:
        """Creates a sample stream from an MP3, MP2, MP1, OGG, WAV, AIFF or plugin supported file on the internet, optionally receiving the downloaded data in a callback function.\n
        https://www.un4seen.com/doc/#bass/BASS_StreamCreateURL.html"""
        #c_proc = DOWNLOADPROC(proc) if proc != None else None
        result = self.dll.BASS_StreamCreateURL(url, offset, flags, proc, user)
        if self.safe and result == 0: self._raise_error('BASS_StreamCreateURL')
        return result
    
    def StreamFree(self, handle:HSTREAM):
        """Frees a sample stream's resources, including any sync/DSP/FX it has.\n
        https://www.un4seen.com/doc/#bass/BASS_StreamFree.html"""
        result = self.dll.BASS_StreamFree(handle)
        if self.safe and result == 0: self._raise_error('BASS_StreamFree')

    def StreamGetFilePosition(self, handle:HSTREAM, mode:DWORD) -> QWORD:
        """Retrieves the file position/status of a stream.\n
        https://www.un4seen.com/doc/#bass/BASS_StreamGetFilePosition.html"""
        result = self.dll.BASS_StreamGetFilePosition(handle, mode)
        if self.safe and result == MINUSONE: self._raise_error('BASS_StreamGetFilePosition')
        return result

    def StreamPutData(self, handle:HSTREAM, data:PTR|None, length:DWORD) -> DWORD:
        """Adds sample data to a "push" stream.\n
        https://www.un4seen.com/doc/#bass/BASS_StreamPutData.html"""
        result = self.dll.BASS_StreamPutData(handle, ctypes.byref(data), length)
        if self.safe and result == 0: self._raise_error('BASS_StreamPutData')
        return result

    def StreamPutFileData(self, handle:HSTREAM, data:PTR|None, length:DWORD) -> DWORD:
        """Adds data to a "push buffered" user file stream's buffer.\n
        https://www.un4seen.com/doc/#bass/BASS_StreamPutFileData.html"""
        result = self.dll.BASS_StreamPutFileData(handle, ctypes.byref(data), length)
        if self.safe and result == 0: self._raise_error('BASS_StreamPutFileData')
        return result
    #endregion

    #region BASS / MOD/MO3 music
    def MusicFree(self, handle:HMUSIC) -> BOOL:
        """Frees a MOD music's resources, including any sync/DSP/FX it has.\n
        https://www.un4seen.com/doc/#bass/BASS_MusicFree.html"""
        result = self.dll.BASS_MusicFree(handle)
        if self.safe and result == 0: self._raise_error('BASS_MusicFree')
        return result

    def MusicLoad(self, mem:BOOL, file:PTR|None, offset:QWORD, length:DWORD, flags:DWORD, freq:DWORD) -> HMUSIC:
        """Loads a MOD music file.\n
        https://www.un4seen.com/doc/#bass/BASS_MusicLoad.html"""
        result = self.dll.BASS_MisicLoad(mem, ctypes.byref(file), offset, length, flags, freq)
        if self.safe and result == 0: self._raise_error('BASS_ChannelPlay')
        return result
    #endregion

    #region BASS / Recording
    def RecordFree(self) -> BOOL:
        """Frees all resources used by the recording device.\n
        https://www.un4seen.com/doc/#bass/BASS_RecordFree.html"""
        result = self.dll.BASS_RecordFree()
        if self.safe and result == 0: self._raise_error('BASS_RecordFree')
        return result
    
    def RecordGetDevice(self) -> DWORD:
        """ Retrieves the recording device setting of the current thread.\n
        https://www.un4seen.com/doc/#bass/BASS_RecordGetDevice.html"""
        result = self.dll.BASS_RecordGetDevice()
        if self.safe and result == MINUSONE: self._raise_error('BASS_RecordGeetDevice')
        return result
    
    def RecordGetDeviceInfo(self, device:DWORD, info:BASS_DEVICEINFO|None) -> BOOL:
        """Retrieves information on a recording device.\n
        https://www.un4seen.com/doc/#bass/BASS_RecordGetDeviceInfo.html"""
        result = self.dll.BASS_RecordGetDeviceInfo(device, ctypes.byref(info))
        if self.safe and result == 0: self._raise_error('BASS_RecordGetDeviceInfo')
        return result
    
    def RecordGetInfo(self, info:BASS_RECORDINFO|None) -> BOOL:
        """Retrieves information on the recording device being used.\n
        https://www.un4seen.com/doc/#bass/BASS_RecordGetInfo.html"""
        result = self.dll.BASS_RecordGetInfo(ctypes.byref(info))
        if self.safe and result == 0: self._raise_error('BASS_RecordGetInfo')
        return result

    def RecordGetInput(self, input:INT, volume:FLOAT|None) -> DWORD:
        """Retrieves the current settings of a recording input source.\n
        https://www.un4seen.com/doc/#bass/BASS_RecordGetInput.html"""
        result = self.dll.BASS_RecordGetInput(input, ctypes.byref(volume))
        if self.safe and result == 0: self._raise_error('BASS_RecordGetInput')
        return result
    
    def RecordGetInputName(self, input:INT) -> str:
        """Retrieves the text description of a recording input source.\n
        https://www.un4seen.com/doc/#bass/BASS_RecordGetInputName.html"""
        result = self.dll.BASS_RecordGetInputName(input)
        if self.safe and result == None: self._raise_error('BASS_RecordGetInputName')
        return result
    
    def RecordInit(self, device:INT) -> BOOL:
        """Initializes a recording device.\n
        https://www.un4seen.com/doc/#bass/BASS_RecordInit.html"""
        result = self.dll.BASS_RecordInit(device)
        if self.safe and result == 0: self._raise_error('BASS_RecordInit')
        return result

    def RecordSetDevice(self, device:DWORD) -> BOOL:
        """Sets the recording device to use for subsequent calls in the current thread.\n
        https://www.un4seen.com/doc/#bass/BASS_RecordSetDevice.html"""
        result = self.dll.BASS_RecordSetDevice(device)
        if self.safe and result == 0: self._raise_error('BASS_RecordSetDevice')
        return result

    def RecordSetInput(self, input:INT, flags:DWORD, volume:FLOAT) -> BOOL:
        """Adjusts the settings of a recording input source.\n
        https://www.un4seen.com/doc/#bass/BASS_RecordSetInput.html"""
        result = self.dll.BASS_RecordSetInput(input, flags, volume)
        if self.safe and result == 0: self._raise_error('BASS_RecordSetInput')
        return result
  
    def RecordStart(self, freq:DWORD, chans:DWORD, flags:DWORD, proc:RecordProcType|None, user:PTR|None) -> HRECORD:
        """Starts recording.\n
        https://www.un4seen.com/doc/#bass/BASS_RecordStart.html"""
        c_proc = RECORDPROC(proc)
        result = self.dll.BASS_RecordStart(freq, chans, flags, c_proc, user)
        if self.safe and result == 0: self._raise_error('BASS_RecordStart')
        return result
    #endregion

    #region BASS / Channels
    def ChannelBytes2Seconds(self, handle:HANDLE, pos:QWORD) -> DOUBLE:
        """ Translates a byte position into time (seconds), based on a channel's format.\n
        https://www.un4seen.com/doc/#bass/BASS_ChannelBytes2Seconds.html"""
        result = self.dll.BASS_ChannelBytes2Seconds(handle, pos)
        if self.safe and result == MINUSONE: self._raise_error('BASS_ChannelBytes2Seconds')
        return result
        
    def ChannelFlags(self, handle:HANDLE, flags:DWORD, mask:DWORD) -> DWORD:
        """Modifies and retrieves a channel's flags.\n
        https://www.un4seen.com/doc/#bass/BASS_ChannelFlags.html"""
        result = self.dll.BASS_ChannelFlags(handle, flags, mask)
        if self.safe and result == 0: self._raise_error('BASS_ChannelFlags')
        return result

    def ChannelFree(self, handle:HANDLE) -> BOOL:
        """Frees a channel, including any sync/DSP/FX it has.\n
        https://www.un4seen.com/doc/#bass/BASS_ChannelFree.html"""
        result = self.dll.BASS_ChannelFree(handle)
        if self.safe and result == 0: self._raise_error('BASS_ChannelFree')
        return result

    def ChannelGet3DAttributes(self, handle:HANDLE, mode:DWORD|None, min:FLOAT|None, max:FLOAT|None, iangle:DWORD|None, oangle:DWORD|None, outvol:FLOAT|None) -> BOOL:
        """Retrieves the 3D attributes of a sample, stream, or MOD music channel with 3D functionality.\n
        https://www.un4seen.com/doc/#bass/BASS_ChannelGet3DAttributes.html"""
        result = self.dll.BASS_ChannelGet3DAttributes(handle, ctypes.byref(mode), ctypes.byref(min), ctypes.byref(max), ctypes.byref(iangle), ctypes.byref(oangle), ctypes.byref(outvol))
        if self.safe and result == 0: self._raise_error('BASS_ChannelGet3DAttributes')
        return result

    def ChannelGet3DPosition(self, handle:HANDLE, pos:BASS_3DVECTOR|None, orient:BASS_3DVECTOR|None, vol:BASS_3DVECTOR|None) -> BOOL:
        """Retrieves the 3D position of a sample, stream, or MOD music channel with 3D functionality.\n
        https://www.un4seen.com/doc/#bass/BASS_ChannelGet3DPosition.html"""
        result = self.dll.BASS_ChannelGet3DPosition(handle, ctypes.byref(pos), ctypes.byref(orient), ctypes.byref(vol))
        if self.safe and result == 0: self._raise_error('BASS_ChannelGet3DPosition')
        return result

    def ChannelGetAttribute(self, handle:HANDLE, attrib:DWORD, value:FLOAT) -> BOOL:
        """Retrieves the value of a channel's attribute.\n
        https://www.un4seen.com/doc/#bass/BASS_ChannelGetAttribute.html"""
        result = self.dll.BASS_ChannelGetAttribute(handle, attrib, ctypes.byref(value))
        if self.safe and result == 0: self._raise_error('BASS_ChannelGetAttribute')
        return result

    def ChannelGetAttributeEx(self, handle:HANDLE, attrib:DWORD, value:PTR|None, size:DWORD) -> DWORD:
        """Retrieves the value of a channel's attribute.\n
        https://www.un4seen.com/doc/#bass/BASS_ChannelGetAttributeEx.html"""
        result = self.dll.BASS_ChannelGetAttributeEx(handle, attrib, ctypes.byref(value), size)
        if self.safe and result == 0: self._raise_error('BASS_ChannelGetAttributeEx')
        return result
    
    def ChannelGetData(self, handle:HANDLE, buffer:PTR|None, lenght:DWORD) -> DWORD:
        """Retrieves the immediate sample data (or an FFT representation of it) of a sample channel, stream, MOD music, or recording channel.\n
        https://www.un4seen.com/doc/#bass/BASS_ChannelGetData.html"""
        result = self.dll.BASS_ChannelGetData(handle, ctypes.byref(buffer), lenght)
        if self.safe and result == MINUSONE: self._raise_error('BASS_ChannelGetData')
        return result
    
    def ChannelGetDevice(self, handle:HANDLE) -> DWORD:
        """Retrieves the device that a channel is using.
        https://www.un4seen.com/doc/#bass/BASS_ChannelGetDevice.html"""
        result = self.dll.BASS_ChannelGetDevice(handle)
        if self.safe and result == MINUSONE: self._raise_error('BASS_ChannelGetDevice')
        return result
    
    def ChannelGetInfo(self, handle:HANDLE, info:BASS_CHANNELINFO|None) -> BOOL:
        """Retrieves information on a channel.
        https://www.un4seen.com/doc/#bass/BASS_ChannelGetInfo.html"""
        result = self.dll.BASS_ChannelGetInfo(handle, ctypes.byref(info))
        if self.safe and result == 0: self._raise_error('BASS_ChannelGetInfo')
        return result
    
    def ChannelGetLength(self, handle:HANDLE, mode:DWORD) -> QWORD:
        """Retrieves the length of a channel.\n
        https://www.un4seen.com/doc/#bass/BASS_ChannelGetLength.html"""
        result = self.dll.BASS_ChannelGetLength(handle, mode)
        if self.safe and result == MINUSONE: self._raise_error('BASS_ChannelGetLength')
        return result
        
    def ChannelGetLevel(self, handle:HANDLE) -> DWORD:
        """ Retrieves the level (peak amplitude) of a sample, stream, MOD music, or recording channel.
        https://www.un4seen.com/doc/#bass/BASS_ChannelGetLevel.html"""
        result = self.dll.BASS_ChannelGetLevel(handle)
        if self.safe and result == MINUSONE: self._raise_error('BASS_ChannelGetLevel')
        return result

    def ChannelGetLevelEx(self, handle:HANDLE, levels:FLOAT|None, lenght:FLOAT, flags:DWORD) -> BOOL:
        """ Retrieves the level of a sample, stream, MOD music, or recording channel.
        https://www.un4seen.com/doc/#bass/BASS_ChannelGetLevelEx.html"""
        result = self.dll.BASS_ChannelGetLevelEx(handle, ctypes.byref(levels), lenght, flags)
        if self.safe and result == 0: self._raise_error('BASS_ChannelGetLevelEx')
        return result

    def ChannelGetPosition(self, handle:HANDLE, mode:DWORD) -> QWORD:
        """Retrieves the current position of a channel.\n
        https://www.un4seen.com/doc/#bass/BASS_ChannelGetPosition.html"""
        result = self.dll.BASS_ChannelGetPosition(handle, mode)
        if self.safe and result == MINUSONE: self._raise_error('BASS_ChannelGetPosition')
        return result

    def ChannelGetTags(self, handle:HANDLE, flags:DWORD) -> str:
        """Retrieves tags/headers from a channel.\n
        https://www.un4seen.com/doc/#bass/BASS_ChannelGetTags.html"""
        result = self.dll.BASS_ChannelGetTags(handle, flags)
        if self.safe and result == None: self._raise_error('BASS_ChannelGetTags')
        return result

    def ChannelIsActive(self, handle:HANDLE) -> DWORD:
        """ Checks if a sample, stream, or MOD music is active (playing) or stalled. Can also check if a recording is in progress.\n
        https://www.un4seen.com/doc/#bass/BASS_ChannelIsActive.html"""
        result = self.dll.BASS_ChannelIsActive(handle)
        return result

    def ChannelIsSliding(self, handle:HANDLE, attrib:DWORD) -> BOOL:
        """ Checks if an attribute (or any attribute) of a sample, stream, or MOD music is sliding.\n
        https://www.un4seen.com/doc/#bass/BASS_ChannelIsSliding.html"""
        result = self.dll.BASS_ChannelIsActive(handle, attrib)
        return result

    def ChannelLock(self, handle:HANDLE, lock:BOOL) -> BOOL:
        """ Locks a stream, MOD music or recording channel to the current thread.\n
        https://www.un4seen.com/doc/#bass/BASS_ChannelLock.html"""
        result = self.dll.BASS_ChannelLock(handle, lock)
        if self.safe and result == 0: self._raise_error('BASS_ChannelLock')
        return result

    def ChannelPause(self, handle:HANDLE) -> BOOL:
        """Pauses a sample, stream, MOD music, or recording.\n
        https://www.un4seen.com/doc/#bass/BASS_ChannelPause.html"""
        result = self.dll.BASS_ChannelPause(handle)
        if self.safe and result == 0: self._raise_error('BASS_ChannelPause')
        return result

    def ChannelPlay(self, handle:HANDLE, restart:BOOL) -> BOOL:
        """Starts/resumes playback of a sample, stream, MOD music, or a recording.\n
        https://www.un4seen.com/doc/#bass/BASS_ChannelPlay.html"""
        result = self.dll.BASS_ChannelPlay(handle, restart)
        if self.safe and result == 0: self._raise_error('BASS_ChannelPlay')
        return result

    def ChannelRemoveDSP(self, handle:HANDLE, dsp:HDSP) -> BOOL:
        """Removes a DSP function from a stream, MOD music, or recording channel.\n
        https://www.un4seen.com/doc/#bass/BASS_ChannelRemoveDSP.html"""
        result = self.dll.BASS_ChannelRemoveDSP(handle, dsp)
        if self.safe and result == 0: self._raise_error('BASS_ChannelRemoveDSP')
        return result
        
    def ChannelRemoveFX(self, handle:HANDLE, fx:HFX) -> BOOL:
        """Removes an effect on a stream, MOD music, or recording channel.\n
        https://www.un4seen.com/doc/#bass/BASS_ChannelRemoveFX.html"""
        result = self.dll.BASS_ChannelRemoveFX(handle, fx)
        if self.safe and result == 0: self._raise_error('BASS_ChannelRemoveFX')
        return result

    def ChannelRemoveLink(self, handle:HANDLE, chan:HCHANNEL) -> BOOL:
        """Removes a links between two MOD music or stream channels.\n
        https://www.un4seen.com/doc/#bass/BASS_ChannelRemoveLink.html"""
        result = self.dll.BASS_ChannelRemoveLink(handle, chan)
        if self.safe and result == 0: self._raise_error('BASS_ChannelRemoveLink')
        return result

    def ChannelRemoveSync(self, handle:HANDLE, sync:HSYNC) -> BOOL:
        """Removes a synchronizer from a MOD music, stream or recording channel.\n
        https://www.un4seen.com/doc/#bass/BASS_ChannelRemoveSync.html"""
        result = self.dll.BASS_ChannelRemoveSync(handle, sync)
        if self.safe and result == 0: self._raise_error('BASS_ChannelRemoveSync')
        return result

    def ChannelSeconds2Bytes(self, handle:HANDLE, seconds:float) -> QWORD:
        """Translates a time (seconds) position into bytes, based on a channel's format.\n
        https://www.un4seen.com/doc/#bass/BASS_ChannelSeconds2Bytes.html"""
        result = self.dll.BASS_ChannelSeconds2Bytes(handle, seconds)
        if self.safe and result == MINUSONE: self._raise_error('BASS_ChannelSeconds2Bytes')
        return result
    
    def ChannelSet3DAttributes(self, handle:HANDLE, mode:INT, min:FLOAT, max:FLOAT, iangle:INT, oangle:INT, outvol:FLOAT) -> BOOL:
        """Sets the 3D attributes of a sample, stream, or MOD music channel with 3D functionality.\n
        https://www.un4seen.com/doc/#bass/BASS_ChannelSet3DAttributes.html"""
        result = self.dll.BASS_ChannelSet3DAttributes(handle, mode, min, max, iangle, oangle, outvol)
        if self.safe and result == 0: self._raise_error('BASS_ChannelSet3DAttributes')
        return result

    def ChannelSet3DPosition(self, handle:HANDLE, pos:BASS_3DVECTOR|None, orient:BASS_3DVECTOR|None, vel:BASS_3DVECTOR|None) -> BOOL:
        """Sets the 3D position of a sample, stream, or MOD music channel with 3D functionality.\n
        https://www.un4seen.com/doc/#bass/BASS_ChannelSet3DPosition.html"""
        result = self.dll.BASS_ChannelSet3DPosition(handle, ctypes.byref(pos), ctypes.byref(orient), ctypes.byref(vel))
        if self.safe and result == 0: self._raise_error('BASS_ChannelSet3DPosition')
        return result

    def ChannelSetAttribute(self, handle:HANDLE, attr:INT, value:FLOAT) -> BOOL:
        """Sets the value of a channel's attribute.\n
        https://www.un4seen.com/doc/#bass/BASS_ChannelSetAttribute.html"""
        result = self.dll.BASS_ChannelSetAttribute(handle, attr, value)
        if self.safe and result == 0: self._raise_error('BASS_ChannelSetAttribute')
        return result

    def ChannelSetAttributeEx(self, handle:HANDLE, attr:INT, value:FLOAT|None, options:INT) -> BOOL:
        """Sets the value of a channel's attribute.\n
        https://www.un4seen.com/doc/#bass/BASS_ChannelSetAttributeEx.html"""
        result = self.dll.BASS_ChannelSetAttribute(handle, attr, ctypes.byref(value), options)
        if self.safe and result == 0: self._raise_error('BASS_ChannelSetAttribute')
        return result

    def ChannelSetDevice(self, handle:HANDLE, device:DWORD) -> BOOL:
        """Changes the device that a stream, MOD music or sample is using.\n
        https://www.un4seen.com/doc/#bass/BASS_ChannelSetDevice.html"""
        result = self.dll.BASS_ChannelSetDevice(handle, device)
        if self.safe and result == 0: self._raise_error('BASS_ChannelSetDevice')
        return result
    
    def ChannelSetDSP(self, handle:HANDLE, proc:DSPProcType|None, user:PTR|None, priority:INT) -> BOOL:
        """Sets up a user DSP function on a stream, MOD music, or recording channel.\n
        https://www.un4seen.com/doc/#bass/BASS_ChannelSetDSP.html"""
        result = self.dll.BASS_ChannelSetDSP(handle, ctypes.byref(proc), ctypes.byref(user), priority)
        if self.safe and result == 0: self._raise_error('BASS_ChannelSetDSP')
        return result
    
    def ChannelSetFX(self, handle:HANDLE, type:DWORD, priority:INT) -> HFX:
        """Sets an effect on a stream, MOD music, or recording channel.\n
        https://www.un4seen.com/doc/#bass/BASS_ChannelSetFX.html"""
        result = self.dll.BASS_ChannelSetFX(handle, type, priority)
        if self.safe and result == 0: self._raise_error('BASS_ChannelSetFX')
        return result

    def ChannelSetLink(self, handle:HANDLE, chan:HANDLE) -> BOOL:
        """Links two MOD music or stream channels together.\n
        https://www.un4seen.com/doc/#bass/BASS_ChannelSetLink.html"""
        result = self.dll.BASS_ChannelSetLink(handle, chan)
        if self.safe and result == 0: self._raise_error('BASS_ChannelSetLink')
        return result

    def ChannelSetPosition(self, handle:HANDLE, pos:QWORD, mode:DWORD) -> BOOL:
        """Sets the current position of a channel.\n
        https://www.un4seen.com/doc/#bass/BASS_ChannelSetPosition.html"""
        result = self.dll.BASS_ChannelSetPosition(handle, pos, mode)
        if self.safe and result == 0: self._raise_error('BASS_ChannelSetPosition')
        return result
    
    def ChannelSetSync(self, handle:HANDLE, type:DWORD, param:QWORD, proc:SyncProcType|None, user:PTR|None) -> HSYNC:
        """Sets up a synchronizer on a MOD music, stream or recording channel.\n
        https://www.un4seen.com/doc/#bass/BASS_ChannelSetSync.html"""
        result = self.dll.BASS_ChannelSetSync(handle, type, param, ctypes.byref(proc), ctypes.byref(user))
        if self.safe and result == 0: self._raise_error('BASS_ChannelSetSync')
        return result
    
    def ChannelSlideAttribute(self, handle:HANDLE, attr:DWORD, value:FLOAT, time:DWORD) -> BOOL:
        """Slides a channel's attribute from its current value to a new value.\n
        https://www.un4seen.com/doc/#bass/BASS_ChannelSlideAttribute.html"""
        result = self.dll.BASS_ChannelSlideAttribute(handle, attr, value, time)
        if self.safe and result == 0: self._raise_error('BASS_ChannelSlideAttribute')
        return result
    
    def ChannelStart(self, handle:HANDLE) -> BOOL:
        """Starts/resumes playback of a sample, stream, MOD music, or a recording.\n
        https://www.un4seen.com/doc/#bass/BASS_ChannelStart.html"""
        result = self.dll.BASS_ChannelStart(handle)
        if self.safe and result == 0: self._raise_error('BASS_ChannelStart')
        return result
    
    def ChannelStop(self, handle:HANDLE) -> BOOL:
        """Stops a sample, stream, MOD music, or recording.\n
        https://www.un4seen.com/doc/#bass/BASS_ChannelStop.html"""
        result = self.dll.BASS_ChannelStop(handle)
        if self.safe and result == 0: self._raise_error('BASS_ChannelStop')
        return result
    
    def ChannelUpdate(self, handle:HANDLE, length:DWORD) -> BOOL:
        """Updates the playback buffer of a stream or MOD music.\n
        https://www.un4seen.com/doc/#bass/BASS_ChannelUpdate.html"""
        result = self.dll.BASS_ChannelUpdate(handle, length)
        if self.safe and result == 0: self._raise_error('BASS_ChannelUpdate')
        return result
    #endregion

    #region BASS / Effects
    def FXGetParameters(self, handle:HFX, params:PTR|None) -> BOOL:
        """Retrieves the parameters of an effect.\n
        https://www.un4seen.com/doc/#bass/BASS_FXGetParameters.html"""
        result = self.dll.BASS_FXGetParameters(handle, ctypes.byref(params))
        if self.safe and result == 0: self._raise_error('BASS_FXGetParameters')
        return result

    def FXReset(self, handle:HANDLE) -> BOOL:
        """Resets the state of an effect or all effects on a channel.\n
        https://www.un4seen.com/doc/#bass/BASS_FXReset.html"""
        result = self.dll.BASS_FXReset(handle)
        if self.safe and result == 0: self._raise_error('BASS_FXReset')
        return result
    
    def FXSetParameters(self, handle:HFX, params:PTR|None) -> BOOL:
        """Sets the parameters of an effect.\n
        https://www.un4seen.com/doc/#bass/BASS_FXSetParameters.html"""
        result = self.dll.BASS_FXSetParameters(handle, ctypes.byref(params))
        if self.safe and result == 0: self._raise_error('BASS_FXSetParameters')
        return result

    def FXSetPriority(self, handle:HFX, priority:INT) -> BOOL:
        """Sets the priority of an effect or DSP function, which determines its position in the DSP chain.\n
        https://www.un4seen.com/doc/#bass/BASS_FXSetPriority.html"""
        result = self.dll.BASS_FXSetPriority(handle, priority)
        if self.safe and result == 0: self._raise_error('BASS_FXSetPriority')
        return result
    #endregion
#endregion

#region BASSError exception

class BASSError(Exception):
    """ Exception class for BASS library.\n
    Rasied, when BASS return *error* value after executing command, if `basson` created with `safe_executon = True` flag\n
    If you want to determine error you can use comparason `BASSError.code` with his constants:
    ```python
    try:
        basson.init(...)
    except BASSError as e:
        if e.code == BASSError.DEVICE:
            print("Device is busy")
        else:
            raise e
    """
    OK           = 0
    """All is OK"""
    MEM          = 1
    """Memory error"""
    FILEOPEN     = 2
    """Cannot open the file"""
    DRIVER       = 3
    """Cannot find a free or valid driver"""
    BUFLOST      = 4
    """Sample buffer was lost"""
    HANDLE       = 5
    """Invalid handle"""
    FORMAT       = 6
    """Unsupported sample format"""
    POSITION     = 7
    """Invalid position"""
    INIT         = 8
    """`init` call was being failed"""
    START        = 9
    """`start` call was being failed"""
    SSL          = 10
    """SSL/HTTPS support isn't avaliable"""
    REINIT       = 11
    """Device reqied to be reinitialized"""
    ALREADY      = 14
    """Last action already done (`init`, `pause`, etc.)"""
    NOTAUDIO     = 17
    """File doesn't contain audio"""
    NOCHAN       = 18
    """Cannot get a free channel"""
    ILLTYPE      = 19
    """Illegal type specified"""
    ILLPARAM     = 20
    """Illegal parameter specified"""
    NO3D         = 21
    """Driver don't have 3D support"""
    NOEAX        = 22
    """Driver don't have EAX support"""
    DEVICE       = 23
    """Illegal device number"""
    NOPLAY       = 24
    """Channel not playing"""
    FREQ         = 25
    """Illegal samplerate"""
    NOTFILE      = 27
    """The stream is not a file stream"""
    NOHW         = 29
    """No hardware voices avaliable"""
    EMPTY        = 31
    """File don't have sample data"""
    NONET        = 32
    """Internet connection couldn't be opened"""
    CREATE       = 33
    """File couldn't be created"""
    NOFX         = 34
    """FX is not avaliable"""
    NOTAVAIL     = 37
    """Requested data or action is not avaliable"""
    DECODE       = 38
    """Channel is/isn't a decoding channel"""
    DX           = 39
    """Reqested DirectX version don't installed"""
    TIMEOUT      = 40
    """Connection timeout"""
    FILEFORM     = 41
    """Unsupported file format"""
    SPEAKER      = 42
    """Unavaliable speaker"""
    VERSION      = 43
    """Unsupported BASS version (used by plugins)"""
    CODEC        = 44
    """Codec is not avaliable or supported"""
    ENDED        = 45
    """File has been reached end"""
    BUSY         = 46
    """Device is busy"""
    UNSTREAMABLE = 47
    """File is unstremable"""
    PROTOCOL     = 48
    """Unsopported protocol"""
    DENIED       = 49
    """Access denied"""
    #UNKNOWN      = -1 # some other mystery problem
    UNKNOWN      = MINUSONE
    """Some unknown error"""

    # I fucking hate this, don't blame me
    _decsription = {
        OK: "All is OK",
        MEM: "Memory error",
        FILEOPEN: "Cannot open the file",
        DRIVER: "Cannot find a free or valid driver",
        BUFLOST: "Sample buffer was lost",
        HANDLE: "Invalid handle",
        FORMAT: "Unsupported sample format",
        POSITION: "Invalid position",
        INIT: "`init` call was being failed",
        START: "`start` call was being failed",
        SSL: "SSL/HTTPS support isn't avaliable",
        REINIT: "Device reqied to be reinitialized",
        ALREADY: "Last action already done (`init`, `pause`, etc.)",
        NOTAUDIO: "File doesn't contain audio",
        NOCHAN: "Cannot get a free channel",
        ILLTYPE: "Illegal type specified",
        ILLPARAM: "Illegal parameter specified",
        NO3D: "Driver don't have 3D support",
        NOEAX: "Driver don't have EAX support",
        DEVICE: "Illegal device number",
        NOPLAY: "Channel not playing",
        FREQ: "Illegal samplerate",
        NOTFILE: "The stream is not a file stream",
        NOHW: "No hardware voices avaliable",
        EMPTY: "File don't have sample data",
        NONET: "Internet connection couldn't be opened",
        CREATE: "File couldn't be created",
        NOFX: "FX is not avaliable",
        NOTAVAIL: "Requested data or action is not avaliable",
        DECODE: "Channel is/isn't a decoding channel",
        DX: "Reqested DirectX version don't installed",
        TIMEOUT: "Connection timeout",
        FILEFORM: "Unsupported file format",
        SPEAKER: "Unavaliable speaker",
        VERSION: "Unsupported BASS version (used by plugins)",
        CODEC: "Codec is not avaliable or supported",
        ENDED: "File has been reached end",
        BUSY: "Device is busy",
        UNSTREAMABLE: "File is unstremable",
        PROTOCOL: "Unsopported protocol",
        DENIED: "Access denied",
        UNKNOWN: "Some unknown error",
    }

    def __init__(self, code:int, function="<none>"):
        self.code = code
        self.message = f"Function {function} returned error {code}: {self._decsription[code]}"
        super().__init__(self.message)
#endregion