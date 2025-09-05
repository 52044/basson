# Some useful utiliies

import ctypes

def get_os() -> str:
    """ Returns OS name"""
    import platform
    import os

    system = platform.system().lower()
    if system == 'windows':
        return 'windows'
    elif system == 'darwin':
        if any(x in platform.platform().lower() for x in ['ios', 'iphone', 'ipad']):
            return 'ios'
        return 'macos'
    elif system == 'linux':
        if 'android' in platform.release().lower() or 'ANDROID_ROOT' in os.environ:
            return 'android'
        try: # WSL check
            with open('/proc/version', 'r') as f:
                if 'microsoft' in f.read().lower():
                    return 'wsl'
        except FileNotFoundError:
            pass
        return 'linux'
    elif system == 'freebsd':
        return 'freebsd'
    elif system == 'openbsd':
        return 'openbsd'
    elif system == 'netbsd':
        return 'netbsd'
    elif system == 'aix':
        return 'aix'
    else:
        return 'unknown'

def get_locale() -> str:
    ''' Return OS locale encoder name '''
    import locale
    return locale.getpreferredencoding()

@staticmethod
def decode_version(version:int) -> str:
    ''' Convers HEX value to human-understandable text
    
    :param version: Value in hex
    :type version: int
    :rtype: str
    :return: Decoded text
    '''
    major = (version >> 24) & 0xFF
    minor = (version >> 16) & 0xFF
    patch = (version >> 8) & 0xFF
    build = version & 0xFF
    return f"{major}.{minor}.{patch}.{build}"

def read_ptr(ptr:ctypes.c_void_p, read_type:str = 'str', struct_type = None):
   if struct_type is not None: return ctypes.cast(ptr, ctypes.POINTER(struct_type)).contents
   match read_type:
      case 'str': return ctypes.cast(ptr, ctypes.c_char_p).value.decode('utf-8')
      case _: raise ValueError(f"Invalid cast type: {read_type}")

def make_ptr(value, value_type:str = 'str', struct_type = None):
    #FIXME probably it's wrong, cuz need to keep created pointer, but for now it works
    if struct_type is not None: return ctypes.byref(struct_type), value
    match value_type:
        case 'str': return ctypes.create_string_buffer(value.encode('utf-8'))
        case 'int': return ctypes.c_int(value)
        case 'float': return ctypes.c_float(value)

        case _: raise ValueError(f"Invalid value type: {value_type}")

def safe_decode(b: bytes) -> str:
    import locale
    return b.decode(locale.getpreferredencoding(), errors='replace')
