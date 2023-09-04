'''
rbxmk application wrapper, coded by Anaminus as is available at:
https://github.com/Anaminus/rbxmk
'''

import platform
import sys
import os
import requests
import shutil
import tempfile

from functools import cache

FILE_DIRECTORY = os.path.abspath(os.path.dirname(__file__))

RBXMK_VERSION = "0.9.1"
RBXMK_URLS = {
	"rbxmk_linux_x64" : f"https://github.com/Anaminus/rbxmk/releases/download/v{RBXMK_VERSION}/rbxmk-v{RBXMK_VERSION}-linux-amd64.zip",
	"rbxmk_linux_x32" : f"https://github.com/Anaminus/rbxmk/releases/download/v{RBXMK_VERSION}/rbxmk-v{RBXMK_VERSION}-linux-386.zip",
	
	"rbxmk_windows_x64.exe" : f"https://github.com/Anaminus/rbxmk/releases/download/v{RBXMK_VERSION}/rbxmk-v{RBXMK_VERSION}-windows-amd64.zip",
	"rbxmk_windows_x32.exe" : f"https://github.com/Anaminus/rbxmk/releases/download/v{RBXMK_VERSION}/rbxmk-v{RBXMK_VERSION}-windows-386.zip",

	"rbxmk_macOS" : f"https://github.com/Anaminus/rbxmk/releases/download/v{RBXMK_VERSION}/rbxmk-v{RBXMK_VERSION}-darwin-amd64.zip"
}

@cache
def determine_rbxmk_platform() -> str | None:
	p = platform.system()
	is_64bits = sys.maxsize > (2**32)
	if p == "Linux": # Linux
		return is_64bits and "rbxmk_linux_x64" or "rbxmk_linux_x32"
	elif p == "Darwin": # MacOS
		return "rbxmk_macOS"
	elif p == "Windows": # Windows
		return (is_64bits and "rbxmk_windows_x64" or "rbxmk_windows_x32") + ".exe"
	return None

def download_rbxmk( file_url : str, filepath : str ) -> bool:
	url_filename = os.path.basename(file_url)
	temp_filepath = os.path.join( tempfile.gettempdir(), url_filename )

	print(f"Downloading rbxmk from {file_url}")

	# download the zip file if not already downloade into the temporary folder
	if not os.path.exists( temp_filepath ):
		try:
			r = requests.get( file_url, stream=True )
			with open(temp_filepath, "wb") as file:
				file.write(r.content)
		except Exception as e:
			print("Failed to download from GitHub: ", e, f"@ {file_url}")
			return False

	# extract the rbxmk out of the zip file from the temporary folder
	try:
		dirname = os.path.splitext(url_filename)[0]
		shutil.unpack_archive(temp_filepath, dirname)
		os.rename( os.path.join(dirname, os.listdir(dirname)[0]), filepath )
		shutil.rmtree( dirname, ignore_errors=True)
	except Exception as e:
		print("Failed to extract rbxmk from the zip file: ", e, f"@ {temp_filepath}")
		return False
	
	print("Successfully downloaded and extracted - continuing.")
	return True

def rbxmk_executable_path() -> str:
	filename = determine_rbxmk_platform()
	if filename == None:
		raise Exception("Unknown Platform - cannot run rbxmk. Supported platforms are Windows, MacOS, and Linux (x32 and x64).")

	filepath = os.path.join( FILE_DIRECTORY, filename )
	if os.path.exists( filepath ):
		return filepath

	print("rbxmk application was not found, downloading it from the rbxmk github.")
	if not filename in RBXMK_URLS.keys():
		raise Exception("Unknown Executable - cannot find the download url to the executable.")
	if not download_rbxmk( RBXMK_URLS[filename], filepath ):
		raise Exception("Download Failed - could not download the rbxmk application.")
	return filepath