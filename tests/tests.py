
import pytest
import roblox_cloud_api

def test_running( ) -> None:
	print('pytest is working.')

def test_cloud_api( ) -> None:
	roblox_cloud_api.TestClass.output()
