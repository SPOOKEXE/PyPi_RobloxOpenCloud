cd %~dp0../
@RD /S /Q dist
py -m build
@RD /S /Q roblox_cloud_api.egg-info
pause