
from functools import (
	partial,
	lru_cache,
	cache
)

from requests import Response

from .common import (
	ASSET_TYPES,
	OPERATION_STATUS,
	ASSET_FILE,
	API_KEY,
	USER_ACCOUNT,
	API_URLS,
	_RequestWrapper
)

class OpenCloudAPI:

	class MessagingService:
		'''
		MessagingService API for Roblox Open Cloud.
		Contains all the webpoints for Open Cloud.
		'''

		@staticmethod
		def publish_async( owner : USER_ACCOUNT | API_KEY, universeId : int, topic : str, message : str ) -> None:
			'''
			Publish a message to the topic under the MessagingService.

			Note: if API_KEY is passed, it must have the permissions to send messages in MessagingService to the specified universeId, which can be set on the open cloud credentials page.
			'''
			assert type(universeId) == int, "Passed universeId must be an int."
			assert type(topic) == str, "Passed topic must be an str."
			assert type(message) == str, "Passed message must be an str."

			response = _RequestWrapper.post(
				owner,
				API_URLS.MESSAGING_SERVICE_API.format(universeId, topic),
				json = {'message' : message}
			)

			if type(response) == Exception:
				raise response

			if response.status_code != 200:
				raise Exception(f"MessagingService - { response.status_code } - Attempted Publish Message - {response.reason}")

	class Operations:

		@staticmethod
		def get_operation_id_status( ):
			raise NotImplementedError

		@staticmethod
		def bulk_await_operations_completion( ):
			raise NotImplementedError

	class Assets:

		@staticmethod
		def upload_and_return_operation_id(  ):
			raise NotImplementedError

		@staticmethod
		def bulk_upload_and_return_operation_ids( ):
			raise NotImplementedError

		@staticmethod
		def bulk_upload_assets():
			raise NotImplementedError

	class DataStores:

		@staticmethod
		def list_datastore_keys( ):
			raise NotImplementedError

		@staticmethod
		def get_universe_datastore( ):
			raise NotImplementedError

		@staticmethod
		def list_keys_in_datastore( ):
			raise NotImplementedError

		@staticmethod
		def get_data_from_datastore( ):
			raise NotImplementedError

		@staticmethod
		def set_data_in_datastore( ):
			raise NotImplementedError

		@staticmethod
		def remove_data_with_key_from_datastore( ):
			raise NotImplementedError

		@staticmethod
		def clear_datastore( ):
			raise NotImplementedError

	class PlacePublishing:

		@staticmethod
		def publish_async( ) -> None:
			raise NotImplementedError
