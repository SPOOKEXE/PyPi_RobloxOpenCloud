@echo OFF

set /p "outputconsole=Output test functions to stout? (y/n): "
set /p "mode=Enable VSCode Mode? (y/n): "

set /p "id1=Enter Roblox Cookie: "
set /p "id2=Enter Roblox User Id: "
set /p "id3=Enter API Key: "
set /p "id4=Enter API Key Creator Id: "

IF /i "%outputconsole%" EQU "y" (
	pytest --capture=tee-sys %~dp0tests_creds.py --id1 %id1% --id2 %id2% --id3 %id3% --id4 %id4%
) ELSE (
	pytest %~dp0tests_creds.py --id1 %id1% --id2 %id2% --id3 %id3% --id4 %id4%
)

pause
