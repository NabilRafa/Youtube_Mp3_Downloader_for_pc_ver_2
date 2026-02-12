@echo off

pyinstaller ^
--onefile ^
--add-binary "ffmpeg.exe;." ^
--add-binary "ffprobe.exe;." ^
--noconsole ^
--icon=icon.ico ^
--distpath Compiled ^
--workpath Compiled\BuildTemp ^
--name "Quick_Audio" ^
"main.py"

rmdir /s /q Compiled\BuildTemp

echo.
echo Build selesai. Tekan tombol apa saja untuk keluar...
pause