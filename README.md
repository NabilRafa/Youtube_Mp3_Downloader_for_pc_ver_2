# Youtube_Mp3_Downloader_for_pc_ver_2

## 📜 Disclaimer : File ini tidak mengandung virus apapun, kalau windows mendeteksi sebagai virus cukup matikan antivirus atau pakai versi 'Portable'.

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

# 📖 English

---

W.I.P

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
