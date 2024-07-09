

:: This file installs node.js.






@echo off

powershell -Command Write-Host "Support tool created by By A Dev" -ForegroundColor Red
echo.

cd /d %userprofile%\Desktop

curl -o node-v20.15.0-x64.msi "https://nodejs.org/dist/v20.15.0/node-v20.15.0-x64.msi"

start /wait node-v20.15.0-x64.msi

del node-v20.15.0-x64.msi

exit
