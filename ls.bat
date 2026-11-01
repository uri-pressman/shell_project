@echo off
echo List of files in: %1

REM Run dir directly on the path passed via %1
dir /b /a-d %1

