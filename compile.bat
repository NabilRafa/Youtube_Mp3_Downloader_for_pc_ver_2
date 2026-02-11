@echo off

pyinstaller ^
--onefile ^
--noconsole ^
--icon=icon.ico ^
--distpath Compiled ^
--workpath Compiled\BuildTemp ^
"Quick_MP3.py"

rmdir /s /q Compiled\BuildTemp

echo.
echo Build selesai. Tekan tombol apa saja untuk keluar...
pause