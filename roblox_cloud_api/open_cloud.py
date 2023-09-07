
import os
import time

from typing import Any
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
	'''
	Open Cloud API for the Roblox Platform
	- MessagingService
	- DataStores
	- Publishing Places
	- Operations
	'''

	class MessagingService:
		'''
		MessagingService API for Roblox Open Cloud.
		'''

		@staticmethod
		def publish( auth : USER_ACCOUNT | API_KEY, universeId : int, topic : str, message : str ) -> None:
			'''
			Publish a message to the topic under MessagingService given a universeId.

			Note: if API_KEY is passed, it must have the permissions to publish messages in MessagingService to the specified universeId, which can be set on the open cloud credentials page.
			'''
			assert type(universeId) == int, "universeId must be an int."
			assert type(topic) == str, "topic must be a str."
			assert type(message) == str, "message must be a str."

			url = API_URLS.MESSAGING_SERVICE_API.format(universeId, topic)
			response = _RequestWrapper.post( auth, url, json={'message' : message} )
			if response.status_code != 200:
				raise Exception(f"MessagingService - { response.status_code } - Attempted Publish Message - {response.reason}")

	class Operations:
		'''
		Operations API for Open Cloud

		Operations tell you the status of a in-progress upload of an asset.
		'''

		class Internal:

			@staticmethod
			def was_operation_moderation_successful( operation_data : dict ) -> bool | None:
				try:
					state = operation_data.get("moderationResult").get("moderationState")
					return (state == "ModerationSuccess")
				except:
					pass
				return None

		@staticmethod
		def get_operation_id_status( auth : API_KEY | USER_ACCOUNT, operation_id : str ) -> tuple[OPERATION_STATUS, Any]:
			'''
			Get the status of an operation
			-> structs.OPERATION_STATUS
			'''
			try:
				url = API_URLS.OPERATIONS_STATUS_API.format(operation_id)
				response = _RequestWrapper.get(auth, url)
			except Exception as exception:
				return (OPERATION_STATUS.Exception, exception)
			if response.status_code != 200:
				return (OPERATION_STATUS.Unavailable, response.reason)

			try:
				data = response.json()
				moderation_passed = OpenCloudAPI.Operations.Internal.was_operation_moderation_successful( data )
				if moderation_passed == None:
					raise Exception("Moderation result could not be found in response.")
				if moderation_passed == False:
					return (OPERATION_STATUS.Moderated, None)
				if data.get("done") == True:
					return (OPERATION_STATUS.Success, data)
			except Exception as exception:
				return (OPERATION_STATUS.Exception, exception)
			return (OPERATION_STATUS.Waiting, None)

		@staticmethod
		def bulk_await_operations_completion( auth : API_KEY | USER_ACCOUNT, operation_ids : list[str] ) -> dict[str : tuple]:
			'''
			Await for all the passed operations to complete.
			Returns a list of operation statuses and data related to it.
			'''
			results = { }
			start_t = time.time()
			timeout_t = start_t + 15
			operation_ids = operation_ids.copy() # don't want to edit the original list

			while len(operation_ids) > 0:
				# check all active operations
				index = 0
				while index < len(operation_ids):
					op_id = operation_ids[index]
					state = OpenCloudAPI.get_operation_id_status( auth, op_id )
					if state[0] == OPERATION_STATUS.Waiting:
						# not ready yet
						index += 1
					else:
						# finished
						results[ str(op_id) ] = state
						operation_ids.pop( index )

				# check if loop ends
				if time.time() > timeout_t:
					break
				dur = round(timeout_t - time.time(), 2)
				print(f"Time remaining before timeout: { dur }")
				time.sleep(0.25)

			dur = round( time.time() - start_t, 2)
			print(f"Operations completed after { dur } seconds.")
			return results

	class Assets:

		@staticmethod
		def upload_and_return_operation_id(  ):
			raise NotImplementedError

		@staticmethod
		def bulk_upload_and_return_operation_ids( ):
			raise NotImplementedError

		@staticmethod
		def bulk_upload_assets( ):
			raise NotImplementedError

		@staticmethod
		def get_mesh_id_from_mesh_asset_id( auth : API_KEY | USER_ACCOUNT, asset_id : int ) -> int | None:
			pass

		@staticmethod
		def get_image_id_from_decal_id( auth : API_KEY | USER_ACCOUNT, asset_id : int ) -> int | None:
			pass

	class DataStores:
		'''
		CURRENTLY UNAVAILABLE - api.roblox.com was sunsetted
		https://create.roblox.com/docs/reference/cloud/datastores-api/v1
		'''

		@staticmethod
		def list_universe_datastores( auth : USER_ACCOUNT | API_KEY, universeId : int ) -> list:
			raise NotImplementedError
			# assert type(universeId) == int, "universeId must be an int."

			# url = API_URLS.STANDARD_DATASTORE_URL.format(universeId),
			# session = _RequestWrapper.build_session( auth )
			# datastores = []
			
			# cursor=""
			# while True:
			# 	data = session.get(url).json()
			# 	datastores.extend( data.get('datastores') )
			# 	cursor = data.get('nextPageCursor')
			# 	if cursor == "":
			# 		break

			# return datastores

		@staticmethod
		def list_datastore_items( auth : USER_ACCOUNT | API_KEY, universeId : int, datastoreName : str, maxItems=-1 ) -> list[tuple]:
			raise NotImplementedError
			# assert type(universeId) == int, "universeId must be an int."
			# assert type(datastoreName) == str, "datastoreName must be a str."
			
			# url = API_URLS.STANDARD_DATASTORE_URL.format(universeId) + "/datastore/entries"
			# session = _RequestWrapper.build_session( auth )

			# keys = []

			# cursor=""
			# while True:
			# 	params = { 'datastoreName' : datastoreName, 'cursor' : cursor, 'prefix' : '', 'allScopes' : True, 'limit' : 100 }
			# 	data = session.get(url, params=params).json()
			# 	print(data)
			# 	# for key in data.get('keys'):
			# 	# 	keys.append( key.get('key') )
			# 	cursor = data.get('nextPageCursor')
			# 	if cursor == "":
			# 		break

			# return keys

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

	class PlacePublish:

		@staticmethod
		def publish( auth : USER_ACCOUNT | API_KEY, universeId : int, placeId : int, filepath : str, versionType="Published" ) -> dict:
			assert type(universeId) == int, "universeId must be an int."
			assert type(placeId) == int, "placeId must be an int."
			assert type(filepath) == str, "filepath must be a str."

			if not os.path.exists(filepath):
				raise FileNotFoundError(f'{filepath} does not exist.')

			filename = os.path.split(filepath)[1]

			is_rbxlx = filename.endswith(".rbxlx")
			assert filename.endswith(".rbxl") or is_rbxlx, "Invalid filepath, must be an rbxl or rbxlx file."

			with open(filepath, 'rb') as file:
				data = file.read()

			url = API_URLS.UNIVERSE_VERSIONS_API.format(universeId, placeId)
			content_type = is_rbxlx and 'application/xml' or 'application/octet-stream'

			session = _RequestWrapper.build_session( auth )
			session.headers.update({'Content-Type' : content_type})
			response : Response = session.post( auth, url, params={'versionType' : versionType}, data=data )
			if response.status_code != 200:
				raise Exception(f"PlacePublish - { response.status_code } - Attempted Upload - {response.reason}")

			return response.json()
