# Manual of Basson

Basson is user-frendly wrapper over original BASS audio library. It uses all power of OOP for comfortable usage, also provided pretty good documentation. *(i try by best)*

# class `BASS`

Class `BASS` represents BASS library itself, providing overhaul config functions and properies.

At first, you need to load OS specific library file as initialization parameter

```python
import basson

match basson.utils.get_os()
    case 'windows':
        path = 'path_to_your.dll'
    case 'macos':
        path = 'path_to_your.dylib'
    case 'linux':
        path = 'path_to_your.so'
    #etc
    
player = basson.BASS('path_to_your.dll')
player.init(-1, 44100, basson.DeviceFlags.STEREO)
```

Then you can use that object while creating new channels. Changing parameters of main class affects to all referenced objects.

```python
mp3 = basson.StreamFile(player, 0, 'path_to_your.mp3')
mp3.start() # Channel start plaing by himself
player.stop() # Stops `mp3` channel
```

*P.S.: You can use direct fuctions of BASS by executing commands from `player.bass`, but it won't provide any info to wrapper back*!

# class `Channel`

Channel in BASS - some sort of container of user provided data. It can be represented as channel of (hardware) audio mixer - contain source, some settings, parameters, effects and routing. It have 4 types of that:

* **Stream** - audio file is streamed from filesystem or internet
* **Sample** - audio file is loaded in memory 
* **Music** - tracker audio file (`*.MOD` or `*.MO3`)
* **Record** - channel desined for creating new audio files

Before creating new channel, requied create and initialize BASS, after that you can create desirable type of channel. 

You cannot directly create a "generic" channel and change it later, because BASS don't desined at that (no OOP, pure c). If you look at BASS API, you see that all audio manipulation requied `handle`. BASS gives to you only after creating any type of channel:

```cpp
...
const int mp3 = BASS_StreamCreateFile(0, 'path_to_your.mp3', 0, 0);
BASS_ChannelSetPosition(mp3, BASS_ChannelSeconds2Bytes(mp3, 30.5), BASS_POS_BYTE);
BASS_ChannelSetAttribute(mp3, BASS_ATTRIB_VOL, 0.8);
BASS_ChannelStart(mp3);
```

By handles you can do thatever you want, but you also requied keep in mind, that you doing with handle and all (it a pure c, baby)

Les't have a look to our variant in Python:
```python
...
mp3 = basson.StreamFile(buzz, 0, 'path_to_your.mp3')
mp3.position = 30.5
mp3.volume = 0.8
mp3.start()
```

Much clenier, yea?

Under the hood we do same operation. `mp3` object while creation contain `.HANDLE` variable, that allow do that we want.