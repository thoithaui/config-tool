@echo off
:: BatchGotAdmin
::-------------------------------------
REM  --> Check for permissions
>nul 2>&1 "%SYSTEMROOT%\system32\cacls.exe" "%SYSTEMROOT%\system32\config\system"

REM --> If error flag set, we do not have admin.
if '%errorlevel%' NEQ '0' (
    echo Requesting administrative privileges...
    goto UACPrompt
) else ( goto gotAdmin )

:UACPrompt
    echo Set UAC = CreateObject^("Shell.Application"^) > "%temp%\getadmin.vbs"
    set params = %*:"="
    echo UAC.ShellExecute "cmd.exe", "/c %~s0 %params%", "", "runas", 1 >> "%temp%\getadmin.vbs"

    "%temp%\getadmin.vbs"
    del "%temp%\getadmin.vbs"
    exit /B

:gotAdmin
    pushd "%CD%"
    CD /D "%~dp0"
::--------------------------------------
cd D:\Program Files\logstash-8.7.1
.\bin\nssm.exe install logstash "C:\logstash-8.7.1\bin\logstash.bat"
.\bin\nssm.exe set logstash AppDirectory "C:\logstash-8.7.1\bin"
.\bin\nssm.exe set logstash AppDirectory "logstash"
.\bin\nssm.exe set logstash Start SERVICE_AUTO_START
.\bin\nssm.exe set logstash DependOnService elasticsearch-service-x64