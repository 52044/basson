# ctypes desctiptions

import ctypes
import typing

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
TRUE = 1 
'''`True` value in BASS'''
FALSE = 0 
'''`False` value in BASS'''
MINUSONE = 0xFFFFFFFF
'''`-1` value'''

# Pointers types (handles) BASS
#   There are different handle names for visual separating the destination. 
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