@echo off
set "file_path=%~1"
set "temp_hex=%TEMP%\temp_hex_dump.txt"

echo Checking file: "%file_path%"

if exist "%file_path%" (
    echo Printing hex dump for: "%file_path%"

    REM יוצרים את הקובץ הזמני בתיקיית ה-TEMP הבטוחה
    certutil -encodehex "%file_path%" "%temp_hex%" 1 >nul

    REM מציגים את התוכן
    type "%temp_hex%"

    REM מוחקים את הקובץ הזמני בסיום
    del "%temp_hex%"
) else (
    echo הקובץ אינו קיים.
)

