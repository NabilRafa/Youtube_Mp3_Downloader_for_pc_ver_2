"""
YouTube to MP3 Downloader - GUI Version
Download langsung format audio tanpa perlu FFmpeg
"""

import tkinter as tk
from tkinter import ttk, filedialog, messagebox
import os
from pathlib import Path
import threading

try:
    import yt_dlp
except ImportError:
    print("Error: yt-dlp belum terinstall!")
    print("Silakan install dengan: pip install yt-dlp")
    exit()


class YouTubeMp3Downloader:
    def __init__(self, root):
        self.root = root
        self.root.title("YouTube MP3 Downloader")
        self.root.geometry("600x450")
        self.root.resizable(False, False)
        
        # Default download folder
        self.download_path = str(Path.home() / "Downloads" / "YouTube_MP3")
        os.makedirs(self.download_path, exist_ok=True)
        
        self.setup_ui()
    
    def setup_ui(self):
        # Header
        header_frame = tk.Frame(self.root, bg="#1a73e8", height=60)
        header_frame.pack(fill=tk.X)
        header_frame.pack_propagate(False)
        
        title_label = tk.Label(
            header_frame,
            text="🎵 YouTube MP3 Downloader",
            font=("Arial", 18, "bold"),
            bg="#1a73e8",
            fg="white"
        )
        title_label.pack(pady=15)
        
        # Main content
        main_frame = tk.Frame(self.root, padx=20, pady=20)
        main_frame.pack(fill=tk.BOTH, expand=True)
        
        # YouTube Link Input
        link_label = tk.Label(main_frame, text="Link YouTube:", font=("Arial", 11))
        link_label.pack(anchor=tk.W)
        
        self.link_entry = tk.Entry(main_frame, font=("Arial", 11), width=50)
        self.link_entry.pack(fill=tk.X, pady=(5, 15))
        self.link_entry.bind("<Return>", lambda e: self.start_download())
        
        # Format Selection
        format_frame = tk.Frame(main_frame)
        format_frame.pack(fill=tk.X, pady=(0, 15))
        
        format_label = tk.Label(format_frame, text="Format Audio:", font=("Arial", 11))
        format_label.pack(anchor=tk.W)
        
        self.format_var = tk.StringVar(value="m4a")
        
        format_options = tk.Frame(format_frame)
        format_options.pack(fill=tk.X, pady=5)
        
        tk.Radiobutton(
            format_options,
            text="M4A (Best Quality, compatible semua player)",
            variable=self.format_var,
            value="m4a",
            font=("Arial", 10)
        ).pack(anchor=tk.W)
        
        tk.Radiobutton(
            format_options,
            text="OPUS (High Quality, size kecil)",
            variable=self.format_var,
            value="opus",
            font=("Arial", 10)
        ).pack(anchor=tk.W)
        
        tk.Radiobutton(
            format_options,
            text="WebM (Good Quality)",
            variable=self.format_var,
            value="webm",
            font=("Arial", 10)
        ).pack(anchor=tk.W)
        
        # Download Location
        location_frame = tk.Frame(main_frame)
        location_frame.pack(fill=tk.X, pady=(0, 15))
        
        location_label = tk.Label(location_frame, text="Lokasi Download:", font=("Arial", 11))
        location_label.pack(anchor=tk.W)
        
        path_frame = tk.Frame(location_frame)
        path_frame.pack(fill=tk.X, pady=5)
        
        self.path_entry = tk.Entry(path_frame, font=("Arial", 10))
        self.path_entry.insert(0, self.download_path)
        self.path_entry.pack(side=tk.LEFT, fill=tk.X, expand=True)
        
        browse_btn = tk.Button(
            path_frame,
            text="Browse",
            command=self.browse_folder,
            font=("Arial", 10),
            bg="#f1f3f4",
            cursor="hand2"
        )
        browse_btn.pack(side=tk.LEFT, padx=(5, 0))
        
        # Download Button
        self.download_btn = tk.Button(
            main_frame,
            text="⬇ Download Audio",
            command=self.start_download,
            font=("Arial", 12, "bold"),
            bg="#1a73e8",
            fg="white",
            cursor="hand2",
            height=2
        )
        self.download_btn.pack(fill=tk.X, pady=(10, 15))
        
        # Progress Bar
        self.progress = ttk.Progressbar(main_frame, mode='indeterminate')
        self.progress.pack(fill=tk.X, pady=(0, 10))
        
        # Status Label
        self.status_label = tk.Label(
            main_frame,
            text="Masukkan link YouTube dan klik Download",
            font=("Arial", 10),
            fg="#5f6368",
            wraplength=550,
            justify=tk.LEFT
        )
        self.status_label.pack(anchor=tk.W)
        
        # Footer
        footer_label = tk.Label(
            main_frame,
            text="💡 Tip: Format M4A paling kompatibel, bisa diputar di semua device",
            font=("Arial", 9),
            fg="#999"
        )
        footer_label.pack(side=tk.BOTTOM, pady=(20, 0))
    
    def browse_folder(self):
        folder = filedialog.askdirectory()
        if folder:
            self.download_path = folder
            self.path_entry.delete(0, tk.END)
            self.path_entry.insert(0, folder)
    
    def start_download(self):
        url = self.link_entry.get().strip()
        
        if not url:
            messagebox.showwarning("Peringatan", "Silakan masukkan link YouTube!")
            return
        
        if not url.startswith(('https://www.youtube.com/', 'https://youtu.be/', 'https://m.youtube.com/')):
            messagebox.showwarning("Peringatan", "Link tidak valid! Pastikan menggunakan link YouTube.")
            return
        
        self.download_path = self.path_entry.get()
        
        # Jalankan download di thread terpisah
        thread = threading.Thread(target=self.download_audio, args=(url,))
        thread.daemon = True
        thread.start()
    
    def download_audio(self, url):
        self.download_btn.config(state=tk.DISABLED)
        self.progress.start(10)
        self.status_label.config(text="🔄 Mengambil informasi video...")
        
        try:
            format_choice = self.format_var.get()
            
            # Konfigurasi untuk download langsung tanpa convert
            if format_choice == "m4a":
                # Download M4A (AAC audio) - paling kompatibel
                format_selector = 'bestaudio[ext=m4a]/bestaudio'
                ext = 'm4a'
                quality_desc = "Best Quality (M4A/AAC)"
            elif format_choice == "opus":
                # Download OPUS - kualitas bagus, size kecil
                format_selector = 'bestaudio[ext=webm]'
                ext = 'opus'
                quality_desc = "High Quality (OPUS)"
            else:
                # Download WebM
                format_selector = 'bestaudio'
                ext = 'webm'
                quality_desc = "Good Quality (WebM)"
            
            ydl_opts = {
                'format': format_selector,
                'outtmpl': os.path.join(self.download_path, '%(title)s.%(ext)s'),
                'progress_hooks': [self.progress_hook],
                'quiet': False,
                'no_warnings': False,
                # Prefer free formats (no conversion needed)
                'prefer_free_formats': True,
            }
            
            # Khusus untuk OPUS, perlu post-processor untuk rename extension
            if format_choice == "opus":
                ydl_opts['postprocessors'] = [{
                    'key': 'FFmpegExtractAudio',
                    'preferredcodec': 'opus',
                }]
                # Tapi karena ga ada FFmpeg, file tetep .webm dengan codec opus
                # Jadi kita skip postprocessor dan biarkan .webm
                del ydl_opts['postprocessors']
                ext = 'webm'  # File akan jadi .webm (tapi isinya OPUS codec)
                quality_desc = "High Quality (WebM/OPUS)"
            
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                info = ydl.extract_info(url, download=False)
                title = info.get('title', 'Unknown')
                
                self.status_label.config(text=f"📥 Downloading: {title}")
                ydl.download([url])
            
            self.status_label.config(
                text=f"✅ Selesai! File tersimpan di: {self.download_path}",
                fg="green"
            )
            
            messagebox.showinfo(
                "Berhasil!",
                f"Download selesai!\n\n"
                f"File: {title}.{ext}\n"
                f"Quality: {quality_desc}\n"
                f"Lokasi: {self.download_path}\n\n"
                f"💡 File bisa langsung diputar di semua music player!"
            )
            
        except Exception as e:
            self.status_label.config(
                text=f"❌ Error: {str(e)}",
                fg="red"
            )
            messagebox.showerror("Error", f"Gagal download:\n{str(e)}")
        
        finally:
            self.progress.stop()
            self.download_btn.config(state=tk.NORMAL)
    
    def progress_hook(self, d):
        if d['status'] == 'downloading':
            percent = d.get('_percent_str', '0%')
            speed = d.get('_speed_str', 'N/A')
            self.status_label.config(
                text=f"📥 Downloading... {percent} | Speed: {speed}",
                fg="#1a73e8"
            )
        elif d['status'] == 'finished':
            self.status_label.config(
                text="✅ Download selesai!",
                fg="green"
            )


def main():
    root = tk.Tk()
    app = YouTubeMp3Downloader(root)
    root.mainloop()


if __name__ == "__main__":
    main()