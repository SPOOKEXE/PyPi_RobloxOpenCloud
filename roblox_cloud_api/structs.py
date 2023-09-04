
from typing import Protocol
from enum import Enum
from attr import dataclass

class API_URLS(Enum):
	pass

class ASSET_TYPES(Enum):
	Model = "Model"
	Decal = "Decal"
	Audio = "Audio"

class OPERATION_STATUS(Enum):
	Success = 1
	Moderated = 2
	Waiting = 3
	Unavailable = 4
	Exception = 5

@dataclass
class ASSET_INSTANCE:
	Name : str = None
	AssetType : str = None
	Filepath : str = None

class API_KEY_PROTOCOL(Protocol):
	def get_api_key( self ) -> str:
		...

	def get_creator_id( self ) -> str:
		...

class USER_ACCOUNT_PROTOCOL(Protocol):
	def get_roblox_cookie( self ) -> str:
		...

	def get_user_id( self ) -> str:
		...
