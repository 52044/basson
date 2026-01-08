from .api import (
    BASS,       # API provider
    BASSError   # Exception class
)

from .basson import (
    Basson      # Main wrapper class
)
Basson = Basson #HACK if import library as tells `readme.md`, for acess requied `from basson import basson`, instead just a `import bassson`. Solution provided by AI and requied testing 

from .header import ( # Flags and Enums. OG
    #1                  #2                  #3                  #4
    Info,               DeviceInfo,
    ConfigOption,       IOSSessionFlag,     DeviceFlag,         D3AlorithmsOption,
    CommonFlag,         StatusOption,       NetPlaylistOption,  DXVersionOption,
    NorampOption,       SamplerateConversionOption, ChannelType, DataLengthOption,
    DataFlag,           PosModeOption,      ChannelOption,      SampleFlag,
    StreamFlag,         InfoFlag,           MusicFreqOption,    MusicFlag,
    SpeakerFlag,        MusicSurroundOption, 
)

from .channel import (
    Channel,
)

from .stream import (
    StreamFile,         StreamURL,
)

from .music import (
    Music
)

from .record import (
    Record
)

from .utils import get_os

__all__ = [
    "BASS", "BASSError", 
    "Basson",

    #1                  #2                  #3                  #4
    "ConfigOption",     "IOSSessionFlag",   "DeviceFlag",       "D3AlorithmsOption", 
    "CommonFlag",       "StatusOption",     "NetPlaylistOption", "DXVersionOption",
    "NorampOption",     "SamplerateConversionOption", "ChannelType", "DataLengthOption",
    "DataFlag",         "PosModeOption",    "ChannelOption",    "SampleFlag",
    "StreamFlag",       "InfoFlag",         "MusicFreqOption",  "MusicFlag",
    "SpeakerFlag",      "MusicSurroundOption", 

    "Info",             "DeviceInfo",

    "Channel",

    "StreamFile",       "StreamURL",
    "Music",
    "Record",

    "get_os"
    ]