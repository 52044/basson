
# Comparison chart of Basson wraper and OG BASS

### class BASS

Basson | BASS | Comment
--- | --- | ---
`BASS.error_code`   | `BASS_ErrorGetCode()` | Probably useless, because wraper itself raises `BASSException` and other exceptions, if BASS function returns 'error' value. Of course, if `BASS.__init__(.., safe_execution=True)`
`BASS.__delattr__()` | `BASS_Free()` | After object destruction BASS frees himself
`BASS.cpu_usage`    | `BASS_GetCPU()` | Renamed for clarity of understanding
`BASS.device`       | `BASS_GetDevice()`, `BASS_SetDevice()` | .
`BASS.volume`       | `BASS_GetVolume()`, `BASS_SetVolume()` | .
`BASS.version`      | `BASS_GetVersion()` | Returns `int` from BASS library. Use `BASS.utils.decode_version(x)` for human-readable version
`BASS.pause()`      | `BASS_Pause()` | .
`BASS.start()`      | `BASS_Start()` | .
`BASS.stop()`       | `BASS_Stop()` | .
`BASS.update()`     | `BASS_Update()` | .
`BASS.init()`       | `BASS_Init()` | .
`BASS.status`       | `BASS_IsStarted()` | Renamed for clarity of understanding
`BASS.device_info()` | `BASS_GetDeviceInfo()` | .
`BASS.info()`       | `BASS_GetInfo()` | .
.                   | `BASS_GetConfig()`, `BASS_GetConfigPtr`, `BASS_SetConfig()`, `BASS_SetConfigPtr()` | All configs implemented in main class as properties

The following table continues the previous one, except that the BASS column contains a parameter derived from the corresponding `BASS_*Config*()` functions

Basson | BASS | Comment
--- | --- | ---
`BASS.am_disable`   | `BASS_CONFIG_AM_DISABLE` |.
`BASS.android_aaudio` | `BASS_CONFIG_ANDROID_AAUDIO` | .
`BASS.android_sessionid` | `BASS_CONFIG_ANDROID_SESSIONID` | .
`BASS.asyncfile_buffer` | `BASS_CONFIG_ASYNCFILE_BUFFER` | .
`BASS.buffer`       | `BASS_CONFIG_BUFFER` | .
`BASS.curve_vol`    | `BASS_CONFIG_CURVE_VOL` | .
`BASS.curve_pan`    | `BASS_CONFIG_CURVE_PAN` | .
`BASS.dev_buffer`   | `BASS_CONFIG_DEV_BUFFER` | .
`BASS.dev_default`  | `BASS_CONFIG_DEV_DEFAULT` | .
`BASS.dev_nonstop`  | `BASS_CONFIG_DEV_NONSTOP` | .
`BASS.dev_period`   | `BASS_CONFIG_DEV_PERIOD` | .
`BASS.floatdsp`     | `BASS_CONFIG_FLOATDSP` | .
`BASS.gvol_music`   | `BASS_CONFIG_GVOL_MUSIC` | .
`BASS.gvol_sample`  | `BASS_CONFIG_GVOL_SAMPLE` | .
`BASS.gvol_stream`  | `BASS_CONFIG_GVOL_STREAM` | .
`BASS.ios_session`  | `BASS_CONFIG_IOS_SESSION` | .
`BASS.libssl`       | `BASS_CONFIG_LIBSSL` | .
`BASS.mf_disable`   | `BASS_CONFIG_MF_DISABLE` | .
`BASS.mf_video`     | `BASS_CONFIG_MF_VIDEO` | .
`BASS.music_virtual` | `BASS_CONFIG_MUSIC_VIRTUAL` | .
`BASS.net_agent`    | `BASS_CONFIG_NET_AGENT` | .
`BASS.net_buffer`   | `BASS_CONFIG_NET_BUFFER` | .
`BASS.net_meta`     | `BASS_CONFIG_NET_META` | .
`BASS.net_passive`  | `BASS_CONFIG_NET_PASSIVE` | .
`BASS.net_playlist` | `BASS_CONFIG_NET_PLAYLIST` | .
`BASS.net_playlist_depth` | `BASS_CONFIG_NET_PLAYLIST_DEPTH` | .
`BASS.net_prebuf`   | `BASS_CONFIG_NET_PREBUF` | .
`BASS.net_proxy`    | `BASS_CONFIG_NET_PROXY` | .
`BASS.net_readtimeout` | `BASS_CONFIG_NET_READTIMEOUT` | .
`BASS.net_restrate` | `BASS_CONFIG_NET_RESTRATE` | .
`BASS.net_timeout`  | `BASS_CONFIG_NET_TIMEOUT` | .
`BASS.noramp`       | `BASS_CONFIG_NORAMP` | .
`BASS.ogg_prescan`  | `BASS_CONFIG_OGG_PRESCAN` | .
`BASS.pause_noplay` | `BASS_CONFIG_PAUSE_NOPLAY` | .
`BASS.rec_buffer`   | `BASS_CONFIG_REC_BUFFER` | .
`BASS.rec_wasapi`   | `BASS_CONFIG_REC_WASAPI` | .
`BASS.sample_onehandle` | `BASS_CONFIG_SAMPLE_ONEHANDLE`| .
`BASS.src`          | `BASS_CONFIG_SRC`| .
`BASS.src_sample`   | `BASS_CONFIG_SRC_SAMPLE`| .
`BASS.unicode`      | `BASS_CONFIG_UNICODE` | .
`BASS.updateperiod` | `BASS_CONFIG_UPDATEPERIOD` | .
`BASS.updatethreads` | `BASS_CONFIG_UPDATETHREADS` | .
`BASS.verify`       | `BASS_CONFIG_VERIFY` | .
`BASS.verify_net`   | `BASS_CONFIG_VERIFY_NET` | .
`BASS.wasapi_persist` | `BASS_CONFIG_WASAPI_PERSIST` | .