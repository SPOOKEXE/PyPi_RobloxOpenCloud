@echo OFF

set /p "outputconsole=Output test functions to stout? (y/n): "

IF /i "%outputconsole%" EQU "y" (
	pytest --capture=tee-sys %~dp0tests_no_creds.py
) ELSE (
	pytest %~dp0tests_no_creds.py
)

pause
