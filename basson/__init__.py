# Core object
from .bass import BASS

# Exception class
from .api.api import BassError

# Additional utilities
from . import utils

# IntFlags & IntEnums
from .api.header import (
    #1                      #2                      #3                      #4
    BassErrorsOptions,      BassIOSSessionFlags,    BassDeviceFlags,        Bass3DAlorithmsOptions,
    )

# Custom flags & emums
from .api.header import (
    #1                      #2                      #3                      #4
    BassNetPlaylistOptions, BassNorampOptions,      BassSamplerateConversionOptions, BassStatusOptions,
    BassInfoFlags,          BassDXVersionOptions, 
    )

__all__ = ["BASS", 
           "BassError",
           "utils",
           
           "BassErrorsOptions", "BassIOSSessionFlags", "BassDeviceFlags", "Bass3DAlorithmsOptions",

           "BassNetPlaylistOptions", "BassNorampOptions", "BassSamplerateConversionOptions", "BassStatusOptions",
           "BassInfoFlags", "BassDXVersionOptions"
           ]