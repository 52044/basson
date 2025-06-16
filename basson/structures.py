from typing import TypedDict
from . import BASS as bass
from . import utils

class Config:
    def __init__(self, lib):
        self.lib = lib

    def _getconf(self, option:str): return self.lib.GetConfig(option)
    def _setconf(self, option:str, value:str): self.lib.SetConfig(option, value)
    def _getconfptr(self, option:str): return self.lib.GetConfigPtr(option)
    def _setconfptr(self, option:str, value:str): self.lib.SetConfigPtr(option, value)
    
    @property
    def algorithm3d(self) -> int:  return self._getconf(bass.BASS_CONFIG_3DALGORITHM)
        
    @algorithm3d.setter
    def algorithm3d(self, algo: int): self._setconf(bass.BASS_CONFIG_3DALGORITHM, algo)

    @property
    def am_disable(self) -> bool: 
        result = self._getconf(bass.BASS_CONFIG_AM_DISABLE)
        return None if result == bass.MINUSONE else result
    @am_disable.setter
    def am_disable(self, algo: bool): self._setconf(bass.BASS_CONFIG_AM_DISABLE, algo)

    @property
    def android_aaudio(self) -> bool: 
        result = self._getconf(bass.BASS_CONFIG_ANDROID_AAUDIO)
        return None if result == bass.MINUSONE else result
    @android_aaudio.setter
    def android_aaudio(self, disable: bool): self._setconf(bass.BASS_CONFIG_ANDROID_AAUDIO, disable)

    @property
    def android_sessionid(self) -> int: 
        result = self._getconf(bass.BASS_CONFIG_ANDROID_SESSIONID)
        return None if result == bass.MINUSONE else result
    @android_sessionid.setter
    def android_sessionid(self, id: int): self._setconf(bass.BASS_CONFIG_ANDROID_SESSIONID, id)

    @property
    def asyncfile_buffer(self) -> int: return self._getconf(bass.BASS_CONFIG_ASYNCFILE_BUFFER)
    @asyncfile_buffer.setter
    def asyncfile_buffer(self, length: int): self._setconf(bass.BASS_CONFIG_ASYNCFILE_BUFFER, length)

    @property
    def buffer(self) -> int: return self._getconf(bass.BASS_CONFIG_BUFFER)
    @buffer.setter
    def buffer(self, length: int): self._setconf(bass.BASS_CONFIG_BUFFER, length)

    @property
    def curve_vol(self) -> bool: return self._getconf(bass.BASS_CONFIG_CURVE_VOL)
    @curve_vol.setter
    def curve_vol(self, logvol: bool): self._setconf(bass.BASS_CONFIG_CURVE_VOL, logvol)

    @property
    def curve_pan(self) -> bool: return self._getconf(bass.BASS_CONFIG_CURVE_PAN)
    @curve_pan.setter
    def curve_pan(self, logpan: bool): self._setconf(bass.BASS_CONFIG_CURVE_PAN, logpan)

    @property
    def dev_buffer(self) -> int: return self._getconf(bass.BASS_CONFIG_DEV_BUFFER)
    @dev_buffer.setter
    def dev_buffer(self, length:int): self._setconf(bass.BASS_CONFIG_DEV_BUFFER, length)

    @property
    def dev_default(self) -> bool: return self._getconf(bass.BASS_CONFIG_DEV_DEFAULT)
    @dev_default.setter
    def dev_default(self, default:bool): self._setconf(bass.BASS_CONFIG_DEV_DEFAULT, default)

    @property
    def dev_nonstop(self) -> bool: return self._getconf(bass.BASS_CONFIG_DEV_NONSTOP)
    @dev_nonstop.setter
    def dev_nonstop(self, nonstop:bool): self._setconf(bass.BASS_CONFIG_DEV_NONSTOP, nonstop)

    @property
    def dev_period(self) -> int: return self._getconf(bass.BASS_CONFIG_DEV_PERIOD)
    @dev_period.setter
    def dev_period(self, period:int): self._setconf(bass.BASS_CONFIG_DEV_PERIOD, period)

    @property
    def filename(self) -> str: return utils.readPtr(self._getconfptr(bass.BASS_CONFIG_FILENAME), 'str')

    @property
    def floatdsp(self) -> bool: return self._getconf(bass.BASS_CONFIG_FLOATDSP)
    @floatdsp.setter
    def floatdsp(self, floatdsp:bool): self._setconf(bass.BASS_CONFIG_FLOATDSP, floatdsp)

    @property
    def gvol_music(self) -> int: return self._getconf(bass.BASS_CONFIG_GVOL_MUSIC)
    @gvol_music.setter
    def gvol_music(self, volume:int): self._setconf(bass.BASS_CONFIG_GVOL_MUSIC, volume)

    @property
    def gvol_sample(self) -> int: return self._getconf(bass.BASS_CONFIG_GVOL_SAMPLE)
    @gvol_sample.setter
    def gvol_sample(self, volume:int): self._setconf(bass.BASS_CONFIG_GVOL_SAMPLE, volume)

    @property
    def gvol_stream(self) -> int: return self._getconf(bass.BASS_CONFIG_GVOL_STREAM)
    @gvol_stream.setter
    def gvol_stream(self, volume:int): self._setconf(bass.BASS_CONFIG_GVOL_STREAM, volume)

    @property
    def handles(self) -> int: return self._getconf(bass.BASS_CONFIG_HANDLES)
                                          
    @property
    def ios_session(self) -> int: return self._getconf(bass.BASS_CONFIG_IOS_SESSION)
    @ios_session.setter
    def ios_session(self, config: int): self._setconf(bass.BASS_CONFIG_IOS_SESSION, config)

    @property
    def libssl(self) -> str: return utils.readPtr(self._getconfptr(bass.BASS_CONFIG_LIBSSL), 'str')
    @libssl.setter
    def libssl(self, filename:str): self._setconf(bass.BASS_CONFIG_LIBSSL, filename)

    @property
    def mf_disable(self) -> bool: return self._getconf(bass.BASS_CONFIG_MF_DISABLE)
    @mf_disable.setter
    def mf_disable(self, disable:bool): self._setconf(bass.BASS_CONFIG_MF_DISABLE, disable)

    @property
    def mf_video(self) -> bool: return self._getconf(bass.BASS_CONFIG_MF_VIDEO)
    @mf_video.setter
    def mf_video(self, video:bool): self._setconf(bass.BASS_CONFIG_MF_VIDEO, video)

    @property
    def music_virtual(self) -> int: return self._getconf(bass.BASS_CONFIG_MUSIC_VIRTUAL)
    @music_virtual.setter
    def music_virtual(self, chans:int): self._setconf(bass.BASS_CONFIG_MUSIC_VIRTUAL, chans)

    @property
    def net_agent(self) -> str: return utils.readPtr(self._getconfptr(bass.BASS_CONFIG_NET_AGENT), 'str')
    @net_agent.setter
    def net_agent(self, agent:str): self._setconf(bass.BASS_CONFIG_NET_AGENT, agent)

    @property
    def net_buffer(self) -> int: return self._getconf(bass.BASS_CONFIG_NET_BUFFER)
    @net_buffer.setter
    def net_buffer(self, length:int): self._setconf(bass.BASS_CONFIG_NET_BUFFER, length)

    @property
    def net_meta(self) -> bool: return self._getconf(bass.BASS_CONFIG_NET_META)
    @net_meta.setter
    def net_meta(self, metadata:bool): self._setconf(bass.BASS_CONFIG_NET_META, metadata)

    @property
    def net_passive(self) -> bool: return self._getconf(bass.BASS_CONFIG_NET_PASSIVE)
    @net_passive.setter
    def net_passive(self, passive:bool): self._setconf(bass.BASS_CONFIG_NET_PASSIVE, passive)
    
    @property
    def net_playlist(self) -> int: return self._getconf(bass.BASS_CONFIG_NET_PLAYLIST)
    @net_playlist.setter
    def net_playlist(self, playlist:int): self._setconf(bass.BASS_CONFIG_NET_PLAYLIST, playlist)

    @property
    def net_playlist_depth(self) -> int: return self._getconf(bass.BASS_CONFIG_NET_PLAYLIST_DEPTH)
    @net_playlist_depth.setter
    def net_playlist_depth(self, depth:int): self._setconf(bass.BASS_CONFIG_NET_PLAYLIST_DEPTH, depth)
    
    @property
    def net_prebuf(self) -> int: return self._getconf(bass.BASS_CONFIG_NET_PREBUF)
    @net_prebuf.setter
    def net_prebuf(self, length:int): self._setconf(bass.BASS_CONFIG_NET_PREBUF, length)
    
    @property
    def net_proxy(self) -> str: return utils.readPtr(self._getconfptr(bass.BASS_CONFIG_NET_PROXY), 'str')
    @net_proxy.setter
    def net_proxy(self, proxy:str|None): self._setconf(bass.BASS_CONFIG_NET_PROXY, proxy)

    @property
    def net_readtimeout(self) -> int: return self._getconf(bass.BASS_CONFIG_NET_READTIMEOUT)
    @net_readtimeout.setter
    def net_readtimeout(self, timeout:int): self._setconf(bass.BASS_CONFIG_NET_READTIMEOUT, timeout)
    
    @property
    def net_restrate(self) -> int: return self._getconf(bass.BASS_CONFIG_NET_RESTRATE)
    @net_restrate.setter
    def net_restrate(self, rate:int): self._setconf(bass.BASS_CONFIG_NET_RESTRATE, rate)

    @property
    def net_timeout(self) -> int: return self._getconf(bass.BASS_CONFIG_NET_TIMEOUT)
    @net_timeout.setter
    def net_timeout(self, timeout:int): self._setconf(bass.BASS_CONFIG_NET_TIMEOUT, timeout)

    @property
    def noramp(self) -> int: return self._getconf(bass.BASS_CONFIG_NORAMP)
    @noramp.setter
    def noramp(self, noramp:int): self._setconf(bass.BASS_CONFIG_NORAMP, noramp)

    @property
    def ogg_prescan(self) -> bool: return self._getconf(bass.BASS_CONFIG_OGG_PRESCAN)
    @ogg_prescan.setter
    def ogg_prescan(self, prescan:bool): self._setconf(bass.BASS_CONFIG_OGG_PRESCAN, prescan)

    @property
    def pause_noplay(self) -> bool: return self._getconf(bass.BASS_CONFIG_PAUSE_NOPLAY)
    @pause_noplay.setter
    def pause_noplay(self, noplay:bool): self._setconf(bass.BASS_CONFIG_PAUSE_NOPLAY, noplay)

    @property
    def rec_buffer(self) -> int: return self._getconf(bass.BASS_CONFIG_REC_BUFFER)
    @rec_buffer.setter
    def rec_buffer(self, length:int): self._setconf(bass.BASS_CONFIG_REC_BUFFER, length)

    @property
    def rec_wasapi(self) -> bool: return self._getconf(bass.BASS_CONFIG_REC_WASAPI)
    @rec_wasapi.setter
    def rec_wasapi(self, enable:bool): self._setconf(bass.BASS_CONFIG_REC_WASAPI, enable)

    @property
    def sample_onehandle(self) -> bool: return self._getconf(bass.BASS_CONFIG_SAMPLE_ONEHANDLE)
    @sample_onehandle.setter
    def sample_onehandle(self, onehandle:bool): self._setconf(bass.BASS_CONFIG_SAMPLE_ONEHANDLE, onehandle)

    @property
    def src(self) -> int: return self._getconf(bass.BASS_CONFIG_SRC)
    @src.setter
    def src(self, quality:int): self._setconf(bass.BASS_CONFIG_SRC, quality)

    @property
    def src_sample(self) -> int: return self._getconf(bass.BASS_CONFIG_SRC_SAMPLE)
    @src_sample.setter
    def src_sample(self, quality:int): self._setconf(bass.BASS_CONFIG_SRC_SAMPLE, quality)

    @property
    def unicode(self) -> bool: return self._getconf(bass.BASS_CONFIG_UNICODE)
    @unicode.setter
    def unicode(self, unicode:bool): self._setconf(bass.BASS_CONFIG_UNICODE, unicode)

    @property
    def updateperiod(self) -> int: return self._getconf(bass.BASS_CONFIG_UPDATEPERIOD)
    @updateperiod.setter
    def updateperiod(self, period:int): self._setconf(bass.BASS_CONFIG_UPDATEPERIOD, period)

    @property
    def updatethreads(self) -> int: return self._getconf(bass.BASS_CONFIG_UPDATETHREADS)
    @updatethreads.setter
    def updatethreads(self, threads:int): self._setconf(bass.BASS_CONFIG_UPDATETHREADS, threads)

    @property
    def verify(self) -> int: return self._getconf(bass.BASS_CONFIG_VERIFY)
    @verify.setter
    def verify(self, length:int): self._setconf(bass.BASS_CONFIG_VERIFY, length)

    @property
    def verify_net(self) -> int: return self._getconf(bass.BASS_CONFIG_VERIFY_NET)
    @verify_net.setter
    def verify_net(self, length:int): self._setconf(bass.BASS_CONFIG_VERIFY_NET, length)

    @property
    def wasapi_persist(self) -> bool: return self._getconf(bass.BASS_CONFIG_WASAPI_PERSIST)
    @wasapi_persist.setter
    def wasapi_persist(self, persist:bool): self._setconf(bass.BASS_CONFIG_WASAPI_PERSIST, persist)

class DeviceInfo(TypedDict):
    ''' Dictionary for using with `Device` and `RecordDevice` properties'''
    name: str
    ''' Description of the device '''
    flags: str
    ''' The device's current status, a combination of flags'''#TODO flags
    driver: str 
    ''' Driver identification '''

class Info(TypedDict):
    ''' Dictionary for using with `Info` property'''
    flags: int
    ''' The device's DirectSound capabilities, a combination of flags''' #TODO flags
    minbuf: int
    ''' The minimum buffer length (rounded up to the nearest millisecond) to avoid stuttering playback '''
    dsver: int
    '''DirectSound version.\n 
    `9` = DX9/8/7/5 features are available,\n 
    `8` = DX8/7/5 features are available,\n 
    `7` = DX7/5 features are available,\n 
    `5` = DX5 features are available,\n 
    `0` = none of the DX9/8/7/5 features are available'''
    latency: int
    ''' The average delay (rounded up to the nearest millisecond) for channel playback to start and be heard '''
    initfalgs: int
    ''' The flags parameter of the `Init` call. This will include any flags that were applied automatically'''
    speakers: int
    ''' The number of available speakers, which can be accessed via the speaker assignment flags '''
    freq: int
    ''' The output rate '''
