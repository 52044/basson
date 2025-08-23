import time
import basson
import os

player = basson.BASS(os.path.join('dll', 'bass_x64.dll'))
print(basson.utils.decode_version(player.version))
player.init(-1, 44100, basson.DeviceFlags.STEREO)
mp3 = basson.StreamFile(player, 0, os.path.join('some_audio.mp3'), 0, 0, basson.CommonFlags.UNICODE)
mp3.start()
while 1:
    print(
        f"{time.strftime('%M:%S', time.gmtime(mp3.bytes2seconds(mp3.position)))} / {time.strftime('%M:%S', time.gmtime(mp3.bytes2seconds(mp3.length)))}",
        end="\r")