from .api import api, header
from .api import structures as cstrct
from .api.headprivate import ConfigOptions as cfgo
from .api.types import MINUSONE
from . import structures as pstrct
from . import utils

class BASS():
    def __init__(self, dll_path:str, safe_execution:bool=True):
        ''' Python-frendly wrapper over BASS library
        
        :param dll_path: Path to BASS dll
        :param safe_execution: If BASS after execution command returns `error` value, code will raise exception'''

        if dll_path == None: raise ValueError('Path to BASS library don\'t setted')#TODO autodetection
        self.bass = api.BASS(dll_path, safe_execution)
        
        #self.config = pstrct.BassConfig(self.bass)

    def __delattr__(self, name):
        #Safe closing
        self.bass.__delattr__(name)

#region Core functions
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
    
    def init(self, device:int, samplerate:int, flags:header.DeviceFlags):
        ''' Initialize output device 
        
        :param device: Number of desirable audio device.\n
            Set to `-1` to default device, `0` - no output
        :param samplerate: Samplerate of output audiostreams
        :param flags: Combinations of `DeviceFlags`'''
        self.bass.Init(device, samplerate, flags, 0, None)

    @property
    def status(self) -> header.StatusOptions:
        ''' Status of output device '''
        return self.bass.IsStarted()
    
    def device_info(self, device:int) -> pstrct.DeviceInfo:
        ''' Retrives information on an output device'''
        info = cstrct.BASS_DEVICEINFO()
        self.bass.GetDeviceInfo(device, info)
        return {
            'driver': info.driver.decode(),
            'flags': info.flags,
            'name': info.name.decode(utils.get_locale())
        }
    
    def info(self) -> pstrct.Info:
        ''' Get information of current using device. '''
        info = cstrct.BASS_INFO()
        self.bass.GetInfo(info)
        return {
            'dsver': info.dsver,
            'flags': info.flags,
            'freq': info.freq,
            'initflags': info.initflags,
            'latency': info.latency,
            'minbuf': info.minbuf,
            'speakers': info.speakers
        }
#endregion

# region Config

    def _getconf(self, option:str): 
        try:
            return self.bass.GetConfig(option)
        except api.BassException as e:
            if e.code == 20:
                return None
    def _setconf(self, option:str, value:str): 
        self.bass.SetConfig(option, value)
    def _getconfptr(self, option:str):
        try:
            return self.bass.GetConfigPtr(option)
        except api.BassException as e:
            if e.code == 20:
                return None
    def _setconfptr(self, option:str, value:str): 
        self.bass.SetConfigPtr(option, value)

    @property
    def algorithm3d(self) -> header.D3AlorithmsOptions:  
        ''' The positioning algorithm for 3D channels '''
        return self._getconf(cfgo.ALGORITHM3D)
    @algorithm3d.setter
    def algorithm3d(self, algo: header.D3AlorithmsOptions): 
        self._setconf(cfgo.ALGORITHM3D, algo)

    @property
    def am_disable(self) -> bool: 
        ''' `[Android]` Disable usage of Android media codecs'''
        result = self._getconf(cfgo.AM_DISABLE)
        return result
    @am_disable.setter
    def am_disable(self, disable: bool): 
        if self._isandroid:
            self._setconf(cfgo.AM_DISABLE, disable)

    @property
    def android_aaudio(self) -> bool: 
        ''' `[Android]` Enable AAudio outpt on Android'''
        result = self._getconf(cfgo.ANDROID_AAUDIO)
        return None if result == MINUSONE else result
    @android_aaudio.setter
    def android_aaudio(self, disable: bool): 
        self._setconf(cfgo.ANDROID_AAUDIO, disable)

    @property
    def android_sessionid(self) -> int:
        ''' `[Android]` Audio session ID to use for output '''
        result = self._getconf(cfgo.ANDROID_SESSIONID)
        return None if result == MINUSONE else result
    @android_sessionid.setter
    def android_sessionid(self, id: int): 
        self._setconf(cfgo.ANDROID_SESSIONID, id)

    @property
    def asyncfile_buffer(self) -> int: 
        ''' Buffer length (bytes) for async file reading. Will be rounded up to nearest 4kb.'''
        return self._getconf(cfgo.ASYNCFILE_BUFFER)
    @asyncfile_buffer.setter
    def asyncfile_buffer(self, length: int): 
        self._setconf(cfgo.ASYNCFILE_BUFFER, length)

    @property
    def buffer(self) -> int: 
        ''' Playback buffer lenght for `HStream` and `HMusic` channels (ms). Capped boundaries: `10 >= length <= 5000`'''
        return self._getconf(cfgo.BUFFER)
    @buffer.setter
    def buffer(self, length: int):
        self._setconf(cfgo.BUFFER, length)

    @property
    def curve_vol(self) -> bool:
        ''' Translations curve of volume values. This config used by `BASS.volume`'''#FIXME ChannelSet3DAttributes  BASS_ATTRIB_VOL
        return self._getconf(cfgo.CURVE_VOL)
    @curve_vol.setter
    def curve_vol(self, logvol: bool): 
        self._setconf(cfgo.CURVE_VOL, logvol)

    @property
    def curve_pan(self) -> bool: 
        ''' Translation curve of panning values. Affect the same way, as `.curve_vol`'''
        return self._getconf(cfgo.CURVE_PAN)
    @curve_pan.setter
    def curve_pan(self, logpan: bool): 
        self._setconf(cfgo.CURVE_PAN, logpan)

    @property
    def dev_buffer(self) -> int: 
        ''' Output device buffer lenght (ms)'''
        return self._getconf(cfgo.DEV_BUFFER)
    @dev_buffer.setter
    def dev_buffer(self, length:int):
        self._setconf(cfgo.DEV_BUFFER, length)

    @property
    def dev_default(self) -> bool: 
        '''`[Windows, MacOS]` Include `Defalut` entry in output device list '''
        return self._getconf(cfgo.DEV_DEFAULT)
    @dev_default.setter
    def dev_default(self, default:bool):
        self._setconf(cfgo.DEV_DEFAULT, default)

    @property
    def dev_nonstop(self) -> bool: 
        ''' Do not stop output device when nothing is playing on it '''
        return self._getconf(cfgo.DEV_NONSTOP)
    @dev_nonstop.setter
    def dev_nonstop(self, nonstop:bool): 
        self._setconf(cfgo.DEV_NONSTOP, nonstop)

    @property
    def dev_period(self) -> int: 
        ''' Output device update period. If `>0` - in ms, if `<0` - in samples'''
        return self._getconf(cfgo.DEV_PERIOD)
    @dev_period.setter
    def dev_period(self, period:int):
        self._setconf(cfgo.DEV_PERIOD, period)

    @property
    def filename(self) -> str: 
        ''' Filename of loaded BASS library'''
        return utils.read_ptr(self._getconfptr(cfgo.FILENAME), 'str')

    @property
    def floatdsp(self) -> bool: 
        ''' Pass 32-bit float-point sample data to DSP functions '''
        return self._getconf(cfgo.FLOATDSP)
    @floatdsp.setter
    def floatdsp(self, floatdsp:bool): 
        self._setconf(cfgo.FLOATDSP, floatdsp)

    @property
    def gvol_music(self) -> int: 
        ''' Global MOD music level (0-10k)'''
        return self._getconf(cfgo.GVOL_MUSIC)
    @gvol_music.setter
    def gvol_music(self, volume:int): 
        self._setconf(cfgo.GVOL_MUSIC, volume)

    @property
    def gvol_sample(self) -> int: 
        ''' Global Sample volume level (0-10k)'''
        return self._getconf(cfgo.GVOL_SAMPLE)
    @gvol_sample.setter
    def gvol_sample(self, volume:int): 
        self._setconf(cfgo.GVOL_SAMPLE, volume)

    @property
    def gvol_stream(self) -> int: 
        ''' Global Stream volume level (0-10k)'''
        return self._getconf(cfgo.GVOL_STREAM)
    @gvol_stream.setter
    def gvol_stream(self, volume:int): 
        self._setconf(cfgo.GVOL_STREAM, volume)

    @property
    def handles(self) -> int: 
        ''' Number of existing handles - `HMusic`, `HRecord`, `HSample`, `HStream`'''
        return self._getconf(cfgo.HANDLES)
                                          
    @property
    def ios_session(self) -> header.IOSSessionFlags: 
        '''[iOS] Audio session configuration'''
        #TODO check for -1
        return self._getconf(cfgo.IOS_SESSION)
    @ios_session.setter
    def ios_session(self, config: header.IOSSessionFlags): 
        self._setconf(cfgo.IOS_SESSION, config)

    @property
    def libssl(self) -> str: 
        #FIXME LibSSL param can be None, and utils.read_ptr cannot understand that
        ''' Path to OpenSSL library. `None` - use default '''
        return utils.read_ptr(self._getconfptr(cfgo.LIBSSL), 'str')
    @libssl.setter
    def libssl(self, filename:str): 
        self._setconf(cfgo.LIBSSL, filename)

    @property
    def mf_disable(self) -> bool: 
        ''' Disable usage of Media Foundation '''
        return self._getconf(cfgo.MF_DISABLE)
    @mf_disable.setter
    def mf_disable(self, disable:bool):
        self._setconf(cfgo.MF_DISABLE, disable)

    @property
    def mf_video(self) -> bool: 
        ''' Accept playback audio from videofiles using Media Foundation '''
        return self._getconf(cfgo.MF_VIDEO)
    @mf_video.setter
    def mf_video(self, video:bool): 
        self._setconf(cfgo.MF_VIDEO, video)

    @property
    def music_virtual(self) -> int:
        ''' Maximum nuber of virtual channel to use in rendering of `IT` fules''' 
        return self._getconf(cfgo.MUSIC_VIRTUAL)
    @music_virtual.setter
    def music_virtual(self, chans:int): 
        self._setconf(cfgo.MUSIC_VIRTUAL, chans)

    @property
    def net_agent(self) -> str: 
        ''' `User-Agent` field sent to servers '''
        return utils.read_ptr(self._getconfptr(cfgo.NET_AGENT), 'str')
    @net_agent.setter
    def net_agent(self, agent:str): 
        self._setconf(cfgo.NET_AGENT, agent)

    @property
    def net_buffer(self) -> int: 
        ''' Length of internet download buffer '''
        return self._getconf(cfgo.NET_BUFFER)
    @net_buffer.setter
    def net_buffer(self, length:int):
        self._setconf(cfgo.NET_BUFFER, length)

    @property
    def net_meta(self) -> bool: 
        ''' Request Shoutcast metadata from servers '''
        return self._getconf(cfgo.NET_META)
    @net_meta.setter
    def net_meta(self, metadata:bool): 
        self._setconf(cfgo.NET_META, metadata)

    @property
    def net_passive(self) -> bool: 
        ''' Enable passive mode in FTP connections '''
        return self._getconf(cfgo.NET_PASSIVE)
    @net_passive.setter
    def net_passive(self, passive:bool): 
        self._setconf(cfgo.NET_PASSIVE, passive)
    
    @property
    def net_playlist(self) -> header.NetPlaylistOptions: 
        ''' Enable process URLs in PSL and M3U playlists'''
        return self._getconf(cfgo.NET_PLAYLIST)
    @net_playlist.setter
    def net_playlist(self, playlist:header.NetPlaylistOptions): 
        self._setconf(cfgo.NET_PLAYLIST, playlist)

    @property
    def net_playlist_depth(self) -> int: 
        ''' Maximum nested playlist processing depth '''
        return self._getconf(cfgo.NET_PLAYLIST_DEPTH)
    @net_playlist_depth.setter
    def net_playlist_depth(self, depth:int):
        self._setconf(cfgo.NET_PLAYLIST_DEPTH, depth)
    
    @property
    def net_prebuf(self) -> int: 
        ''' Amount to pre-buffer before playing internet streams (%)'''
        return self._getconf(cfgo.NET_PREBUF)
    @net_prebuf.setter
    def net_prebuf(self, length:int): 
        self._setconf(cfgo.NET_PREBUF, length)
    
    @property
    def net_proxy(self) -> str|None: 
        ''' Proxy server settings\n
        `None` - Do not use proxy\n
        `empty string` - Use OS proxy settings\n
        `server:port` - Connect to proxy w/a auth\n
        `user:pass@server:port` - Connect to proxy w/ auth'''
        return utils.read_ptr(self._getconfptr(cfgo.NET_PROXY), 'str')
    @net_proxy.setter
    def net_proxy(self, proxy:str|None): 
        self._setconf(cfgo.NET_PROXY, proxy)

    @property
    def net_readtimeout(self) -> int: 
        ''' Time to wait for server to deliver more data for an internet stream'''
        return self._getconf(cfgo.NET_READTIMEOUT)
    @net_readtimeout.setter
    def net_readtimeout(self, timeout:int): 
        self._setconf(cfgo.NET_READTIMEOUT, timeout)
    
    @property
    def net_restrate(self) -> int: 
        ''' Restricted download rate for internet file streams (b/s)'''
        return self._getconf(cfgo.NET_RESTRATE)
    @net_restrate.setter
    def net_restrate(self, rate:int):
        self._setconf(cfgo.NET_RESTRATE, rate)

    @property
    def net_timeout(self) -> int: 
        ''' Time to wat for a server to respond to a connection request (ms)'''
        return self._getconf(cfgo.NET_TIMEOUT)
    @net_timeout.setter
    def net_timeout(self, timeout:int): 
        self._setconf(cfgo.NET_TIMEOUT, timeout)

    @property
    def noramp(self) -> header.NorampOptions:
        ''' Playback ramping setting'''
        return self._getconf(cfgo.NORAMP)
    @noramp.setter
    def noramp(self, noramp:header.NorampOptions): 
        self._setconf(cfgo.NORAMP, noramp)

    @property
    def ogg_prescan(self) -> bool: 
        ''' Pre-scan chained OGG files '''
        return self._getconf(cfgo.OGG_PRESCAN)
    @ogg_prescan.setter
    def ogg_prescan(self, prescan:bool): 
        self._setconf(cfgo.OGG_PRESCAN, prescan)

    @property
    def pause_noplay(self) -> bool: 
        ''' Prevent channels playback if output is paused '''
        return self._getconf(cfgo.PAUSE_NOPLAY)
    @pause_noplay.setter
    def pause_noplay(self, noplay:bool): 
        self._setconf(cfgo.PAUSE_NOPLAY, noplay)

    @property
    def rec_buffer(self) -> int: 
        '''Buffer length for recording channels (10 ... 5000 ms)'''
        return self._getconf(cfgo.REC_BUFFER)
    @rec_buffer.setter
    def rec_buffer(self, length:int): 
        self._setconf(cfgo.REC_BUFFER, length)

    @property
    def rec_wasapi(self) -> bool: 
        '''[Windows] Enable usage WASAPI when recording'''
        return self._getconf(cfgo.REC_WASAPI)
    @rec_wasapi.setter
    def rec_wasapi(self, enable:bool): 
        self._setconf(cfgo.REC_WASAPI, enable)

    @property
    def sample_onehandle(self) -> bool: 
        ''' enable usage of same handle for a sample and its single playback channel '''
        return self._getconf(cfgo.SAMPLE_ONEHANDLE)
    @sample_onehandle.setter
    def sample_onehandle(self, onehandle:bool): 
        self._setconf(cfgo.SAMPLE_ONEHANDLE, onehandle)

    @property
    def src(self) -> header.SamplerateConversionOptions|int: 
        ''' Default samplerate conversion quality'''
        return self._getconf(cfgo.SRC)
    @src.setter
    def src(self, quality:header.SamplerateConversionOptions|int):
        self._setconf(cfgo.SRC, quality)

    @property
    def src_sample(self) -> header.SamplerateConversionOptions|int: 
        ''' Default samplerate conversion quality for sample channels'''
        return self._getconf(cfgo.SRC_SAMPLE)
    @src_sample.setter
    def src_sample(self, quality:header.SamplerateConversionOptions|int): 
        self._setconf(cfgo.SRC_SAMPLE, quality)

    @property
    def unicode(self) -> bool: 
        ''' Use Unicode in device information'''
        return self._getconf(cfgo.UNICODE)
    @unicode.setter
    def unicode(self, unicode:bool): 
        self._setconf(cfgo.UNICODE, unicode)

    @property
    def updateperiod(self) -> int: 
        ''' Update period of `HStream` and `HMusic` channel playback buffers (0, 5 ... 100 ms, autocap)'''
        return self._getconf(cfgo.UPDATEPERIOD)
    @updateperiod.setter
    def updateperiod(self, period:int): 
        self._setconf(cfgo.UPDATEPERIOD, period)

    @property
    def updatethreads(self) -> int: 
        ''' Nuber of threads to use for updating playback buffers '''
        return self._getconf(cfgo.UPDATETHREADS)
    @updatethreads.setter
    def updatethreads(self, threads:int): 
        self._setconf(cfgo.UPDATETHREADS, threads)

    @property
    def verify(self) -> int: 
        ''' Amount of data to check in order to verify/detect file format (1k ... 1M bytes, autocap)'''
        return self._getconf(cfgo.VERIFY)
    @verify.setter
    def verify(self, length:int): 
        self._setconf(cfgo.VERIFY, length)

    @property
    def verify_net(self) -> int: 
        ''' Amount of data to check in order to verify/detect file format of internet streams (1k ... 1M bytes, autocap)'''
        return self._getconf(cfgo.VERIFY_NET)
    @verify_net.setter
    def verify_net(self, length:int): 
        self._setconf(cfgo.VERIFY_NET, length)

    @property
    def wasapi_persist(self) -> bool: 
        '''[Windows] Retain Windows mixer settings across sessions'''
        return self._getconf(cfgo.WASAPI_PERSIST)
    @wasapi_persist.setter
    def wasapi_persist(self, persist:bool):
        self._setconf(cfgo.WASAPI_PERSIST, persist)
#endregion

#region Plugins
    #TODO bass plugins
    def plugin_enable(self, *args):
        raise NotImplementedError("Plugin functionality not implemented yet.")
    def plugin_free(self, *args):
        raise NotImplementedError("Plugin functionality not implemented yet.")
    def plugin_get_info(self, *args):
        raise NotImplementedError("Plugin functionality not implemented yet.")
    def plugin_load(self, *args):
        raise NotImplementedError("Plugin functionality not implemented yet.")