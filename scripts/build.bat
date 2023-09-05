cd %~dp0../
@RD /S /Q dist
@RD /S /Q roblox_cloud_api.egg-info
py -m build
pause