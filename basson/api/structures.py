from .types import *

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