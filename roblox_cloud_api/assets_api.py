
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

class AssetsDeliveryAPI:

	@staticmethod
	def download_asset( owner : USER_ACCOUNT | API_KEY, asset_id : int ) -> ASSET_FILE | None:
		pass # TODO

class AssetFileAPI:

	@staticmethod
	def compress_asset( asset : ASSET_FILE ) -> None:
		assert not asset.IsXMLCompressed, "Asset is already compressed!"

		pass # TODO

	@staticmethod
	def decompress_asset( asset : ASSET_FILE ) -> None:
		assert asset.IsXMLCompressed, "Asset is already compressed!"

		pass # TODO
