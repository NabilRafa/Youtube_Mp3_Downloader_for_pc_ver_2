"""
YouTube Audio Downloader - Unified Version
Support: M4A, OPUS (WebM), MP3
"""

import tkinter as tk
from tkinter import ttk, filedialog, messagebox
import os
from pathlib import Path
import threading
import sys

try:
    import yt_dlp
except ImportError:
    print("yt-dlp belum terinstall! pip install yt-dlp")
    exit()


# ===== OPTIONAL FFMPEG DETECTION =====
def get_ffmpeg_path():
    if getattr(sys, 'frozen', False):
        base_path = os.path.dirname(sys.executable)
    else:
        base_path = os.path.dirname(os.path.abspath(__file__))

    ffmpeg_path = os.path.join(base_path, "ffmpeg.exe")
    return ffmpeg_path if os.path.exists(ffmpeg_path) else None


class YouTubeAudioDownloader:
    def __init__(self, root):
        self.root = root
        self.root.title("YouTube Audio Downloader")
        self.root.geometry("600x485")
        self.root.resizable(True, True)

        self.download_path = str(Path.home() / "Downloads" / "YouTube_Audio")
        os.makedirs(self.download_path, exist_ok=True)

        self.setup_ui()

    def setup_ui(self):
        header = tk.Frame(self.root, bg="#1a73e8", height=60)
        header.pack(fill=tk.X)
        header.pack_propagate(False)

        tk.Label(
            header,
            text="🎵 YouTube Audio Downloader",
            font=("Arial", 18, "bold"),
            bg="#1a73e8",
            fg="white"
        ).pack(pady=15)

        main = tk.Frame(self.root, padx=20, pady=20)
        main.pack(fill=tk.BOTH, expand=True)

        tk.Label(main, text="Link YouTube:", font=("Arial", 11)).pack(anchor=tk.W)

        self.link_entry = tk.Entry(main, font=("Arial", 11))
        self.link_entry.pack(fill=tk.X, pady=(5, 15))
        self.link_entry.bind("<Return>", lambda e: self.start_download())

        # ===== FORMAT OPTIONS =====
        tk.Label(main, text="Format Audio:", font=("Arial", 11)).pack(anchor=tk.W)

        self.format_var = tk.StringVar(value="m4a")

        formats = [
            ("MP3 (Butuh FFmpeg)", "mp3"),
            ("M4A (Best compatibility)", "m4a"),
            ("OPUS (WebM, small size)", "opus"),
        ]

        for text, value in formats:
            tk.Radiobutton(
                main,
                text=text,
                variable=self.format_var,
                value=value,
                font=("Arial", 10)
            ).pack(anchor=tk.W)

        # ===== LOCATION =====
        tk.Label(main, text="Lokasi Download:", font=("Arial", 11)).pack(anchor=tk.W, pady=(15,0))

        path_frame = tk.Frame(main)
        path_frame.pack(fill=tk.X, pady=5)

        self.path_entry = tk.Entry(path_frame, font=("Arial", 10))
        self.path_entry.insert(0, self.download_path)
        self.path_entry.pack(side=tk.LEFT, fill=tk.X, expand=True)

        tk.Button(
            path_frame,
            text="Browse",
            command=self.browse_folder
        ).pack(side=tk.LEFT, padx=5)

        # ===== DOWNLOAD BUTTON =====
        self.download_btn = tk.Button(
            main,
            text="⬇ Download",
            command=self.start_download,
            bg="#1a73e8",
            fg="white",
            font=("Arial", 12, "bold"),
            height=2
        )
        self.download_btn.pack(fill=tk.X, pady=15)

        self.progress = ttk.Progressbar(main, mode='indeterminate')
        self.progress.pack(fill=tk.X)

        self.status_label = tk.Label(
            main,
            text="Masukkan link dan pilih format.",
            font=("Arial", 10),
            fg="#5f6368",
            wraplength=550,
            justify=tk.LEFT
        )
        self.status_label.pack(anchor=tk.W, pady=10)

    def browse_folder(self):
        folder = filedialog.askdirectory()
        if folder:
            self.download_path = folder
            self.path_entry.delete(0, tk.END)
            self.path_entry.insert(0, folder)

    def start_download(self):
        url = self.link_entry.get().strip()

        if not url:
            messagebox.showwarning("Warning", "Masukkan link YouTube.")
            return

        self.download_path = self.path_entry.get()

        thread = threading.Thread(target=self.download_audio, args=(url,))
        thread.daemon = True
        thread.start()

    def download_audio(self, url):
        self.download_btn.config(state=tk.DISABLED)
        self.progress.start(10)
        self.status_label.config(text="Mengambil informasi...")

        try:
            selected_format = self.format_var.get()

            ydl_opts = {
                'outtmpl': os.path.join(self.download_path, '%(title)s.%(ext)s'),
                'progress_hooks': [self.progress_hook],
                'quiet': False,
                'no_warnings': False,
            }

            # ===== FORMAT LOGIC =====
            if selected_format == "m4a":
                ydl_opts['format'] = 'bestaudio[ext=m4a]/bestaudio'

            elif selected_format == "opus":
                ydl_opts['format'] = 'bestaudio[ext=webm]/bestaudio'

            elif selected_format == "mp3":
                ffmpeg_path = get_ffmpeg_path()

                if not ffmpeg_path:
                    messagebox.showerror(
                        "FFmpeg Tidak Ditemukan",
                        "MP3 membutuhkan ffmpeg.exe di folder aplikasi."
                    )
                    return

                ydl_opts['format'] = 'bestaudio/best'
                ydl_opts['ffmpeg_location'] = ffmpeg_path
                ydl_opts['postprocessors'] = [{
                    'key': 'FFmpegExtractAudio',
                    'preferredcodec': 'mp3',
                    'preferredquality': '192',
                }]

            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                info = ydl.extract_info(url, download=False)
                title = info.get('title', 'Unknown')

                self.status_label.config(text=f"Downloading: {title}")
                ydl.download([url])

            self.status_label.config(
                text="Selesai!",
                fg="green"
            )

            messagebox.showinfo("Berhasil", f"Download selesai:\n{title}")

        except Exception as e:
            self.status_label.config(text=f"Error: {str(e)}", fg="red")
            messagebox.showerror("Error", str(e))

        finally:
            self.progress.stop()
            self.download_btn.config(state=tk.NORMAL)

    def progress_hook(self, d):
        if d['status'] == 'downloading':
            percent = d.get('_percent_str', '0%')
            self.status_label.config(text=f"Downloading... {percent}", fg="#1a73e8")
        elif d['status'] == 'finished':
            self.status_label.config(text="Processing...", fg="#1a73e8")


def main():
    root = tk.Tk()
    app = YouTubeAudioDownloader(root)
    root.mainloop()


if __name__ == "__main__":
    main()