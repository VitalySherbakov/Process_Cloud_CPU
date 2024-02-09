@echo off
title Terminal Project
set /p encoding=<"Encoding_CMD.txt"
echo ENCODING CMD: Windows Cyrulica (1251)/DOS (866)/UTF-8 (65001)
echo SELECT ENCODING: %encoding%
chcp %encoding%
set /p project=<"Path_Project_Dir.txt"
set /p python=<"Path_Python.txt"
echo Path Python: %python%\python.exe
echo Path Project: %project%
cd /d "%project%"
echo %cd%
cmd /k "venv\Scripts\activate & echo -------------------------------------- & pip freeze & echo -------------------------------------- & echo Command Run: pip install & echo Command Run: python "
pause