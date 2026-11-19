@echo off
setlocal

if "%~1"=="" (
    echo [!] Usage: grep.bat "search_term" [file_path]
    goto :end
)

set "search_term=%~1"
set "file_path=%~2"

if "%file_path%"=="" (
    findstr /i /n "%search_term%"
    echo.
) else (
    set "file_path=%file_path:"=%"

    if not exist "%file_path%" (
        echo [!] הקובץ אינו קיים: "%file_path%"
        goto :end
    )

    findstr /i /n "%search_term%" "%file_path%"
    echo.
)

:end