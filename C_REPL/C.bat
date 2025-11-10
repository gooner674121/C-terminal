@echo off
cd /d "%~dp0"

REM ✅ Add GCC to PATH for this session
set PATH=%PATH%;C:\MinGW\bin

REM ✅ Run your Python terminal
python C_terminal.py

pause
