'''
This file tests for everything not relating to
credential-required activities.
'''

ENABLE_VSCODE_MODE = True

import pytest

from os import path as os_path
from sys import path as sys_path

if ENABLE_VSCODE_MODE:
	FILE_DIRECTORY = os_path.dirname(os_path.realpath(__file__))
	sys_path.insert( 0, os_path.join( FILE_DIRECTORY, ".." ) )

import roblox_cloud_api

if ENABLE_VSCODE_MODE:
	sys_path.pop(0)

######## TESTS ########

def test_running( ) -> None:
	print('pytest is working.')

def test_1( ) -> None:
	asset = roblox_cloud_api.ASSET_INSTANCE("Hello!", roblox_cloud_api.ASSET_TYPES.Model, "C:")
	print(asset)
