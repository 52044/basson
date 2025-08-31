# Basson - BASS python wrapper

![Basson Logo](docs/logo.png)  
**BASS Object Native**  
_because pybass was already taken :(_

Python user-frendly wrapper over [original BASS library](https://www.un4seen.com/bass.html). It allowes use all power of object-oriented Python language for simple and powerful audio playback. No other library can compete with power and simplisity of BASS!

**Make sure, what your project is not violating BASS license** (you can read that in `LICENSE.BASS.md`)

## Advantages

* `Stream`, `Music`, `Sample`, `Record` presented as in original BASS, nothing new has been invented
* All `Channel` parameters implemented as properties (no more `BASS_GetAttribute`!)
* Safe execution (BASS errors raises exceptions)
* Proper inline documentation*
* Pylance frendly
* Access to BASS API directly, via `basson.bass.__xyz__`

## How to use

1. Download this repository and `pip install -e to_this_path`
2. Download library file from <https://www.un4seen.com/bass.html>, depending wich OS you are using
3. Start writing beautiful code!

```python
import basson

bass = basson.BASS(path_to_bass_dll)
bass.init(-1, 44100, basson.DeviceFlags.STEREO)
audio = basson.StreamFile(bass, 0, path_to_audio_file.mp3)
audio.play()
```
