import json
import os
from typing import Callable

from requests import Session

'''
Returns the passed value except only the first n characters are
shown and rest are asterisks.
'''
def get_blurred_value( value : str, count=6 ) -> str:
	assert type(value) == str, "Passed parameter must be a string."
	return value[:count] + ("*" * (len(value) - count))

'''
Attempt to load a json file, returns a dictionary (the json)
or None if failed.
'''
def read_json( filepath : str ) -> dict | None:
	try:
		with open(filepath, "r") as file:
			return json.loads( file.read() )
	except Exception as e:
		print(e)
	return None

'''
Move all files within the root directory tree to the root directory;
Searches all sub-folders of the root directory for files.
'''
def move_descendant_files_to_root( directory : str ) -> None:
	for root, _, files in os.walk(directory):
		for file in files:
			filepath = os.path.join( root, file )
			new_path = os.path.join( directory, os.path.basename(file) )
			try:
				os.rename( filepath, new_path )
			except:
				pass
