@echo OFF
code2flow %~dp0..\tests\tests_no_creds.py --output %~dp0graphy.dot
dot -Tpng %~dp0graphy.dot > %~dp0out.png
start %~dp0out.png
pause