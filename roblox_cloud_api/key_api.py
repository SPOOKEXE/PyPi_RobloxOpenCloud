
from functools import (
	partial,
	lru_cache,
	cache
)

from .common import (
	ASSET_TYPES,
	OPERATION_STATUS,
	ASSET_FILE,
	API_KEY,
	USER_ACCOUNT,
	API_URLS,
	_RequestWrapper
)

class KeyAPI:

	@staticmethod
	def is_api_key_valid( api_key : API_KEY ) -> bool:
		'''
		**Unavailable at the moment - waiting for response from roblox staff to implement this properly

		Will automatically return True when called.**
		''' # TODO: fix
		return True
