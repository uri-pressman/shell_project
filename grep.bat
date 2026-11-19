@echo off
setlocal

if "%~1"=="" (
    echo [!] Usage: grep.bat "search_term" [file_path]
    goto :end
)

set "search_term=%~1"
set "file_path=%~2"

if "%file_path%"=="" (
    :: קריאה מ-stdin (למשל בעבודה עם pipe)
    findstr /i /n "%search_term%"
) else (
    :: ניקוי מרכאות
    set "file_path=%file_path:"=%"

    if not exist "%file_path%" (
        echo [!] הקובץ אינו קיים: "%file_path%"
        goto :end
    )

    :: קריאה מתוך הקובץ
    findstr /i /n "%search_term%" "%file_path%"
)

:end