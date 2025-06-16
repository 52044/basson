# Converted BASS.h to Python

import ctypes
import typing

def LOBYTE(a):
    return (a) & 0xff

def HIBYTE(a):
    return (a >> 8) & 0xff

def LOWORD(a):
    return (a) & 0xffff

def HIWORD(a):
    return (a >> 16) & 0xffff

def MAKEWORD(a,b):
    return (((a)&0xff)|((b)<<8))

def MAKELONG(a,b):
    return (((a)&0xffff)|((b)<<16))

def BASS_SPEAKER_N(n): # n'th pair of speakers (max 15)
    return (n << 24)

#region C data types
INT =   ctypes.c_int        
BYTE =  ctypes.c_ubyte
WORD =  ctypes.c_ushort
DWORD = ctypes.c_ulong
QWORD = ctypes.c_uint64
FLOAT = ctypes.c_float
DOUBLE = ctypes.c_double
CHAR =  ctypes.c_char
PTR = ctypes.c_void_p # Pointer to something
CHARP = ctypes.c_char_p

BOOL = ctypes.c_int # BASS using integers as bollean
TRUE = 1 ;''' True value in bass'''    
FALSE = 0
MINUSONE = 0xFFFFFFFF

# Pointers types (handles) BASS
#   There are different handle names for separating the destination. 
#   A universal handle is also provided. 
#   Basically it's all the same thing.
HANDLE =    DWORD
HMUSIC =    DWORD
HSAMPLE =   DWORD
HCHANNEL =  DWORD
HSTREAM =   DWORD
HRECORD =   DWORD
HSYNC =     DWORD
HDSP =      DWORD
HFX =       DWORD
HPLUGIN =   DWORD
#endregion

#region Constants

BASSAPI = 0x204

# Error codes returned by BASS_ErrorGetCode
BASS_OK                     = 0 # all is OK
BASS_ERROR_MEM              = 1 # memory error
BASS_ERROR_FILEOPEN         = 2 # can't open the file
BASS_ERROR_DRIVER           = 3 # can't find a free/valid driver
BASS_ERROR_BUFLOST          = 4 # the sample buffer was lost
BASS_ERROR_HANDLE           = 5 # invalid handle
BASS_ERROR_FORMAT           = 6 # unsupported sample format
BASS_ERROR_POSITION         = 7 # invalid position
BASS_ERROR_INIT             = 8 # BASS_Init has not been successfully called
BASS_ERROR_START            = 9 # BASS_Start has not been successfully called
BASS_ERROR_SSL              = 10 # SSL/HTTPS support isn't available
BASS_ERROR_REINIT           = 11 # device needs to be reinitialized
BASS_ERROR_ALREADY          = 14 # already initialized/paused/whatever
BASS_ERROR_NOTAUDIO         = 17 # file does not contain audio
BASS_ERROR_NOCHAN           = 18 # can't get a free channel
BASS_ERROR_ILLTYPE          = 19 # an illegal type was specified
BASS_ERROR_ILLPARAM         = 20 # an illegal parameter was specified
BASS_ERROR_NO3D             = 21 # no 3D support
BASS_ERROR_NOEAX            = 22 # no EAX support
BASS_ERROR_DEVICE           = 23 # illegal device number
BASS_ERROR_NOPLAY           = 24 # not playing
BASS_ERROR_FREQ             = 25 # illegal sample rate
BASS_ERROR_NOTFILE          = 27 # the stream is not a file stream
BASS_ERROR_NOHW             = 29 # no hardware voices available
BASS_ERROR_EMPTY            = 31 # the file has no sample data
BASS_ERROR_NONET            = 32 # no internet connection could be opened
BASS_ERROR_CREATE           = 33 # couldn't create the file
BASS_ERROR_NOFX             = 34 # effects are not available
BASS_ERROR_NOTAVAIL         = 37 # requested data/action is not available
BASS_ERROR_DECODE           = 38 # the channel is/isn't a "decoding channel"
BASS_ERROR_DX               = 39 # a sufficient DirectX version is not installed
BASS_ERROR_TIMEOUT          = 40 # connection timedout
BASS_ERROR_FILEFORM         = 41 # unsupported file format
BASS_ERROR_SPEAKER          = 42 # unavailable speaker
BASS_ERROR_VERSION          = 43 # invalid BASS version (used by add-ons)
BASS_ERROR_CODEC            = 44 # codec is not available/supported
BASS_ERROR_ENDED            = 45 # the channel/file has ended
BASS_ERROR_BUSY             = 46 # the device is busy
BASS_ERROR_UNSTREAMABLE     = 47 # unstreamable file
BASS_ERROR_PROTOCOL         = 48 # unsupported protocol
BASS_ERROR_DENIED           = 49 # access denied
BASS_ERROR_UNKNOWN          = -1 # some other mystery problem

# BASS_SetConfig options
BASS_CONFIG_BUFFER          = 0
BASS_CONFIG_UPDATEPERIOD    = 1
BASS_CONFIG_GVOL_SAMPLE     = 4
BASS_CONFIG_GVOL_STREAM     = 5
BASS_CONFIG_GVOL_MUSIC      = 6
BASS_CONFIG_CURVE_VOL       = 7
BASS_CONFIG_CURVE_PAN       = 8
BASS_CONFIG_FLOATDSP        = 9
BASS_CONFIG_3DALGORITHM     = 10
BASS_CONFIG_NET_TIMEOUT     = 11
BASS_CONFIG_NET_BUFFER      = 12
BASS_CONFIG_PAUSE_NOPLAY    = 13
BASS_CONFIG_NET_PREBUF      = 15
BASS_CONFIG_NET_PASSIVE     = 18
BASS_CONFIG_REC_BUFFER      = 19
BASS_CONFIG_NET_PLAYLIST    = 21
BASS_CONFIG_MUSIC_VIRTUAL   = 22
BASS_CONFIG_VERIFY          = 23
BASS_CONFIG_UPDATETHREADS   = 24
BASS_CONFIG_DEV_BUFFER      = 27
BASS_CONFIG_REC_LOOPBACK    = 28
BASS_CONFIG_VISTA_TRUEPOS   = 30
BASS_CONFIG_IOS_SESSION     = 34
BASS_CONFIG_IOS_MIXAUDIO    = 34 # Alias for BASS_CONFIG_IOS_SESSION
BASS_CONFIG_DEV_DEFAULT     = 36
BASS_CONFIG_NET_READTIMEOUT = 37
BASS_CONFIG_VISTA_SPEAKERS  = 38
BASS_CONFIG_IOS_SPEAKER     = 39
BASS_CONFIG_MF_DISABLE      = 40
BASS_CONFIG_HANDLES         = 41
BASS_CONFIG_UNICODE         = 42
BASS_CONFIG_SRC             = 43
BASS_CONFIG_SRC_SAMPLE      = 44
BASS_CONFIG_ASYNCFILE_BUFFER = 45
BASS_CONFIG_OGG_PRESCAN     = 47
BASS_CONFIG_MF_VIDEO        = 48
BASS_CONFIG_AIRPLAY         = 49
BASS_CONFIG_DEV_NONSTOP     = 50
BASS_CONFIG_IOS_NOCATEGORY  = 51
BASS_CONFIG_VERIFY_NET      = 52
BASS_CONFIG_DEV_PERIOD      = 53
BASS_CONFIG_FLOAT           = 54
BASS_CONFIG_NET_SEEK        = 56
BASS_CONFIG_AM_DISABLE      = 58
BASS_CONFIG_NET_PLAYLIST_DEPTH = 59
BASS_CONFIG_NET_PREBUF_WAIT = 60
BASS_CONFIG_ANDROID_SESSIONID = 62
BASS_CONFIG_WASAPI_PERSIST  = 65
BASS_CONFIG_REC_WASAPI      = 66
BASS_CONFIG_ANDROID_AAUDIO  = 67
BASS_CONFIG_SAMPLE_ONEHANDLE = 69
BASS_CONFIG_NET_META        = 71
BASS_CONFIG_NET_RESTRATE    = 72
BASS_CONFIG_REC_DEFAULT     = 73
BASS_CONFIG_NORAMP          = 74

# BASS_SetConfigPtr options
BASS_CONFIG_NET_AGENT       = 16
BASS_CONFIG_NET_PROXY       = 17
BASS_CONFIG_IOS_NOTIFY      = 46
BASS_CONFIG_ANDROID_JAVAVM  = 63
BASS_CONFIG_LIBSSL          = 64
BASS_CONFIG_FILENAME        = 75

BASS_CONFIG_THREAD          = 0x40000000 # flag: thread-specific setting

# BASS_CONFIG_IOS_SESSION flags
BASS_IOS_SESSION_MIX        = 1
BASS_IOS_SESSION_DUCK       = 2
BASS_IOS_SESSION_AMBIENT    = 4
BASS_IOS_SESSION_SPEAKER    = 8
BASS_IOS_SESSION_DISABLE    = 16
BASS_IOS_SESSION_DEACTIVATE = 32
BASS_IOS_SESSION_AIRPLAY    = 64
BASS_IOS_SESSION_BTHFP      = 128
BASS_IOS_SESSION_BTA2DP     = 0x100

# BASS_Init flags
BASS_DEVICE_8BITS           = 1 # unused
BASS_DEVICE_MONO            = 2 # mono
BASS_DEVICE_3D              = 4 # unused
BASS_DEVICE_16BITS          = 8 # limit output to 16-bit
BASS_DEVICE_REINIT          = 128 # reinitialize
BASS_DEVICE_LATENCY         = 0x100 # unused
BASS_DEVICE_CPSPEAKERS      = 0x400 # unused
BASS_DEVICE_SPEAKERS        = 0x800 # force enabling of speaker assignment
BASS_DEVICE_NOSPEAKER       = 0x1000 # ignore speaker arrangement
BASS_DEVICE_DMIX            = 0x2000 # use ALSA "dmix" plugin
BASS_DEVICE_FREQ            = 0x4000 # set device sample rate
BASS_DEVICE_STEREO          = 0x8000 # limit output to stereo
BASS_DEVICE_HOG             = 0x10000 # hog/exclusive mode
BASS_DEVICE_AUDIOTRACK      = 0x20000 # use AudioTrack output
BASS_DEVICE_DSOUND          = 0x40000 # use DirectSound output
BASS_DEVICE_SOFTWARE        = 0x80000 # disable hardware/fastpath output

# DirectSound interfaces (for use with BASS_GetDSoundObject)
BASS_OBJECT_DS              = 1 # IDirectSound
BASS_OBJECT_DS3DL           = 2 # IDirectSound3DListener

# BASS_DEVICEINFO flags
BASS_DEVICE_ENABLED         = 1
BASS_DEVICE_DEFAULT         = 2
BASS_DEVICE_INIT            = 4
BASS_DEVICE_LOOPBACK        = 8
BASS_DEVICE_DEFAULTCOM      = 128

BASS_DEVICE_TYPE_MASK       = 0xff000000
BASS_DEVICE_TYPE_NETWORK    = 0x01000000
BASS_DEVICE_TYPE_SPEAKERS   = 0x02000000
BASS_DEVICE_TYPE_LINE       = 0x03000000
BASS_DEVICE_TYPE_HEADPHONES = 0x04000000
BASS_DEVICE_TYPE_MICROPHONE = 0x05000000
BASS_DEVICE_TYPE_HEADSET    = 0x06000000
BASS_DEVICE_TYPE_HANDSET    = 0x07000000
BASS_DEVICE_TYPE_DIGITAL    = 0x08000000
BASS_DEVICE_TYPE_SPDIF      = 0x09000000
BASS_DEVICE_TYPE_HDMI       = 0x0a000000
BASS_DEVICE_TYPE_DISPLAYPORT = 0x40000000

# BASS_GetDeviceInfo flags
BASS_DEVICES_AIRPLAY        = 0x1000000

# BASS_INFO flags (from DSOUND.H)
DSCAPS_EMULDRIVER           = 0x00000020 # device does not have hardware DirectSound support
DSCAPS_CERTIFIED            = 0x00000040 # device driver has been certified by Microsoft
DSCAPS_HARDWARE             = 0x80000000 # hardware mixed

# BASS_RECORDINFO flags (from DSOUND.H)
DSCCAPS_EMULDRIVER          = DSCAPS_EMULDRIVER # device does not have hardware DirectSound recording support
DSCCAPS_CERTIFIED           = DSCAPS_CERTIFIED # device driver has been certified by Microsoft

# defines for formats field of BASS_RECORDINFO (from MMSYSTEM.H)
WAVE_FORMAT_1M08            = 0x00000001 # 11.025 kHz, Mono,   8-bit
WAVE_FORMAT_1S08            = 0x00000002 # 11.025 kHz, Stereo, 8-bit
WAVE_FORMAT_1M16            = 0x00000004 # 11.025 kHz, Mono,   16-bit
WAVE_FORMAT_1S16            = 0x00000008 # 11.025 kHz, Stereo, 16-bit
WAVE_FORMAT_2M08            = 0x00000010 # 22.05  kHz, Mono,   8-bit
WAVE_FORMAT_2S08            = 0x00000020 # 22.05  kHz, Stereo, 8-bit
WAVE_FORMAT_2M16            = 0x00000040 # 22.05  kHz, Mono,   16-bit
WAVE_FORMAT_2S16            = 0x00000080 # 22.05  kHz, Stereo, 16-bit
WAVE_FORMAT_4M08            = 0x00000100 # 44.1   kHz, Mono,   8-bit
WAVE_FORMAT_4S08            = 0x00000200 # 44.1   kHz, Stereo, 8-bit
WAVE_FORMAT_4M16            = 0x00000400 # 44.1   kHz, Mono,   16-bit
WAVE_FORMAT_4S16            = 0x00000800 # 44.1   kHz, Stereo, 16-bit

# BASS_SAMPLE flags
BASS_SAMPLE_8BITS           = 1 # 8 bit
BASS_SAMPLE_FLOAT           = 256 # 32 bit floating-point
BASS_SAMPLE_MONO            = 2 # mono
BASS_SAMPLE_LOOP            = 4 # looped
BASS_SAMPLE_3D              = 8 # 3D functionality
BASS_SAMPLE_SOFTWARE        = 16 # unused
BASS_SAMPLE_MUTEMAX         = 32 # mute at max distance (3D only)
BASS_SAMPLE_VAM             = 64 # unused
BASS_SAMPLE_FX              = 128 # unused
BASS_SAMPLE_OVER_VOL        = 0x10000 # override lowest volume
BASS_SAMPLE_OVER_POS        = 0x20000 # override longest playing
BASS_SAMPLE_OVER_DIST       = 0x30000 # override furthest from listener (3D only)

BASS_STREAM_PRESCAN         = 0x20000 # scan file for accurate seeking and length
BASS_STREAM_AUTOFREE        = 0x40000 # automatically free the stream when it stops/ends
BASS_STREAM_RESTRATE        = 0x80000 # restrict the download rate of internet file stream
BASS_STREAM_BLOCK           = 0x100000 # download internet file stream in small blocks
BASS_STREAM_DECODE          = 0x200000 # don't play the stream, only decode
BASS_STREAM_STATUS          = 0x800000 # give server status info (HTTP/ICY tags) in DOWNLOADPROC

BASS_MP3_IGNOREDELAY        = 0x200 # ignore LAME/Xing/VBRI/iTunes delay & padding info
BASS_MP3_SETPOS             = BASS_STREAM_PRESCAN

BASS_MUSIC_FLOAT            = BASS_SAMPLE_FLOAT
BASS_MUSIC_MONO             = BASS_SAMPLE_MONO
BASS_MUSIC_LOOP             = BASS_SAMPLE_LOOP
BASS_MUSIC_3D               = BASS_SAMPLE_3D
BASS_MUSIC_FX               = BASS_SAMPLE_FX
BASS_MUSIC_AUTOFREE         = BASS_STREAM_AUTOFREE
BASS_MUSIC_DECODE           = BASS_STREAM_DECODE
BASS_MUSIC_PRESCAN          = BASS_STREAM_PRESCAN # calculate playback length
BASS_MUSIC_CALCLEN          = BASS_MUSIC_PRESCAN
BASS_MUSIC_RAMP             = 0x200 # normal ramping
BASS_MUSIC_RAMPS            = 0x400 # sensitive ramping
BASS_MUSIC_SURROUND         = 0x800 # surround sound
BASS_MUSIC_SURROUND2        = 0x1000 # surround sound (mode 2)
BASS_MUSIC_FT2PAN           = 0x2000 # apply FastTracker 2 panning to XM files
BASS_MUSIC_FT2MOD           = 0x2000 # play .MOD as FastTracker 2 does
BASS_MUSIC_PT1MOD           = 0x4000 # play .MOD as ProTracker 1 does
BASS_MUSIC_NONINTER         = 0x10000 # non-interpolated sample mixing
BASS_MUSIC_SINCINTER        = 0x800000 # sinc interpolated sample mixing
BASS_MUSIC_POSRESET         = 0x8000 # stop all notes when moving position
BASS_MUSIC_POSRESETEX       = 0x400000 # stop all notes and reset bmp/etc when moving position
BASS_MUSIC_STOPBACK         = 0x80000 # stop the music on a backwards jump effect
BASS_MUSIC_NOSAMPLE         = 0x100000 # don't load the samples

# Speaker assignment flags
BASS_SPEAKER_FRONT          = 0x1000000 # front speakers
BASS_SPEAKER_REAR           = 0x2000000 # rear speakers
BASS_SPEAKER_CENLFE         = 0x3000000 # center & LFE speakers (5.1)
BASS_SPEAKER_SIDE           = 0x4000000 # side speakers (7.1)

BASS_SPEAKER_LEFT           = 0x10000000 # modifier: left
BASS_SPEAKER_RIGHT          = 0x20000000 # modifier: right
BASS_SPEAKER_FRONTLEFT      = BASS_SPEAKER_FRONT | BASS_SPEAKER_LEFT
BASS_SPEAKER_FRONTRIGHT     = BASS_SPEAKER_FRONT | BASS_SPEAKER_RIGHT
BASS_SPEAKER_REARLEFT       = BASS_SPEAKER_REAR | BASS_SPEAKER_LEFT
BASS_SPEAKER_REARRIGHT      = BASS_SPEAKER_REAR | BASS_SPEAKER_RIGHT
BASS_SPEAKER_CENTER         = BASS_SPEAKER_CENLFE | BASS_SPEAKER_LEFT
BASS_SPEAKER_LFE            = BASS_SPEAKER_CENLFE | BASS_SPEAKER_RIGHT
BASS_SPEAKER_SIDELEFT       = BASS_SPEAKER_SIDE | BASS_SPEAKER_LEFT
BASS_SPEAKER_SIDERIGHT      = BASS_SPEAKER_SIDE | BASS_SPEAKER_RIGHT
BASS_SPEAKER_REAR2          = BASS_SPEAKER_SIDE
BASS_SPEAKER_REAR2LEFT      = BASS_SPEAKER_SIDELEFT
BASS_SPEAKER_REAR2RIGHT     = BASS_SPEAKER_SIDERIGHT

BASS_ASYNCFILE              = 0x40000000 # read file asynchronously
BASS_UNICODE                = 0x80000000 # UTF-16

BASS_RECORD_ECHOCANCEL      = 0x2000
BASS_RECORD_AGC             = 0x4000
BASS_RECORD_PAUSE           = 0x8000 # start recording paused

# DX7 voice allocation & management flags
BASS_VAM_HARDWARE           = 1
BASS_VAM_SOFTWARE           = 2
BASS_VAM_TERM_TIME          = 4
BASS_VAM_TERM_DIST          = 8
BASS_VAM_TERM_PRIO          = 16

# BASS_CHANNELINFO flags
BASS_ORIGRES_FLOAT          = 0x10000

# BASS_CHANNELINFO types
BASS_CTYPE_SAMPLE           = 1
BASS_CTYPE_RECORD           = 2
BASS_CTYPE_STREAM           = 0x10000
BASS_CTYPE_STREAM_VORBIS    = 0x10002
BASS_CTYPE_STREAM_OGG       = 0x10002
BASS_CTYPE_STREAM_MP1       = 0x10003
BASS_CTYPE_STREAM_MP2       = 0x10004
BASS_CTYPE_STREAM_MP3       = 0x10005
BASS_CTYPE_STREAM_AIFF      = 0x10006
BASS_CTYPE_STREAM_CA        = 0x10007
BASS_CTYPE_STREAM_MF        = 0x10008
BASS_CTYPE_STREAM_AM        = 0x10009
BASS_CTYPE_STREAM_SAMPLE    = 0x1000a
BASS_CTYPE_STREAM_DUMMY     = 0x18000
BASS_CTYPE_STREAM_DEVICE    = 0x18001
BASS_CTYPE_STREAM_WAV       = 0x40000 # WAVE flag (LOWORD=codec)
BASS_CTYPE_STREAM_WAV_PCM   = 0x50001
BASS_CTYPE_STREAM_WAV_FLOAT = 0x50003
BASS_CTYPE_MUSIC_MOD        = 0x20000
BASS_CTYPE_MUSIC_MTM        = 0x20001
BASS_CTYPE_MUSIC_S3M        = 0x20002
BASS_CTYPE_MUSIC_XM         = 0x20003
BASS_CTYPE_MUSIC_IT         = 0x20004
BASS_CTYPE_MUSIC_MO3        = 0x00100 # MO3 flag

# BASS_PluginLoad flags
BASS_PLUGIN_PROC            = 1

# 3D channel modes
BASS_3DMODE_NORMAL          = 0 # normal 3D processing
BASS_3DMODE_RELATIVE        = 1 # position is relative to the listener
BASS_3DMODE_OFF             = 2 # no 3D processing

# software 3D mixing algorithms (used with BASS_CONFIG_3DALGORITHM)
BASS_3DALG_DEFAULT          = 0
BASS_3DALG_OFF              = 1
BASS_3DALG_FULL             = 2
BASS_3DALG_LIGHT            = 3

# BASS_SampleGetChannel flags
BASS_SAMCHAN_NEW            = 1 # get a new playback channel
BASS_SAMCHAN_STREAM         = 2 # create a stream

BASS_STREAMPROC_END         = 0x80000000 # end of user stream flag

# Special STREAMPROCs
STREAMPROC_DUMMY            = 0 # "dummy" stream
STREAMPROC_PUSH             = -1 # push stream
STREAMPROC_DEVICE           = -2 # device mix stream
STREAMPROC_DEVICE_3D        = -3 # device 3D mix stream

# BASS_StreamCreateFileUser file systems
STREAMFILE_NOBUFFER         = 0
STREAMFILE_BUFFER           = 1
STREAMFILE_BUFFERPUSH       = 2

# BASS_StreamPutFileData options
BASS_FILEDATA_END           = 0 # end & close the file

# BASS_StreamGetFilePosition modes
BASS_FILEPOS_CURRENT        = 0
BASS_FILEPOS_DECODE         = BASS_FILEPOS_CURRENT
BASS_FILEPOS_DOWNLOAD       = 1
BASS_FILEPOS_END            = 2
BASS_FILEPOS_START          = 3
BASS_FILEPOS_CONNECTED      = 4
BASS_FILEPOS_BUFFER         = 5
BASS_FILEPOS_SOCKET         = 6
BASS_FILEPOS_ASYNCBUF       = 7
BASS_FILEPOS_SIZE           = 8
BASS_FILEPOS_BUFFERING      = 9
BASS_FILEPOS_AVAILABLE      = 10

# BASS_ChannelSetSync types
BASS_SYNC_POS               = 0
BASS_SYNC_END               = 2
BASS_SYNC_META              = 4
BASS_SYNC_SLIDE             = 5
BASS_SYNC_STALL             = 6
BASS_SYNC_DOWNLOAD          = 7
BASS_SYNC_FREE              = 8
BASS_SYNC_SETPOS            = 11
BASS_SYNC_MUSICPOS          = 10
BASS_SYNC_MUSICINST         = 1
BASS_SYNC_MUSICFX           = 3
BASS_SYNC_OGG_CHANGE        = 12
BASS_SYNC_DEV_FAIL          = 14
BASS_SYNC_DEV_FORMAT        = 15
BASS_SYNC_THREAD            = 0x20000000 # flag: call sync in other thread
BASS_SYNC_MIXTIME           = 0x40000000 # flag: sync at mixtime, else at playtime
BASS_SYNC_ONETIME           = 0x80000000 # flag: sync only once, else continuously

# BASS_ChannelIsActive return values
BASS_ACTIVE_STOPPED         = 0
BASS_ACTIVE_PLAYING         = 1
BASS_ACTIVE_STALLED         = 2
BASS_ACTIVE_PAUSED          = 3
BASS_ACTIVE_PAUSED_DEVICE   = 4

# Channel attributes
BASS_ATTRIB_FREQ            = 1
BASS_ATTRIB_VOL             = 2
BASS_ATTRIB_PAN             = 3
BASS_ATTRIB_EAXMIX          = 4
BASS_ATTRIB_NOBUFFER        = 5
BASS_ATTRIB_VBR             = 6 # unused
BASS_ATTRIB_CPU             = 7
BASS_ATTRIB_SRC             = 8
BASS_ATTRIB_NET_RESUME      = 9
BASS_ATTRIB_SCANINFO        = 10
BASS_ATTRIB_NORAMP          = 11
BASS_ATTRIB_BITRATE         = 12
BASS_ATTRIB_BUFFER          = 13
BASS_ATTRIB_GRANULE         = 14
BASS_ATTRIB_USER            = 15       # from BASS 2.4.16
BASS_ATTRIB_TAIL            = 16       # from BASS 2.4.16
BASS_ATTRIB_PUSH_LIMIT      = 17 # from BASS 2.4.16
BASS_ATTRIB_DOWNLOADPROC    = 18 # from BASS 2.4.17
BASS_ATTRIB_VOLDSP          = 19     # from BASS 2.4.17
BASS_ATTRIB_VOLDSP_PRIORITY = 20 # from BASS 2.4.17
BASS_ATTRIB_MUSIC_AMPLIFY   = 0x100
BASS_ATTRIB_MUSIC_PANSEP    = 0x101
BASS_ATTRIB_MUSIC_PSCALER   = 0x102
BASS_ATTRIB_MUSIC_BPM       = 0x103
BASS_ATTRIB_MUSIC_SPEED     = 0x104
BASS_ATTRIB_MUSIC_VOL_GLOBAL = 0x105
BASS_ATTRIB_MUSIC_ACTIVE    = 0x106
BASS_ATTRIB_MUSIC_VOL_CHAN  = 0x200 # + channel #
BASS_ATTRIB_MUSIC_VOL_INST  = 0x300 # + instrument #

# BASS_ChannelSlideAttribute flags
BASS_SLIDE_LOG              = 0x1000000

# BASS_ChannelGetData flags
BASS_DATA_AVAILABLE         = 0 # query how much data is buffered
BASS_DATA_NOREMOVE          = 0x10000000 # flag: don't remove data from recording buffer
BASS_DATA_FIXED             = 0x20000000 # unused
BASS_DATA_FLOAT             = 0x40000000 # flag: return floating-point sample data
BASS_DATA_FFT256            = 0x80000000 # 256 sample FFT
BASS_DATA_FFT512            = 0x80000001 # 512 FFT
BASS_DATA_FFT1024           = 0x80000002 # 1024 FFT
BASS_DATA_FFT2048           = 0x80000003 # 2048 FFT
BASS_DATA_FFT4096           = 0x80000004 # 4096 FFT
BASS_DATA_FFT8192           = 0x80000005 # 8192 FFT
BASS_DATA_FFT16384          = 0x80000006 # 16384 FFT
BASS_DATA_FFT32768          = 0x80000007 # 32768 FFT
BASS_DATA_FFT_INDIVIDUAL    = 0x10 # FFT flag: FFT for each channel, else all combined
BASS_DATA_FFT_NOWINDOW      = 0x20 # FFT flag: no Hanning window
BASS_DATA_FFT_REMOVEDC      = 0x40 # FFT flag: pre-remove DC bias
BASS_DATA_FFT_COMPLEX       = 0x80 # FFT flag: return complex data
BASS_DATA_FFT_NYQUIST       = 0x100 # FFT flag: return extra Nyquist value

# BASS_ChannelGetLevelEx flags
BASS_LEVEL_MONO = 1 # get mono level
BASS_LEVEL_STEREO = 2 # get stereo level
BASS_LEVEL_RMS = 4 # get RMS levels
BASS_LEVEL_VOLPAN = 8   # apply VOL/PAN attributes to the levels
BASS_LEVEL_NOREMOVE = 16 # don't remove data from recording buffer


# BASS_ChannelGetTags types : what's returned
BASS_TAG_ID3 = 0 # ID3v1 tags : TAG_ID3 structure
BASS_TAG_ID3V2 = 1 # ID3v2 tags : variable length block
BASS_TAG_OGG = 2 # OGG comments : series of null-terminated UTF-8 strings
BASS_TAG_HTTP = 3 # HTTP headers : series of null-terminated ASCII strings
BASS_TAG_ICY = 4 # ICY headers : series of null-terminated ANSI strings
BASS_TAG_META = 5 # ICY metadata : ANSI string
BASS_TAG_APE = 6 # APE tags : series of null-terminated UTF-8 strings
BASS_TAG_MP4 = 7 # MP4/iTunes metadata : series of null-terminated UTF-8 strings
BASS_TAG_WMA = 8 # WMA tags : series of null-terminated UTF-8 strings
BASS_TAG_VENDOR = 9 # OGG encoder : UTF-8 string
BASS_TAG_LYRICS3 = 10 # Lyric3v2 tag : ASCII string
BASS_TAG_CA_CODEC = 11 # CoreAudio codec info : TAG_CA_CODEC structure
BASS_TAG_MF = 13 # Media Foundation tags : series of null-terminated UTF-8 strings
BASS_TAG_WAVEFORMAT = 14 # WAVE format : WAVEFORMATEEX structure
BASS_TAG_AM_NAME = 16 # Android Media codec name : ASCII string
BASS_TAG_ID3V2_2 = 17 # ID3v2 tags (2nd block) : variable length block
BASS_TAG_AM_MIME = 18 # Android Media MIME type : ASCII string
BASS_TAG_LOCATION = 19 # redirected URL : ASCII string
BASS_TAG_RIFF_INFO = 0x100 # RIFF "INFO" tags : series of null-terminated ANSI strings
BASS_TAG_RIFF_BEXT = 0x101 # RIFF/BWF "bext" tags : TAG_BEXT structure
BASS_TAG_RIFF_CART = 0x102 # RIFF/BWF "cart" tags : TAG_CART structure
BASS_TAG_RIFF_DISP = 0x103 # RIFF "DISP" text tag : ANSI string
BASS_TAG_RIFF_CUE = 0x104 # RIFF "cue " chunk : TAG_CUE structure
BASS_TAG_RIFF_SMPL = 0x105 # RIFF "smpl" chunk : TAG_SMPL structure
BASS_TAG_APE_BINARY = 0x1000 # + index #, binary APE tag : TAG_APE_BINARY structure
BASS_TAG_MUSIC_NAME = 0x10000 # MOD music name : ANSI string
BASS_TAG_MUSIC_MESSAGE = 0x10001 # MOD message : ANSI string
BASS_TAG_MUSIC_ORDERS = 0x10002 # MOD order list : BYTE array of pattern numbers
BASS_TAG_MUSIC_AUTH = 0x10003 # MOD author : UTF-8 string
BASS_TAG_MUSIC_INST = 0x10100 # + instrument #, MOD instrument name : ANSI string
BASS_TAG_MUSIC_CHAN = 0x10200 # + channel #, MOD channel name : ANSI string
BASS_TAG_MUSIC_SAMPLE = 0x10300 # + sample #, MOD sample name : ANSI string

# BASS_ChannelGetLength/GetPosition/SetPosition modes
BASS_POS_BYTE = 0 # byte position
BASS_POS_MUSIC_ORDER = 1 # order.row position, MAKELONG(order,row)
BASS_POS_OGG = 3 # OGG bitstream number
BASS_POS_END = 0x10 # trimmed end position
BASS_POS_LOOP = 0x11 # loop start positiom
BASS_POS_FLUSH = 0x1000000 # flag: flush decoder/FX buffers
BASS_POS_RESET = 0x2000000 # flag: reset user file buffers
BASS_POS_RELATIVE = 0x4000000 # flag: seek relative to the current position
BASS_POS_INEXACT = 0x8000000 # flag: allow seeking to inexact position
BASS_POS_DECODE = 0x10000000 # flag: get the decoding (not playing) position
BASS_POS_DECODETO = 0x20000000 # flag: decode to the position instead of seeking
BASS_POS_SCAN = 0x40000000 # flag: scan to the position

# BASS_ChannelSetDevice/GetDevice option
BASS_NODEVICE = 0x20000

# BASS_RecordSetInput flags
BASS_INPUT_OFF = 0x10000
BASS_INPUT_ON = 0x20000

BASS_INPUT_TYPE_MASK = 0xff000000
BASS_INPUT_TYPE_UNDEF = 0x00000000
BASS_INPUT_TYPE_DIGITAL = 0x01000000
BASS_INPUT_TYPE_LINE = 0x02000000
BASS_INPUT_TYPE_MIC = 0x03000000
BASS_INPUT_TYPE_SYNTH = 0x04000000
BASS_INPUT_TYPE_CD = 0x05000000
BASS_INPUT_TYPE_PHONE = 0x06000000
BASS_INPUT_TYPE_SPEAKER = 0x07000000
BASS_INPUT_TYPE_WAVE = 0x08000000
BASS_INPUT_TYPE_AUX = 0x09000000
BASS_INPUT_TYPE_ANALOG = 0x0a000000

# BASS_ChannelSetFX effect types
BASS_FX_DX8_CHORUS = 0
BASS_FX_DX8_COMPRESSOR = 1
BASS_FX_DX8_DISTORTION = 2
BASS_FX_DX8_ECHO = 3
BASS_FX_DX8_FLANGER = 4
BASS_FX_DX8_GARGLE = 5
BASS_FX_DX8_I3DL2REVERB = 6
BASS_FX_DX8_PARAMEQ = 7
BASS_FX_DX8_REVERB = 8
BASS_FX_VOLUME = 9

# BASS_DX8_PHASE_xxx
BASS_DX8_PHASE_NEG_180 = 0
BASS_DX8_PHASE_NEG_90 = 1
BASS_DX8_PHASE_ZERO = 2
BASS_DX8_PHASE_90 = 3
BASS_DX8_PHASE_180 = 4

# iOS notification types (BASS_CONFIG_IOS_NOTIFY)
BASS_IOSNOTIFY_INTERRUPT = 1 # interruption started
BASS_IOSNOTIFY_INTERRUPT_END = 2 # interruption ended
#endregion

#region Callbacks
# Streams callbacks
DOWNLOADPROC =  ctypes.CFUNCTYPE(None, PTR, DWORD, PTR)
DownloadProcType = typing.Callable[[PTR, DWORD, PTR], None]
FILECLOSEPROC = ctypes.CFUNCTYPE(None, PTR)
FileCloseProc = typing.Callable[[PTR], None]
FILELENPROC =   ctypes.CFUNCTYPE(QWORD, PTR)
FileLenProc = typing.Callable[[PTR], QWORD]
FILEREADPROC =  ctypes.CFUNCTYPE(DWORD, PTR, DWORD, PTR)
FileReadProcType = typing.Callable[[PTR, DWORD, PTR], DWORD]
FILESEEKPROC =  ctypes.CFUNCTYPE(BOOL, QWORD, PTR)
FileSeekProcType = typing.Callable[[QWORD, PTR], BOOL]
STREAMPROC =    ctypes.CFUNCTYPE(DWORD, HSTREAM, PTR, PTR)
StreamProcType = typing.Callable[[HSTREAM, PTR, PTR], DWORD]

# Record callback
RECORDPROC =    ctypes.CFUNCTYPE(BOOL, HRECORD, PTR, DWORD, PTR)
RecordProcType = typing.Callable[[HRECORD, PTR, DWORD, PTR], BOOL]

# Channel callbacks
DSPPROC =       ctypes.CFUNCTYPE(None, HDSP, DWORD, PTR, DWORD, PTR)
DSPProcType = typing.Callable[[HDSP, DWORD, PTR, DWORD, PTR], None]
SYNCPROC =      ctypes.CFUNCTYPE(None, HSYNC, DWORD, DWORD, PTR)
SyncProcType = typing.Callable[[HSYNC, DWORD, DWORD, PTR], None]

IOSNOTIFYPROC = ctypes.CFUNCTYPE(None, DWORD)
IOSNotifyProcType = typing.Callable[[DWORD], None]
#endregion

#region Structures
# BASS / Config doesn't have any documented structures
# BASS / Plugins
class BASS_PLUGINFORM(ctypes.Structure):
    _fields_ = [
        ("ctype", DWORD),   # channel type
        ("name",  CHARP),   # format description (const char * or const wchar_t *)
        ("exts",  CHARP)    # file extension filter (const char * or const wchar_t *)
    ]
class BASS_PLUGININFO(ctypes.Structure):
    _fields_ = [
        ("version", DWORD),         # version (same form as BASS_GetVersion)
        ("formatc", DWORD),         # number of formats
        ("formats", ctypes.POINTER(BASS_PLUGINFORM)) # const BASS_PLUGINFORM *
    ]

# BASS / Initialization, info, etc...
class BASS_DEVICEINFO(ctypes.Structure):
    _fields_ = [
        ("name", CHARP),   # const char *name; (wchar_t* в некоторых конфигурациях Windows)
        ("driver", CHARP), # const char *driver; (wchar_t* в некоторых конфигурациях Windows)
        ("flags", DWORD)
    ]
class BASS_INFO(ctypes.Structure):
    _fields_ = [
        ("flags", DWORD),       # device capabilities (DSCAPS_xxx flags)
        ("hwsize", DWORD),      # unused
        ("hwfree", DWORD),      # unused
        ("freesam", DWORD),     # unused
        ("free3d", DWORD),      # unused
        ("minrate", DWORD),     # unused
        ("maxrate", DWORD),     # unused
        ("eax", BOOL),          # unused
        ("minbuf", DWORD),      # recommended minimum buffer length in ms
        ("dsver", DWORD),       # DirectSound version
        ("latency", DWORD),     # average delay (in ms) before start of playback
        ("initflags", DWORD),   # BASS_Init "flags" parameter
        ("speakers", DWORD),    # number of speakers available
        ("freq", DWORD)         # current output rate
    ]

# BASS / 3D
class BASS_3DVECTOR(ctypes.Structure):
    _fields_ = [
        ("x", FLOAT), # +=right, -=left
        ("y", FLOAT), # +=up, -=down
        ("z", FLOAT)  # +=front, -=behind
    ]

# BASS / Samples
class BASS_SAMPLE(ctypes.Structure):
    _fields_ = [
        ("freq",    DWORD), # default playback rate
        ("volume",  FLOAT), # default volume (0-1)
        ("pan",     FLOAT), # default pan (-1=left, 0=middle, 1=right)
        ("flags",   DWORD), # BASS_SAMPLE_xxx flags
        ("length",  DWORD), # length (in bytes)
        ("max",     DWORD), # maximum simultaneous playbacks
        ("origres", DWORD), # original resolution
        ("chans",   DWORD), # number of channels
        ("mingap",  DWORD), # minimum gap (ms) between creating channels
        ("mode3d",  DWORD), # BASS_3DMODE_xxx mode
        ("mindist", FLOAT), # minimum distance
        ("maxdist", FLOAT), # maximum distance
        ("iangle",  DWORD), # angle of inside projection cone
        ("oangle",  DWORD), # angle of outside projection cone
        ("outvol",  FLOAT), # delta-volume outside the projection cone
        ("vam",     DWORD), # unused
        ("priority", DWORD) # unused
    ]

# BASS / Streams
class BASS_FILEPROCS(ctypes.Structure):
    _fields_ = [
        ("close",  ctypes.POINTER(FILECLOSEPROC)),
        ("length", ctypes.POINTER(FILELENPROC)),
        ("read",   ctypes.POINTER(FILEREADPROC)),
        ("seek",   ctypes.POINTER(FILESEEKPROC))
    ]

# BASS / MOD music doesn't have any documented structures
# BASS / Recording
class BASS_RECORDINFO(ctypes.Structure):
    _fields_ = [
        ("flags",   DWORD), # device capabilities (DSCCAPS_xxx flags)
        ("formats", DWORD), # supported standard formats (WAVE_FORMAT_xxx flags)
        ("inputs",  DWORD), # number of inputs
        ("singlein", BOOL), # TRUE = only 1 input can be set at a time
        ("freq",    DWORD)  # current input rate
    ]

# BASS / Channels
class BASS_CHANNELINFO(ctypes.Structure):
    _fields_ = [
        ("freq",    DWORD),
        ("chans",   DWORD),
        ("flags",   DWORD),
        ("ctype",   DWORD),       # type of channel
        ("origres", DWORD),     # original resolution
        ("plugin",  HPLUGIN),
        ("sample",  HSAMPLE),
        ("filename", CHARP) # const char *
    ]
class TAG_APE_BINARY(ctypes.Structure):
    _fields_ = [
        ("key",     CHARP),   # const char *
        ("data",    PTR),  # const void *
        ("length",  DWORD)
    ]
class TAG_BEXT(ctypes.Structure):
    _fields_ = [
        ("Description",     CHAR * 256),
        ("Originator",      CHAR * 32),
        ("OriginatorReference", CHAR * 32),
        ("OriginationDate", CHAR * 10), # yyyy-mm-dd
        ("OriginationTime", CHAR * 8),   # hh-mm-ss
        ("TimeReference",   QWORD),                 # little-endian
        ("Version",         WORD),                        # little-endian
        ("UMID",            BYTE * 64),
        ("Reserved",        BYTE * 190)
        #TODO char CodingHistory[]
    ]
class TAG_CA_CODEC(ctypes.Structure):
    _fields_ = [
        ("ftype", DWORD), # file format
        ("atype", DWORD), # audio format
        ("name",  CHARP)  # const char *
    ]
class TAG_CART_TIMER(ctypes.Structure):
    _fields_ = [
        ("dwUsage", DWORD), # FOURCC timer usage ID
        ("dwValue", DWORD)  # timer value in samples from head
    ]
class TAG_CART(ctypes.Structure):
    _fields_ = [
        ("Version",     CHAR * 4),
        ("Title",       CHAR * 64),
        ("Artist",      CHAR * 64),
        ("CutID",       CHAR * 64),
        ("ClientID",    CHAR * 64),
        ("Category",    CHAR * 64),
        ("Classification", CHAR * 64),
        ("OutCue",      CHAR * 64),
        ("StartDate",   CHAR * 10),  # yyyy-mm-dd
        ("StartTime",   CHAR * 8),   # hh:mm:ss
        ("EndDate",     CHAR * 10),    # yyyy-mm-dd
        ("EndTime",     CHAR * 8),     # hh:mm:ss
        ("ProducerAppID", CHAR * 64),
        ("ProducerAppVersion", CHAR * 64),
        ("UserDef",     CHAR * 64),
        ("dwLevelReference", DWORD), # sample value for 0 dB reference
        ("PostTimer",   TAG_CART_TIMER * 8),
        ("Reserved",    CHAR * 276), 
        ("URL",         CHAR * 1024)
        #RODO char TagText[];
    ]
class TAG_CUE_POINT(ctypes.Structure):
    _fields_ = [
        ("dwName", DWORD),
        ("dwPosition", DWORD),
        ("fccChunk", DWORD),
        ("dwChunkStart", DWORD),
        ("dwBlockStart", DWORD),
        ("dwSampleOffset", DWORD)
    ]
class TAG_CUE(ctypes.Structure):
    _fields_ = [
        ("dwCuePoints", DWORD)
        #TODO TAG_CUE_POINT CuePoints[];
    ]
class TAG_ID3(ctypes.Structure):
    _fields_ = [
        ("id",      CHAR * 3),
        ("title",   CHAR * 30),
        ("artist",  CHAR * 30),
        ("album",   CHAR * 30),
        ("year",    CHAR * 4),
        ("comment", CHAR * 30),
        ("genre",   BYTE)
    ]
class TAG_SMPL_LOOP(ctypes.Structure):
    _fields_ = [
        ("dwIdentifier", DWORD),
        ("dwType", DWORD),
        ("dwStart", DWORD),
        ("dwEnd", DWORD),
        ("dwFraction", DWORD),
        ("dwPlayCount", DWORD)
    ]
class TAG_SMPL(ctypes.Structure):
    _fields_ = [
        ("dwManufacturer", DWORD),
        ("dwProduct", DWORD),
        ("dwSamplePeriod", DWORD),
        ("dwMIDIUnityNote", DWORD),
        ("dwMIDIPitchFraction", DWORD),
        ("dwSMPTEFormat", DWORD),
        ("dwSMPTEOffset", DWORD),
        ("cSampleLoops", DWORD),
        ("cbSamplerData", DWORD)
        #TODO TAG_SMPL_LOOP SampleLoops[]
    ]

# BASS / Effects (DirectX 8)
class BASS_DX8_CHORUS(ctypes.Structure):
    _fields_ = [
        ("fWetDryMix",  FLOAT),
        ("fDepth",      FLOAT),
        ("fFeedback",   FLOAT),
        ("fFrequency",  FLOAT),
        ("lWaveform",   DWORD), # 0=triangle, 1=sine
        ("fDelay",      FLOAT),
        ("lPhase",      DWORD)  # BASS_DX8_PHASE_xxx
    ]
class BASS_DX8_COMPRESSOR(ctypes.Structure):
    _fields_ = [
        ("fGain",       FLOAT),
        ("fAttack",     FLOAT),
        ("fRelease",    FLOAT),
        ("fThreshold",  FLOAT),
        ("fRatio",      FLOAT),
        ("fPredelay",   FLOAT)
    ]
class BASS_DX8_DISTORTION(ctypes.Structure):
    _fields_ = [
        ("fGain",       FLOAT),
        ("fEdge",       FLOAT),
        ("fPostEQCenterFrequency", FLOAT),
        ("fPostEQBandwidth", FLOAT),
        ("fPreLowpassCutoff", FLOAT)
    ]
class BASS_DX8_ECHO(ctypes.Structure):
    _fields_ = [
        ("fWetDryMix",  FLOAT),
        ("fFeedback",   FLOAT),
        ("fLeftDelay",  FLOAT),
        ("fRightDelay", FLOAT),
        ("lPanDelay",   BOOL)
    ]
class BASS_DX8_FLANGER(ctypes.Structure):
    _fields_ = [
        ("fWetDryMix",  FLOAT),
        ("fDepth",      FLOAT),
        ("fFeedback",   FLOAT),
        ("fFrequency",  FLOAT),
        ("lWaveform",   DWORD), # 0=triangle, 1=sine
        ("fDelay",      FLOAT),
        ("lPhase",      DWORD)  # BASS_DX8_PHASE_xxx
    ]
class BASS_DX8_GARGLE(ctypes.Structure):
    _fields_ = [
        ("dwRateHz",    DWORD), # Rate of modulation in hz
        ("dwWaveShape", DWORD)  # 0=triangle, 1=square
    ]
class BASS_DX8_I3DL2REVERB(ctypes.Structure):
    _fields_ = [
        ("lRoom",       INT),       # [-10000, 0]      default: -1000 mB
        ("lRoomHF",     INT),       # [-10000, 0]      default: 0 mB
        ("flRoomRolloffFactor", FLOAT), # [0.0, 10.0]      default: 0.0
        ("flDecayTime", FLOAT),     # [0.1, 20.0]      default: 1.49s
        ("flDecayHFRatio", FLOAT),  # [0.1, 2.0]       default: 0.83
        ("lReflections", INT),      # [-10000, 1000]   default: -2602 mB
        ("flReflectionsDelay", FLOAT),# [0.0, 0.3]       default: 0.007 s
        ("lReverb",     INT),       # [-10000, 2000]   default: 200 mB
        ("flReverbDelay", FLOAT),   # [0.0, 0.1]       default: 0.011 s
        ("flDiffusion", FLOAT),     # [0.0, 100.0]     default: 100.0 %
        ("flDensity",   FLOAT),     # [0.0, 100.0]     default: 100.0 %
        ("flHFReference", FLOAT)    # [20.0, 20000.0]  default: 5000.0 Hz
    ]
class BASS_DX8_PARAMEQ(ctypes.Structure):
    _fields_ = [
        ("fCenter",     FLOAT),
        ("fBandwidth",  FLOAT),
        ("fGain",       FLOAT)
    ]
class BASS_DX8_REVERB(ctypes.Structure):
    _fields_ = [
        ("fInGain",     FLOAT),        # [-96.0,0.0]            default: 0.0 dB
        ("fReverbMix",  FLOAT),     # [-96.0,0.0]            default: 0.0 db
        ("fReverbTime", FLOAT),    # [0.001,3000.0]         default: 1000.0 ms
        ("fHighFreqRTRatio", FLOAT) # [0.001,0.999]          default: 0.001
    ]
class BASS_FX_VOLUME_PARAM(ctypes.Structure):
    _fields_ = [
        ("fTarget",     FLOAT),
        ("fCurrent",    FLOAT),
        ("fTime",       FLOAT), # In seconds
        ("lCurve",      DWORD) # 0 for linear, 1 for logarithmic (BASS_SLIDE_LOG) - check constants
    ]

class WAVEFORMATEX(ctypes.Structure):
    _pack_ = 1 # From #pragma pack(push,1)
    _fields_ = [
        ("wFormatTag", WORD),
        ("nChannels", WORD),
        ("nSamplesPerSec", DWORD),
        ("nAvgBytesPerSec", DWORD),
        ("nBlockAlign", WORD),
        ("wBitsPerSample", WORD),
        ("cbSize", WORD)
    ]
LPWAVEFORMATEX = ctypes.POINTER(WAVEFORMATEX)
#enderegion