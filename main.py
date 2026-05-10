@echo off
setlocal enabledelayedexpansion

set "art1=                                        _        _    ____  ____  "
set "art2=                                       | |      / \  |  _ \|  _ \ "
set "art3=                                       | |     / _ \ | |_) | |_) |"
set "art4=                                       | |___ / ___ \|  _ <|  __/ "
set "art5=                                       |_____/_/   \_\_| \_\_|    "
set "art6=         [1] start LARP"
set "art7=         [2] FastFetch"
set "art8=         [3] ip grabber"

:menu
cls
echo !art1!
echo !art2!
echo !art3!
echo !art4!
echo !art5!
echo !art6!
echo !art7!
echo !art8!
echo.
set /p input=Enter your choice: 

for /f "tokens=1-3" %%a in ("%input%") do (
  set "opt=%%a"
  set "col1=%%b"
  set "col2=%%c"
)

if "%opt%"=="1" (
  start cmd /k "@echo off & setlocal enabledelayedexpansion & for /f %%a in ('echo prompt $E ^| cmd') do set "ESC=%%a" & set "code=!ESC![40;32m101010101001101010101010101000001101001!ESC![0m" & :loop & cls & for /l %%i in (1,1,25) do echo !code! & goto loop"
)

if "%opt%"=="2" (
  echo.
  echo ================= SYSTEM INFO =================
  echo OS: %OS% %PROCESSOR_ARCHITECTURE%
  for /f "tokens=2 delims==" %%i in ('wmic os get Caption /value') do echo Full OS: %%i
  for /f "tokens=2 delims==" %%i in ('wmic cpu get Name /value') do echo CPU: %%i
  for /f "tokens=2 delims==" %%i in ('wmic computersystem get TotalPhysicalMemory /value') do set /a mem=%%i/1024/1024 & echo RAM: !mem! MB
  for /f "tokens=2 delims==" %%i in ('wmic diskdrive get Size /value') do set /a disk=%%i/1024/1024/1024 & echo Disk: !disk! GB
  echo ===============================================
  echo.
  timeout /t 5 >nul
)

if "%opt%"=="3" (
  echo Grabbing IP...
  ipconfig | findstr /i "ipv4"
  timeout /t 2 >nul
)

goto menu

pause