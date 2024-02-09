@echo off
title Create Project
set /p encoding=<"Encoding_CMD.txt"
echo ENCODING CMD: Windows Cyrulica (1251)/DOS (866)/UTF-8 (65001)
echo SELECT ENCODING: %encoding%
chcp %encoding%
set /p project=<"Path_Project_Dir.txt"
set /p python=<"Path_Python.txt"
echo Path Python: %python%\python.exe
echo Path Project: %project%
md "%project%"
copy /y "requirements.txt" "%project%\requirements.txt"
cd /d "%project%"
echo %cd%
cmd /k "%python%\python.exe -m virtualenv venv & venv\Scripts\activate & python.exe -m pip install --upgrade pip & python.exe -m pip install -r requirements.txt & del /s/q requirements.txt & echo -------------Project %project% End-------------"
pause