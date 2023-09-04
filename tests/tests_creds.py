'''
This file tests for everything relating to
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

def test_for_ids( id1 : str, id2 : str, id3 : str, id4 : str ) -> None:
	assert id1, "ID is unavailable - did you run the test with --id1?"
	assert id2, "ID is unavailable - did you run the test with --id2?"
	assert id3, "ID is unavailable - did you run the test with --id3?"
	assert id4, "ID is unavailable - did you run the test with --id4?"
	print(id1, id2, id3, id4)
