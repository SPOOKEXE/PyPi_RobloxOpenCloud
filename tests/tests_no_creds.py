'''
This file tests for everything not relating to
credential-required activities.
'''

ENABLE_VSCODE_MODE = True

import pytest

from os import system
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

def test_for_rbxmk_version( ) -> None:
	rbxmk_filepath = roblox_cloud_api.rbxmk_executable_path()
	print('Running rbxmk with version: ')
	system( rbxmk_filepath + ' version' )

if __name__ == '__main__':
	test_for_rbxmk_version( )
