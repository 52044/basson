# Basson - BASS python wrapper

![Basson Logo](docs/logo.png)  
**BASS Object Native**  
_because pybass was already taken :(_

Python user-frendly wrapper over [original BASS library](https://www.un4seen.com/bass.html). It allowes use all power of object-oriented Python language for simple and powerful audio playback. No other library can compete with power and simplisity of BASS!

**Make sure, what your project is not violating BASS license** (you can read that in `LICENSE`)

***PROJECT IS IN DEVELOPMENT, SO ALOT IS NOT IMPLEMENTED YET***

## Advantages

* `Stream`, `Music`, `Sample`, `Record` presented as in original BASS, nothing new has been invented
* No more `BASS_GetAttribute` and `BASS_ChannelGetAttribute`, just regular properties
* Safe execution (BASS errors raises exceptions)
* Proper inline documentation*
* Access to BASS API directly, via `basson.bass.__xyz__`

## How to use

1. Download this repository and `pip install -e to_this_path`
2. Download library file from <https://www.un4seen.com/bass.html>, depending wich OS you are using
3. Start writing beautiful code!

```python
import basson

bass = basson.Basson('path_to_bass_dll')
bass.init(-1, 44100, basson.DeviceFlag.STEREO)
audio = basson.StreamFile(bass, 0, 'path_to_audio_file.mp3')
audio.play()
```
