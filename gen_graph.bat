code2flow %~dp0tests\tests_no_creds.py --output graphy.dot
dot -Tpng graphy.dot > out.png
start out.png