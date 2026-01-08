
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

### class Channel _(and all classes inheriting it)_

Basson | BASS | Comment
--- | --- | ---|
`Basson.Channel.WHOAMI` | - | Contain `Basson.ChannelType` flag
`Basson.Channel.HANDLE` | - | Contain BASS handle of channel
`Basson.Channel.bytes2seconds()` | `BASS_ChannelBytes2Seconds()` |
`Basson.Channel.seconds2bytes()` | `BASS_ChannelSeconds2Bytes()` |
NIE                     | `BASS_ChannelGet3DAttributes()` |
NIE                     | `BASS_ChannelGet3DPosition()` |
NIE                     | `BASS_ChannelGetData()` |
`Basson.Channel.deivce` | `BASS_ChannelGetDevice()`, `BASS_ChannelSetDevice()` |
`Basson.Channel.length`, `Basson.Channel.length_get()` | `BASS_ChannelGetLength()` | Renamed for ease of understanding. Have simple property as assign for main function
NIE                     | `BASS_ChannelLevel()` |
`Basson.Channel.position`, `Basson.Channel.position_get()`, `Basson.Channel.position_set()` | `BASS_ChannelGetPosition()`, `BASS_ChannelSetPosition()`| Renamed for ease of understanding. Have simple property as assign for main function
`Basson.Channel.status` | `BASS_ChannelIsActive()` | Renamed for ease of understanding
NIE                     | `BASS_ChannelIsSliding()` |
NIE                     | `BASS_ChannelSlideAttribute()` |
`Basson.Channel.lock()` | `BASS_ChannelLock()` |
`Basson.Channel.play()` | `BASS_ChannelPlay()` | Can be called without `.start()`
`Basson.Channel.pause()` | `BASS_ChannelPause()` |
`Basson.Channel.stop()` | `BASS_ChannelStop()` |
`Basson.Channel.start()` | `BASS_ChannelStart()` |
NIE                     | `BASS_ChannelSetDSP()`, `BASS_ChannelRemoveDSP()` |
NIE                     | `BASS_ChannelSetDSP()`, `BASS_ChannelRemoveFX()` |
NIE                     | `BASS_ChannelSetDSP()`, `BASS_ChannelRemoveLink()` |
NIE                     | `BASS_ChannelSetDSP()`, `BASS_ChannelRemoveSync()` |
\-                      | `BASS_ChannelGetAttribute()`, `BASS_ChannelSetAttribute()`, `BASS_ChannelGetAttributeEx()`, `BASS_ChannelSetAttributeEx()`, `BASS_ChannelFlags()` | All configs implemented in main class as properties
`Basson.Channel.bitrate` | `BASS_ChannelGetAtrribute(BASS_ATTRIB_BITRATE)` | 
`Basson.Channel.buffer` | `BASS_Channel*etAtrribute(BASS_ATTRIB_BITRATE)` |
`Basson.Channel.cpu_usage` | `BASS_ChannelGetAtrribute(BASS_ATTRIB_CPU)` |
`Basson.Channel.frequency` | `BASS_Channel*etAtrribute(BASS_ATTRIB_FREQ)` |
`Basson.Channel.granule` | `BASS_Channel*etAtrribute(BASS_ATTRIB_GRANULE)` |
`Basson.Channel.music_active` | `BASS_ChannelGetAtrribute(BASS_ATTRIB_MUSIC_ACTTIVE)` |
`Basson.Channel.music_amplify` | `BASS_Channel*etAtrribute(BASS_ATTRIB_MUSIC_AMPLIFY)` |
`Basson.Channel.music_bpm` | `BASS_Channel*etAtrribute(BASS_ATTRIB_MUSIC_BPM)` |
`Basson.Channel.music_pansep` | `BASS_Channel*etAtrribute(BASS_ATTRIB_MUSIC_PANSEP)` |
`Basson.Channel.music_position_scaler` | `BASS_Channel*etAtrribute(BASS_ATTRIB_MUSIC_PSCALER)` |
`Basson.Channel.music_speed` | `BASS_Channel*etAtrribute(BASS_ATTRIB_MUSIC_SPEED)` |
`Basson.Channel.music_volume` | `BASS_Channel*etAtrribute(BASS_ATTRIB_MUSIC_VOLUME)` |
`Basson.Channel.music_volume_instrument` | `BASS_Channel*etAtrribute(BASS_ATTRIB_MUSIC_VOL_INST)` |
`Basson.Channel.net_resume` | `BASS_Channel*etAtrribute(BASS_ATTRIB_NET_RESUME)` |
`Basson.Channel.noramp` | `BASS_Channel*etAtrribute(BASS_ATTRIB_NORAMP)` |
`Basson.Channel.pan`    | `BASS_Channel*etAtrribute(BASS_ATTRIB_PAN)` |
`Basson.Channel.push_limit` | `BASS_Channel*etAtrribute(BASS_ATTRIB_PUSH_LIMIT)` |
`Basson.Channel.src`    | `BASS_Channel*etAtrribute(BASS_ATTRIB_SRC)` |
`Basson.Channel.tail`   | `BASS_Channel*etAtrribute(BASS_ATTRIB_TAIL)` |
`Basson.Channel.volume` | `BASS_Channel*etAtrribute(BASS_ATTRIB_VOL)` |
`Basson.Channel.dsp_volume` | `BASS_Channel*etAtrribute(BASS_ATTRIB_VOLDSP)` |
`Basson.Channel.dsp_volume_priority` | `BASS_Channel*etAtrribute(BASS_ATTRIB_VOLDSP_PRIORITY)` |
`Basson.Channel.loop`   | `BASS_ChannelFlags(BASS_SAMPLE_LOOP)` |
`Basson.Channel.mutemax` | `BASS_ChannelFlags(BASS_SAMPLE_MUTEMAX)` |
NIE                     | `BASS_ChannelFlags(BASS_STREAM_AUTOFREE)` |
`Basson.Channel.restrict_rate` | `BASS_ChannelFlags(BASS_STREAM_RESTRATE)` |
`Basson.Channel.noninter` | `BASS_ChannelFlags(BASS_MUSIC_NONINTER)` |
`Basson.Channel.sinter` | `BASS_ChannelFlags(BASS_MUSIC_SINTER)` |
`Basson.Channel.ramp`   | `BASS_ChannelFlags(BASS_MUSIC_RAMP)` |
`Basson.Channel.noninter` | `BASS_ChannelFlags(BASS_MUSIC_NONINTER)` |
`Basson.Channel.surround` | `BASS_ChannelFlags(BASS_MUSIC_SURROUND)`, `BASS_ChannelFlags(BASS_MUSIC_SURROUND2)` |
`Basson.Channel.ft2mod` | `BASS_ChannelFlags(BASS_MUSIC_FT2MOD)` |
`Basson.Channel.pt1mod` | `BASS_ChannelFlags(BASS_MUSIC_PT1MOD)` |
`Basson.Channel.posreset` | `BASS_ChannelFlags(BASS_MUSIC_POSRESET)` |
`Basson.Channel.posresetex` | `BASS_ChannelFlags(BASS_MUSIC_POSRESETEX)` |
`Basson.Channel.stopback` | `BASS_ChannelFlags(BASS_MUSIC_STOPBACK)` |
NIE                      | `BASS_ChannelFlags(BASS_SPEAKER_xxx)` |
