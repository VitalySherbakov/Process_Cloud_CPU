@echo off
title INSTALL PIP
set /p encoding=<"Encoding_CMD.txt"
echo ENCODING CMD: Windows Cyrulica (1251)/DOS (866)/UTF-8 (65001)
echo SELECT ENCODING: %encoding%
chcp %encoding%
set /p python=<"Path_Python.txt"
echo Path Python: %python%\python.exe
cmd /k "%python%\python.exe get-pip2.py & %python%\python.exe -m pip install --upgrade pip & echo ----------------------END PIP----------------------"
pause