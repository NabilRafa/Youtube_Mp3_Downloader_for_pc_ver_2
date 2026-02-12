@echo off

pyinstaller ^
--onedir ^
--add-binary "ffmpeg.exe;." ^
--add-binary "ffprobe.exe;." ^
--noconsole ^
--icon=icon.ico ^
--distpath Build ^
--workpath Build\BuildTemp ^
--name "Quick_Audio" ^
main.py

rmdir /s /q Build\BuildTemp

echo.
echo Build selesai. Tekan tombol apa saja untuk keluar...
pause