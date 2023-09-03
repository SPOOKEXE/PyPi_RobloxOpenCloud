echo LIVE PUBLISHING TO https://pypi.org/manage/projects/
twine upload -r pypi %~dp0../dist/*
pause