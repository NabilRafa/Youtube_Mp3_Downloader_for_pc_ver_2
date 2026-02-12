@echo off

pyinstaller ^
--onedir ^
--noconsole ^
--icon=icon.ico ^
--distpath Compiled ^
--workpath Compiled\BuildTemp ^
--name Quick_MP3"
"main.py"

rmdir /s /q Build\BuildTemp

echo.
echo Build selesai. Tekan tombol apa saja untuk keluar...
pause