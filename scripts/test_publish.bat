echo TEST PUBLISHING TO https://test.pypi.org/manage/projects/
twine upload -r testpypi %~dp0../dist/*
pause