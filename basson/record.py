from .basson import Basson
from .channel import Channel
from . import api, header
import ctypes

class Record(Channel):
    def __init__(self, basson: Basson, device: int = -1, freq: int = 44100, chans: int = 2,
                 flags: api.RecordFlag = 0, callback=None):
        """ 
        Creating Recording channel\n
        Note: Only one `Record` channel can be assigned to one BASS instance. If you want to record multiple devices, you need to create multiple `Basson` objects. (remarks on https://www.un4seen.com/doc/#bass/BASS_RecordInit.html )

        """

        # Check, if Record channel existing
        if basson._has_record_channel == True:
            raise api.BASSError(api.BASSError.ALREADY)


        # Assign context
        self.bass = basson.bass
        self._proc = api.RECORDPROC(callback) if callback else None

        # Device initialization
        self.bass.RecordInit(device)
        
        # Запуск записи
        self.HANDLE = self.bass.RecordStart(freq, chans, flags, self._proc, None)
        self.WHOAMI = api.ChannelType.RECORD

        super().__init__()

    def __del__(self):
        """ Освобождение ресурсов записи """

        super().__del__()
