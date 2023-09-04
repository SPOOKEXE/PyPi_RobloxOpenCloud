
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

class OpenCloudAPI:
	
	class MessagingService:

		@staticmethod
		def publish_async(  ) -> None:
			pass # TODO

	class Operations:

		@staticmethod
		def get_operation_id_status(  ):
			pass # TODO
		@staticmethod
		def bulk_await_operations_completion( ):
			pass # TODO

	class Assets:

		@staticmethod
		def upload_and_return_operation_id(  ):
			pass # TODO

		@staticmethod
		def bulk_upload_and_return_operation_ids( ):
			pass # TODO

		@staticmethod
		def bulk_upload_assets():
			pass # TODO

	class DataStores:

		@staticmethod
		def list_datastore_keys( ):
			pass # TODO

		@staticmethod
		def get_universe_datastore( ):
			pass # TODO

		@staticmethod
		def list_keys_in_datastore( ):
			pass # TODO

		@staticmethod
		def get_data_from_datastore( ):
			pass # TODO

		@staticmethod
		def set_data_in_datastore( ):
			pass # TODO

		@staticmethod
		def remove_data_with_key_from_datastore( ):
			pass # TODO

		@staticmethod
		def clear_datastore( ):
			pass # TODO

	class PlacePublishing:

		@staticmethod
		def publish_async( ) -> None:
			pass # TODO
