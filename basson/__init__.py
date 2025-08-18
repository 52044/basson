# Core object
from .bass import BASS
from .stream import StreamFile, StreamURL

# Exception class
from .api.api import BassError

# Additional utilities
from . import utils

# IntFlags & IntEnums
from .api.header import (
    #1                      #2                      #3                      #4
    BassIOSSessionFlags,    BassDeviceFlags,        Bass3DAlorithmsOptions, BassSampleFlags,        
    BassStreamFlags,        BassPosOptions,         BassChannelOptions,
    )

# Custom flags & emums
from .api.header import (
    #1                      #2                      #3                      #4
    BassNetPlaylistOptions, BassNorampOptions,      BassSamplerateConversionOptions, BassStatusOptions,
    BassInfoFlags,          BassDXVersionOptions,   BassCommonFlags,
    )

__all__ = ["BASS", 
           "StreamFile", "StreamURL",
           "BassError",
           "utils",
           
           "BassIOSSessionFlags", "BassDeviceFlags", "Bass3DAlorithmsOptions","BassSampleFlags", 
           "BassStreamFlags", "BassPosOptions", "BassChannelOptions",

           "BassNetPlaylistOptions", "BassNorampOptions", "BassSamplerateConversionOptions", "BassStatusOptions",
           "BassInfoFlags", "BassDXVersionOptions", "BassCommonFlags"
           ]