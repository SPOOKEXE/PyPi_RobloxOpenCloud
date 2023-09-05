
from setuptools import find_packages, setup
from os import path as os_path

FILE_DIRECTORY = os_path.abspath(os_path.dirname(__file__))

VERSION = "0.0.10"

with open( os_path.join(FILE_DIRECTORY, "README.md"), "r") as f:
	long_description = f.read()

setup(
	name="roblox_cloud_api",
	version=VERSION,
	description="Roblox API for open cloud and assets.",
	long_description=long_description,
	long_description_content_type="text/markdown",
	packages=find_packages(),
	url="https://github.com/SPOOKEXE/PyPi_RobloxOpenCloud",
	author="SPOOK_EXE (Declan)",
	license="MIT",
	classifiers=[
		"License :: OSI Approved :: MIT License",
		"Intended Audience :: Developers",
		"Programming Language :: Python :: 3 :: Only",
		"Operating System :: Microsoft :: Windows",
		"Operating System :: Unix",
		"Operating System :: MacOS :: MacOS X",
		"Development Status :: 2 - Pre-Alpha"
	],
	keywords=['roblox', 'open-cloud', 'roblox open cloud', 'open cloud', 'roblox opencloud'],
	install_requires=['requests', 'pytest']
)
