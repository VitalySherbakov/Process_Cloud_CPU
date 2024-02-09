@echo off
title Run Script Vitaly Sherbakov
:start
title Libs Install
set /p pythonpath=<"Path_Python.txt"
echo PYTHON: %pythonpath%\python
%pythonpath%\Scripts\auto-py-to-exe
pause
goto start
pause