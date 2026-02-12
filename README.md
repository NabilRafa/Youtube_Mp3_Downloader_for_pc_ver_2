# Youtube_Mp3_Downloader_for_pc_ver_2

Disclaimer : File ini tidak ada virus apapun, kalau windows mendeteksi sebagai virus cukup matikan antivirus atau pakai versi 'Portable'

# 📖 Indonesia (Scroll for English Ver)

---

# 🎵 YouTube MP3 Downloader (GUI)

Simple desktop app untuk download dan convert video YouTube ke MP3 menggunakan Python + Tkinter + yt-dlp.

## ✨ Features

* GUI sederhana dan ringan
* Download audio kualitas terbaik
* Auto convert ke MP3 (192kbps)
* Bisa pilih folder download
* Tidak bikin UI freeze (pakai threading)

---

## ▶️ How to run?

```bash
python main.py
```

atau

Cukup klik file .exe nya :)

---

## ▶️ Cara pakai?

### 1️⃣ Download Aplikasi

Download file:

```
Quick_Audio.rar
```

### 2️⃣ Jalankan Aplikasi

Double click file `.exe`.

Jika muncul peringatan Windows:

* Klik **More Info**
* Klik **Run Anyway**

Atau matikan antivirus terlebih dulu

### 3️⃣ Download Audio

1. Paste link YouTube
2. Pilih lokasi download (opsional)
3. Klik **Download**
4. Tunggu sampai selesai

File MP3 akan otomatis tersimpan di folder pilihan Anda.

---

## 📁 Lokasi Default

Jika tidak diubah, file akan tersimpan di:

```
Downloads\YouTube_Audio
```

---


## FOR DEVELOPMENT ONLY

---

## 🛠 Requirements

* Python 3.10+
* yt-dlp
* FFmpeg (WAJIB untuk convert ke MP3)

---

## 📦 Installation

### 1️⃣ Install dependency

```bash
pip install yt-dlp
```

### 2️⃣ Install FFmpeg

Download FFmpeg Windows build:
[https://www.gyan.dev/ffmpeg/builds/](https://www.gyan.dev/ffmpeg/builds/)

Tambahkan folder `bin` ke Environment Variables (PATH).

Cek instalasi:

```bash
ffmpeg -version
```

---

## 📁 Default Output Location

```
Downloads/YouTube_MP3
```

Bisa diganti langsung dari aplikasi.

---

## ⚠ Notes

* Pastikan koneksi internet stabil
* Jika error, update yt-dlp:

```bash
pip install -U yt-dlp
```

---

## 📜 Disclaimer

Gunakan aplikasi ini hanya untuk konten yang memiliki izin untuk diunduh.

---

# 📖 English

---

# 🎵 YouTube MP3 Downloader (GUI)

A simple desktop application to download and convert YouTube videos to MP3 using Python + Tkinter + yt-dlp.

## ✨ Features

* Simple and lightweight GUI
* Downloads best available audio quality
* Automatically converts to MP3 (192kbps)
* Customizable download folder
* Non-blocking UI (uses threading)

---

## 🛠 Requirements

* Python 3.10+
* yt-dlp
* FFmpeg (REQUIRED for MP3 conversion)

---

## 📦 Installation

### 1️⃣ Install dependency

```bash
pip install yt-dlp
```

### 2️⃣ Install FFmpeg

Download the Windows build of FFmpeg:
[https://www.gyan.dev/ffmpeg/builds/](https://www.gyan.dev/ffmpeg/builds/)

Add the `bin` folder to your Environment Variables (PATH).

Verify installation:

```bash
ffmpeg -version
```

---

## ▶️ Run Application

```bash
python main.py
```

---

## 📁 Default Output Location

```
Downloads/YouTube_MP3
```

You can change it directly from the application.

---

## ⚠ Notes

* Make sure your internet connection is stable
* If you encounter errors, update yt-dlp:

```bash
pip install -U yt-dlp
```

---

## 📜 Disclaimer

Use this application only for content that you have permission to download.

---

