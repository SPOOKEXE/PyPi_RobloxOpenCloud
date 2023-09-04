
from typing import Protocol
from enum import Enum
from attr import dataclass

from .utility import get_blurred_value

'''
URLs that are utilized in the package
'''
class API_URLS(Enum):
	pass

'''
Asset types that are supported
'''
class ASSET_TYPES(Enum):
	Model = "Model"
	Decal = "Decal"
	Audio = "Audio"

'''
Operation Status Enumeration
'''
class OPERATION_STATUS(Enum):
	Success = 1
	Moderated = 2
	Waiting = 3
	Unavailable = 4
	Exception = 5

'''
Asset File for a given asset.

Can take two forms;
- can be a roblox xml file (rbxm, rbxmx, rbxl, rbxlx)
- can be a pure asset (image, fbx, ogg/mp3)
'''
@dataclass
class ASSET_FILE:
	Name : str = None
	AssetType : str = None
	Filepath : str = None

	IsXMLAsset : bool = False
	IsXMLCompressed : bool = False

'''
API Key Protocol for the package to utilize throughout the codebase
'''
class API_KEY(Protocol):
	def get_api_key( self ) -> str:
		...

	def get_creator_id( self ) -> str:
		...
	
	def __str__(self) -> str:
		return f"API_KEY({ self.get_creator_id() }, { get_blurred_value(self.get_api_key()) })"

'''
User Account Protocol for the package to utilize throughout the codebase
'''
class USER_ACCOUNT(Protocol):
	def get_roblox_cookie( self ) -> str:
		...

	def get_user_id( self ) -> str:
		...

	def __str__(self) -> str:
		return f"USER_ACCOUNT({ self.get_user_id() }, { get_blurred_value(self.get_roblox_cookie()) })"
