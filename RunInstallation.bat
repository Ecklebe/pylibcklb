@echo off
rem Tobias Ecklebe development.ecklebe@outlook.de

echo Install pylibcklb into the python site-packages. 
echo You have to call this script in most cases as administrator!
echo -------------------------------------------------------------
echo.

rem code for admin access comes from https://stackoverflow.com/a/26676983

>nul 2>&1 "%SYSTEMROOT%\system32\cacls.exe" "%SYSTEMROOT%\system32\config\system"

IF '%errorlevel%' NEQ '0' (
    echo Requesting Admin access...
    goto goUAC 
) ELSE (
	goto goADMIN
)

:goUAC
    echo Set UAC = CreateObject^("Shell.Application"^) > "%temp%\getadmin.vbs"
    set params = %*:"=""
    echo UAC.ShellExecute "cmd.exe", "/c %~s0 %params%", "", "runas", 1 >> "%temp%\getadmin.vbs"
    "%temp%\getadmin.vbs"
    del "%temp%\getadmin.vbs"
    exit /B

:goADMIN
    pushd "%CD%"
    CD /D "%~dp0"

python.exe setup.py install