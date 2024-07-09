

: : Download this file and run as admin









@echo off

net session >nul 2>&1
if %errorlevel% neq 0 (
    echo You must run this script as Administrator.
    pause
    exit /b 1
)

powershell.exe -Command "$action = New-ScheduledTaskAction -Execute '"%userprofile%\Desktop\install_wave.bat"'; $trigger = New-ScheduledTaskTrigger -AtLogon; $settings = New-ScheduledTaskSettingsSet -AllowStartIfOnBatteries; $taskName = 'InstallWave'; $taskDescription = 'Runs the bat file that installs wave'; Register-ScheduledTask -Action $action -Trigger $trigger -TaskName $taskName -Description $taskDescription -Settings $settings -RunLevel Highest -Force"

powershell -Command Write-Host "All in one support tool created by mi_aio" -ForegroundColor Red
echo.
powershell -Command "Start-Process PowerShell -ArgumentList 'Add-MpPreference -ExclusionPath \"%localappdata%\Wave\"' -Verb RunAs"

echo %localappdata%\Wave has been added to exclusions.
echo.

if exist "%localappdata%\Wave" (
    echo Deleting Wave in %localappdata%...
    echo.
    rmdir /S /Q "%localappdata%\Wave"
    echo Wave has been deleted successfully.
    echo.
) else (
    echo Wave does not exist in %localappdata%.
    echo.
)

if exist "%temp%\Injector.exe" (
    echo Deleting Injector.exe in %temp%...
    echo.
    del /F /Q "%temp%\Injector.exe"
    echo Injector.exe deleted successfully.
    echo.
) else (
    echo Injector.exe does not exist in %temp%.
    echo.
)

if exist "%temp%\Wave.dll" (
    echo Deleting Wave.dll in %temp%...
    echo.
    del /F /Q "%temp%\Wave.dll"
    echo Wave.dll deleted successfully.
    echo.
) else (
    echo Wave.dll does not exist in %temp%.
    echo.
)

@echo off
cd /d %userprofile%\Desktop

echo Downloading and extracting Visual-C-Runtimes-All-in-One-May-2024.zip...
echo.



curl -o Visual-C-Runtimes-All-in-One-May-2024.zip "https://fs5.fastupload.io/e1f6020d3eeda369/Visual-C-Runtimes-All-in-One-May-2024.zip?download_token=991adb999072f244c9b1d3827e009b99eac488323506d56313be78443fde2730"
mkdir VisualC++
powershell Expand-Archive -Path Visual-C-Runtimes-All-in-One-May-2024.zip -DestinationPath VisualC++
del Visual-C-Runtimes-All-in-One-May-2024.zip

echo Installing VisualC++ components...
echo.
start "install" /wait cmd /c "cd VisualC++ && call install_all.bat"

echo Downloading Node.js installer...
echo.
curl -o node-v20.15.0-x64.msi "https://nodejs.org/dist/v20.15.0/node-v20.15.0-x64.msi"

echo Installing Node.js...
echo.
start /wait node-v20.15.0-x64.msi
del node-v20.15.0-x64.msi

echo Downloading ASP.NET Core 6.0.31 Windows x64 installer...
echo.
curl -o aspnetcore-runtime-6.0.31-win-x64.exe "https://download.visualstudio.microsoft.com/download/pr/29b7b141-bb4d-462b-8b55-6a1e4a610add/c38161439a048506b923b47fd50d21cc/aspnetcore-runtime-6.0.31-win-x64.exe"

echo Installing ASP.NET Core...
echo.
start /wait aspnetcore-runtime-6.0.31-win-x64.exe
del aspnetcore-runtime-6.0.31-win-x64.exe
rmdir /S /Q "VisualC++"
cls

echo All installations complete.
echo.

echo Setting up WaveInstaller to run after restart...
echo.
set install_bat="%userprofile%\Desktop\install_wave.bat"
(
echo @echo off
echo powershell -Command Write-Host "Support tool created by mi_aio" -ForegroundColor Red
echo schtasks /delete /tn "InstallWave" /f
echo echo.
echo cd /d %%userprofile%%\Desktop
echo curl -o WaveInstaller.exe "https://cdn.getwave.gg/WaveInstaller.exe"
echo start /wait WaveInstaller.exe
echo del WaveInstaller.exe
echo del install_wave.bat
echo exit
) > %install_bat%

echo Setup complete. Please restart your PC to finish the installation.
echo Press any key to restart the computer...
pause >nul
shutdown /r /t 0
pause

