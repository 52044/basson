# Private part of BASS.h header

# BASS_Get/SetConfig(Ptr) options
from enum import IntEnum

class BassConfigOptions(IntEnum):
    BUFFER          = 0
    UPDATEPERIOD    = 1
    GVOL_SAMPLE     = 4
    GVOL_STREAM     = 5
    GVOL_MUSIC      = 6
    CURVE_VOL       = 7
    CURVE_PAN       = 8
    FLOATDSP        = 9
    ALGORITHM3D     = 10
    NET_TIMEOUT     = 11
    NET_BUFFER      = 12
    PAUSE_NOPLAY    = 13
    NET_PREBUF      = 15
    NET_PASSIVE     = 18
    REC_BUFFER      = 19
    NET_PLAYLIST    = 21
    MUSIC_VIRTUAL   = 22
    VERIFY          = 23
    UPDATETHREADS   = 24
    DEV_BUFFER      = 27
    REC_LOOPBACK    = 28
    VISTA_TRUEPOS   = 30
    IOS_SESSION     = 34
    IOS_MIXAUDIO    = 34 # Alias for BASS_CONFIG_IOS_SESSION
    DEV_DEFAULT     = 36
    NET_READTIMEOUT = 37
    VISTA_SPEAKERS  = 38
    IOS_SPEAKER     = 39
    MF_DISABLE      = 40
    HANDLES         = 41
    UNICODE         = 42
    SRC             = 43
    SRC_SAMPLE      = 44
    ASYNCFILE_BUFFER = 45
    OGG_PRESCAN     = 47
    MF_VIDEO        = 48
    AIRPLAY         = 49
    DEV_NONSTOP     = 50
    IOS_NOCATEGORY  = 51
    VERIFY_NET      = 52
    DEV_PERIOD      = 53
    FLOAT           = 54
    NET_SEEK        = 56
    AM_DISABLE      = 58
    NET_PLAYLIST_DEPTH = 59
    NET_PREBUF_WAIT = 60
    ANDROID_SESSIONID = 62
    WASAPI_PERSIST  = 65
    REC_WASAPI      = 66
    ANDROID_AAUDIO  = 67
    SAMPLE_ONEHANDLE = 69
    NET_META        = 71
    NET_RESTRATE    = 72
    REC_DEFAULT     = 73
    NORAMP          = 74
    # BASS_SetConfigPtr options
    NET_AGENT       = 16
    NET_PROXY       = 17
    IOS_NOTIFY      = 46
    ANDROID_JAVAVM  = 63
    LIBSSL          = 64
    FILENAME        = 75