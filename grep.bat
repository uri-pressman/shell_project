@echo off
setlocal

:: בדיקה אם המשתמש סיפק מילת חיפוש ונתיב לקובץ
if "%~1"=="" (
    echo [!] Usage: mygrep.bat "fd" "C:\Users\talmid\Downloads\fdfdff\fdfdfd.txt"
    goto :end
)
if "%~2"=="" (
    echo [!] Error: Please provide a file path.
    goto :end
)

set "search_term=%~1"
set "file_path=%~2"

:: ניקוי מרכאות מיותרות אם ישנן
set "file_path=%file_path:"=%"

if not exist "%file_path%" (
    echo [!] הקובץ אינו קיים: "%file_path%"
    goto :end
)

echo Searching for "%search_term%" in: "%file_path%"
echo --------------------------------------------------

:: שימוש ב-findstr (ה-"grep" של ווינדוס)
:: /i = התעלם מאותיות גדולות/קטנות (Case-insensitive, מקביל ל-grep -i)
:: /n = הצג מספרי שורות (Line numbers, מקביל ל-grep -n)
findstr /i /n "%search_term%" "%file_path%"

:end
pause