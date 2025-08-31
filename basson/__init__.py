# Error
from .api import BASSError

__all__ = [

    # Exceptions
    "BASSError", 
    ]

'''# Core object
from .BASS import BASS
from .stream import StreamFile, StreamURL

# Exception class
from .api.api import BASSException

# Additional utilities
from . import utils

# IntFlags & IntEnums
from .api.header import (
    #1                  #2                  #3                  #4
    IOSSessionFlags,    DeviceFlags,        D3AlorithmsOptions, SampleFlags,        
    StreamFlags,        PosOptions,         ChannelOptions,     DataFlags, 
    DataLengthOptions,  
    )

# Custom flags & emums
from .api.header import (
    #1                  #2                  #3                  #4
    NetPlaylistOptions, NorampOptions,      SamplerateConversionOptions, StatusOptions,
    InfoFlags,          DXVersionOptions,   CommonFlags,        ChannelType,
    )

__all__ = ["BASS", "BASSException",
           "StreamFile", "StreamURL",
           "utils",
           
           #1                   #2                  #3                  #4
           "IOSSessionFlags",   "DeviceFlags",      "D3AlorithmsOptions", "SampleFlags", 
           "StreamFlags",       "PosOptions",       "ChannelOptions",   "DataFlags", 
           "DataLengthOptions",

           "NetPlaylistOptions", "NorampOptions",   "SamplerateConversionOptions", "StatusOptions",
           "InfoFlags",         "DXVersionOptions", "CommonFlags",      "ChannelType",
           ]'''