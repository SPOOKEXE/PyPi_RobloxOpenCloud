
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
	API_URLS
)

class KeyAPI:

	@staticmethod
	def is_api_key_valid( account : USER_ACCOUNT ) -> bool:
		pass # TODO
