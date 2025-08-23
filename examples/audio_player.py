# by ChatGPT5

import tkinter as tk
from tkinter import filedialog
import os
import time

import basson
from basson.utils import get_os

class BassTkPlayer:
    def __init__(self, root):
        self.root = root
        self.root.title("BassTkPlayer")
        self.root.geometry("400x200")
        self.unicode = 0

        # === Init Bass ===
        if get_os() == "windows":
            lib = os.path.join("dll", "bass_x64.dll")
            self.unicode = basson.CommonFlags.UNICODE
        else:
            lib = os.path.join("dll", "libbass.dylib")

        self.bass = basson.BASS(lib)
        self.bass.init(-1, 44100, basson.DeviceFlags.STEREO)

        self.stream = None

        # === UI Elements ===
        self.label = tk.Label(root, text="No file loaded", anchor="w")
        self.label.pack(fill='x', pady=5)

        # время
        self.time_label = tk.Label(root, text="00:00:00 / 00:00:00")
        self.time_label.pack(pady=5)

        btn_frame = tk.Frame(root)
        btn_frame.pack()

        self.btn_open = tk.Button(btn_frame, text="Open File", command=self.load_file)
        self.btn_open.pack(side='left', padx=5)

        self.btn_play = tk.Button(btn_frame, text="Play", command=self.play)
        self.btn_play.pack(side='left', padx=5)

        self.btn_stop = tk.Button(btn_frame, text="Stop", command=self.stop)
        self.btn_stop.pack(side='left', padx=5)

        # Volume
        self.volume = tk.DoubleVar(value=1.0)
        self.vol_slider = tk.Scale(
            root, from_=0.0, to=1.0, resolution=0.01,
            label="Volume", orient='horizontal',
            variable=self.volume, command=self.set_volume
        )
        self.vol_slider.pack(fill='x', padx=10)

        # Position
        self.position = tk.DoubleVar()
        self.pos_slider = tk.Scale(
            root, from_=0, to=100, orient="horizontal",
            label="Position", variable=self.position,
            showvalue=False, command=self.seek
        )
        self.pos_slider.pack(fill='x', padx=10)
        self.updating_slider = False

        # === Timer ===
        self.update_position()

    def load_file(self):
        file = filedialog.askopenfilename(
            title="Select audio file",
            filetypes=[("Audio files", "*.mp3 *.wav *.ogg *.aac"), ("All files", "*.*")]
        )
        if file:
            if self.stream:
                self.stream.stop()

            self.stream = basson.StreamFile(
                self.bass, False, file, 0, 0,
                self.unicode
            )
            self.label.config(text=os.path.basename(file))

    def play(self):
        if self.stream:
            self.stream.start()

    def stop(self):
        if self.stream:
            self.stream.stop()

    def set_volume(self, value):
        if self.stream:
            self.stream.volume = float(value)

    def update_position(self):
        if self.stream:
            try:
                pos = self.stream.position
                length = self.stream.length
                pos_sec = self.stream.bytes2seconds(pos)
                len_sec = self.stream.bytes2seconds(length)

                pos_str = time.strftime('%H:%M:%S', time.gmtime(pos_sec))
                len_str = time.strftime('%H:%M:%S', time.gmtime(len_sec))
                self.time_label.config(text=f"{pos_str} / {len_str}")

                if not self.updating_slider:
                    self.pos_slider.config(to=len_sec)
                    self.position.set(pos_sec)
            except Exception:
                pass
        self.root.after(500, self.update_position)

    def seek(self, value):
        if self.stream:
            try:
                self.updating_slider = True
                seconds = float(value)
                byte_pos = self.stream.seconds2bytes(seconds)
                self.stream.position = byte_pos
            except Exception:
                pass
            finally:
                self.updating_slider = False


if __name__ == '__main__':
    root = tk.Tk()
    app = BassTkPlayer(root)
    root.mainloop()
