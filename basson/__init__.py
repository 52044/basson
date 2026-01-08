from .api import (
    BASS,       # API provider
    BASSError   # Exception class
)

from .basson import (
    Basson      # Main wrapper class
)

from .header import ( # Flags and Enums. OG
    #1                  #2                  #3                  #4
    ConfigOption,       IOSSessionFlag,     DeviceFlag,         D3AlorithmsOption,
    CommonFlag,         StatusOption,       NetPlaylistOption,  DXVersionOption,
    NorampOption,       SamplerateConversionOption, ChannelType, DataLengthOption,
    DataFlag,           PosModeOption,      ChannelOption,      SampleFlag,
    StreamFlag,         InfoFlag,           MusicFreqOption,    MusicFlag,
    SpeakerFlag,        MusicSurroundOption, RecordFlag,
    RECORDPROC
)

from .structures import (
    Info,               DeviceInfo,
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
    "SpeakerFlag",      "MusicSurroundOption", "RecordFlag", 
    "RECORDPROC"   

    "Info",             "DeviceInfo",

    "StreamFile",       "StreamURL",
    "Music",
    "Record",

    "get_os"
    ]