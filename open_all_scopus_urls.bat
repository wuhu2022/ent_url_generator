@echo off
echo Opening all ORCID URLs...
echo This will open lots of browser tabs - make sure your browser can handle this!

pause

for /f "delims=" %%i in (scopus_search_urls.txt) do (
    start "" "%%i"
    timeout /t 1 /nobreak >nul
)

echo All URLs have been opened!
pause
