
from typing import Protocol
from enum import Enum
from attr import dataclass
from requests import Response, Session

from .utility import get_blurred_value

'''
URLs that are utilized in the package
'''
class API_URLS:

	MESSAGING_SERVICE_API = 'https://apis.roblox.com/messaging-service/v1/universes/{}/topics/{}'
	CLOUD_API_KEY_URL = 'https://apis.roblox.com/cloud-authentication/v1/apiKey'
	ACCOUNT_AUTHENTICATED_URL = 'https://users.roblox.com/v1/users/authenticated'
	UNIVERSE_VERSIONS_API = 'https://apis.roblox.com/universes/v1/{}/places/{}/versions'
	STANDARD_DATASTORE_URL = 'https://apis.roblox.com/datastores/v1/universes/{}/standard-datastores'
	OPERATIONS_STATUS_API = "https://apis.roblox.com/assets/v1/operations/{}"


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
@dataclass
class API_KEY:
	api_key : str = None
	creator_id : str = None

	def append_auth( self, session : Session ) -> None:
		session.headers["x-api-key"] = self.api_key

	def __str__(self) -> str:
		return f"API_KEY({ self.creator_id }, { get_blurred_value(self.api_key) })"

'''
User Account Protocol for the package to utilize throughout the codebase
'''
@dataclass
class USER_ACCOUNT:
	cookie : str = None
	user_id : str = None

	def append_auth( self, session : Session ) -> None:
		session.cookies.set('.ROBLOSECURITY', self.cookie)

	def __str__(self) -> str:
		return f"USER_ACCOUNT({ self.user_id }, { get_blurred_value(self.cookie) })"
