
# Comparison chart of Basson wraper and OG BASS

### class BASS

Basson | BASS | Comment
--- | --- | ---
`Basson.error_code`   | `BASS_ErrorGetCode()` | Wraper itself raises `BASSError` and other exceptions, if BASS function returns 'error' value. Of course, if `Basson.__init__(.., safe_execution=True)`
`Basson.__delattr__()` | `BASS_Free()` | After object destruction BASS frees himself
`Basson.cpu_usage`    | `BASS_GetCPU()` | Renamed for ease of understanding
`Basson.device`       | `BASS_GetDevice()`, `BASS_SetDevice()` | 
`Basson.volume`       | `BASS_GetVolume()`, `BASS_SetVolume()` | 
`Basson.version`      | `BASS_GetVersion()` | Returns decoded `str` or hex `int`
`Basson.pause()`      | `BASS_Pause()` | 
`Basson.start()`      | `BASS_Start()` | 
`Basson.stop()`       | `BASS_Stop()` | 
`Basson.update()`     | `BASS_Update()` | 
`Basson.init()`       | `BASS_Init()` | 
`Basson.status`       | `BASS_IsStarted()` | Renamed for ease of understanding
`Basson.device_info()` | `BASS_GetDeviceInfo()` | 
`Basson.info()`       | `BASS_GetInfo()` | 
\-                  | `BASS_GetConfig()`, `BASS_GetConfigPtr`, `BASS_SetConfig()`, `BASS_SetConfigPtr()` | All configs implemented in main class as properties
`Basson.am_disable`   | `BASS_*Config*(BASS_CONFIG_AM_DISABLE)` |
`Basson.android_aaudio` | `BASS_*Config*(BASS_CONFIG_ANDROID_AAUDIO)` | 
`Basson.android_sessionid` | `BASS_*Config*(BASS_CONFIG_ANDROID_SESSIONID)` | 
`Basson.asyncfile_buffer` | `BASS_*Config*(BASS_CONFIG_ASYNCFILE_BUFFER)` | 
`Basson.buffer`       | `BASS_*Config*(BASS_CONFIG_BUFFER)` | 
`Basson.curve_vol`    | `BASS_*Config*(BASS_CONFIG_CURVE_VOL)` | 
`Basson.curve_pan`    | `BASS_*Config*(BASS_CONFIG_CURVE_PAN)` | 
`Basson.dev_buffer`   | `BASS_*Config*(BASS_CONFIG_DEV_BUFFER)` | 
`Basson.dev_default`  | `BASS_*Config*(BASS_CONFIG_DEV_DEFAULT)` | 
`Basson.dev_nonstop`  | `BASS_*Config*(BASS_CONFIG_DEV_NONSTOP)` | 
`Basson.dev_period`   | `BASS_*Config*(BASS_CONFIG_DEV_PERIOD)` | 
`Basson.floatdsp`     | `BASS_*Config*(BASS_CONFIG_FLOATDSP)` | 
`Basson.gvol_music`   | `BASS_*Config*(BASS_CONFIG_GVOL_MUSIC)` | 
`Basson.gvol_sample`  | `BASS_*Config*(BASS_CONFIG_GVOL_SAMPLE)` |
`Basson.gvol_stream`  | `BASS_*Config*(BASS_CONFIG_GVOL_STREAM)` | 
`Basson.ios_session`  | `BASS_*Config*(BASS_CONFIG_IOS_SESSION)` | 
`Basson.libssl`       | `BASS_*Config*(BASS_CONFIG_LIBSSL)` | 
`Basson.mf_disable`   | `BASS_*Config*(BASS_CONFIG_MF_DISABLE)` | 
`Basson.mf_video`     | `BASS_*Config*(BASS_CONFIG_MF_VIDEO)` | 
`Basson.music_virtual` | `BASS_*Config*(BASS_CONFIG_MUSIC_VIRTUAL)` | 
`Basson.net_agent`    | `BASS_*Config*(BASS_CONFIG_NET_AGENT)` | 
`Basson.net_buffer`   | `BASS_*Config*(BASS_CONFIG_NET_BUFFER)` | 
`Basson.net_meta`     | `BASS_*Config*(BASS_CONFIG_NET_META)` | 
`Basson.net_passive`  | `BASS_*Config*(BASS_CONFIG_NET_PASSIVE)` | 
`Basson.net_playlist` | `BASS_*Config*(BASS_CONFIG_NET_PLAYLIST)` |
`Basson.net_playlist_depth` | `BASS_*Config*(BASS_CONFIG_NET_PLAYLIST_DEPTH)` | 
`Basson.net_prebuf`   | `BASS_*Config*(BASS_CONFIG_NET_PREBUF)` | 
`Basson.net_proxy`    | `BASS_*Config*(BASS_CONFIG_NET_PROXY)` | 
`Basson.net_readtimeout` | `BASS_*Config*(BASS_CONFIG_NET_READTIMEOUT)` | 
`Basson.net_restrate` | `BASS_*Config*(BASS_CONFIG_NET_RESTRATE)` | 
`Basson.net_timeout`  | `BASS_*Config*(BASS_CONFIG_NET_TIMEOUT)` | 
`Basson.noramp`       | `BASS_*Config*(BASS_CONFIG_NORAMP)` | 
`Basson.ogg_prescan`  | `BASS_*Config*(BASS_CONFIG_OGG_PRESCAN)` | 
`Basson.pause_noplay` | `BASS_*Config*(BASS_CONFIG_PAUSE_NOPLAY)` | 
`Basson.rec_buffer`   | `BASS_*Config*(BASS_CONFIG_REC_BUFFER)` | 
`Basson.rec_wasapi`   | `BASS_*Config*(BASS_CONFIG_REC_WASAPI)` | 
`Basson.sample_onehandle` | `BASS_*Config*(BASS_CONFIG_SAMPLE_ONEHANDLE)`| 
`Basson.src`          | `BASS_*Config*(BASS_CONFIG_SRC)`| 
`Basson.src_sample`   | `BASS_*Config*(BASS_CONFIG_SRC_SAMPLE)`| 
`Basson.unicode`      | `BASS_*Config*(BASS_CONFIG_UNICODE)` | 
`Basson.updateperiod` | `BASS_*Config*(BASS_CONFIG_UPDATEPERIOD)` | 
`Basson.updatethreads` | `BASS_*Config*(BASS_CONFIG_UPDATETHREADS)` | 
`Basson.verify`       | `BASS_*Config*(BASS_CONFIG_VERIFY)` | 
`Basson.verify_net`   | `BASS_*Config*(BASS_CONFIG_VERIFY_NET)` | 
`Basson.wasapi_persist` | `BASS_*Config*(BASS_CONFIG_WASAPI_PERSIST)` | 

### class Channel

Basson | BASS | Comment
--- | --- | ---
`Basson.Channel.WHOAMI` | - | Contain `Basson.ChannelType` flag
`Basson.Channel.HANDLE` | - | Contain BASS handle of channel
`Basson.Channel.bytes2seconds()` | `BASS_ChannelBytes2Seconds()` |
`Basson.Channel.seconds2bytes()` | `BASS_ChannelSeconds2Bytes()` |
NIE | `BASS_ChannelGet3DAttributes()` |
NIE | `BASS_ChannelGet3DPosition()` |
NIE | `BASS_ChannelGetData()` |
`Basson.Channel.deivce` | `BASS_ChannelGetDevice()`, `BASS_ChannelSetDevice()` |
`Basson.Channel.length`, `Basson.Channel.length_get()` | `BASS_ChannelGetLength()` | Renamed for ease of understanding. Have simple property as assign for main function
NIE | `BASS_ChannelLevel()` |
`Basson.Channel.position`, `Basson.Channel.position_get()`, `Basson.Channel.position_set()` | `BASS_ChannelGetPosition()`, `BASS_ChannelSetPosition()`| Renamed for ease of understanding. Have simple property as assign for main function
`Basson.Channel.status` | `BASS_ChannelIsActive()` | Renamed for ease of understanding
NIE | `BASS_ChannelIsSliding()` |
NIE | `BASS_ChannelSlideAttribute()` |
`Basson.Channel.lock()` | `BASS_ChannelLock()` |
`Basson.Channel.play()` | `BASS_ChannelPlay()` | Can be called without `.start()`
`Basson.Channel.pause()` | `BASS_ChannelPause()` |
`Basson.Channel.stop()` | `BASS_ChannelStop()` |
`Basson.Channel.start()` | `BASS_ChannelStart()` |
NIE | `BASS_ChannelSetDSP()`, `BASS_ChannelRemoveDSP()` |
NIE | `BASS_ChannelSetDSP()`, `BASS_ChannelRemoveFX()` |
NIE | `BASS_ChannelSetDSP()`, `BASS_ChannelRemoveLink()` |
NIE | `BASS_ChannelSetDSP()`, `BASS_ChannelRemoveSync()` |
