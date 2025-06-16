import tkinter as tk
from tkinter import filedialog
import os

from basson import BassPlayer
from basson import utils

class BassTkPlayer:
    def __init__(self, root):
        self.root = root
        self.root.title("BassPlayer GUI")
        self.root.geometry("400x150")

        # === Init Bass ===
        if utils.getOS() == "windows":
            lib = os.path.join("dll", "bass_x64.dll")
        else:
            lib = os.path.join("dll", "libbass.dylib")

        self.player = BassPlayer(lib)
        self.player.Init(-1, 44100, 0, 0)

        # === UI Elements ===
        self.label = tk.Label(root, text="No file loaded", anchor="w")
        self.label.pack(fill='x')

        btn_frame = tk.Frame(root)
        btn_frame.pack()

        self.btn_open = tk.Button(btn_frame, text="Open File", command=self.load_file)
        self.btn_open.pack(side='left', padx=5)

        self.btn_play = tk.Button(btn_frame, text="Play", command=self.play)
        self.btn_play.pack(side='left', padx=5)

        self.btn_stop = tk.Button(btn_frame, text="Stop", command=self.stop)
        self.btn_stop.pack(side='left', padx=5)

        self.volume = tk.DoubleVar(value=1.0)
        self.vol_slider = tk.Scale(root, from_=0.0, to=1.0, resolution=0.01,
                                   label="Volume", orient='horizontal',
                                   variable=self.volume, command=self.set_volume)
        self.vol_slider.pack(fill='x', padx=10)

        self.position = tk.DoubleVar()
        self.pos_slider = tk.Scale(root, from_=0, to=100, orient="horizontal",
                                   label="Position", variable=self.position,
                                   showvalue=False, command=self.seek)
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
            self.player.File = file
            self.label.config(text=os.path.basename(file))

    def play(self):
        try:
            self.player.Play()
        except Exception as e:
            self.label.config(text=f"Error: {e}")

    def stop(self):
        try:
            self.player.Stop()
        except Exception as e:
            self.label.config(text=f"Error: {e}")

    def set_volume(self, value):
        try:
            self.player.Volume = float(value)
        except Exception:
            pass

    def update_position(self):
        try:
            pos = self.player.Position
            length = self.player.Lenght
            pos_sec = self.player.TimeConvert(pos)
            len_sec = self.player.TimeConvert(length)

            self.root.title(f"Playing: {pos_sec:.1f}s / {len_sec:.1f}s")

            if not self.updating_slider:
                self.pos_slider.config(to=len_sec)
                self.position.set(pos_sec)
        except:
            pass
        self.root.after(500, self.update_position)
    
    def seek(self, value):
        try:
            self.updating_slider = True
            seconds = float(value)
            byte_pos = self.player.TimeConvert(seconds)
            self.player.Position = byte_pos
        except:
            pass
        finally:
            self.updating_slider = False

# === Run ===
if __name__ == '__main__':
    root = tk.Tk()
    app = BassTkPlayer(root)
    root.mainloop()
