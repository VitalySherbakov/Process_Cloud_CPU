@echo off
title AUTO RUN Project
set /p encoding=<"Encoding_CMD.txt"
echo ENCODING CMD: Windows Cyrulica (1251)/DOS (866)/UTF-8 (65001)
echo SELECT ENCODING: %encoding%
chcp %encoding%
set /p project=<"Path_Project_Dir.txt"
set /p python=<"Path_Python.txt"
set /p pythonrun=<"Path_Python_Run.txt"
echo Path Python: %python%\python.exe
echo Path Project: %project%
echo Path Run: %pythonrun%.py
cd /d "%project%"
echo %cd%
cmd /k "venv\Scripts\activate & python.exe %pythonrun%.py & echo Command Run: python.exe %pythonrun%.py"
pause