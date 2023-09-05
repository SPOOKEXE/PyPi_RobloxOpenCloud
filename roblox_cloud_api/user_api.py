
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

class UserAPI:

	@staticmethod
	def get_user_id_from_cookie( cookie : str ) -> int:
		'''
		Get the user id of the given cookie in the user account.

		Returns -1 if the cookie is invalid.
		'''
		r : dict = _RequestWrapper.get( USER_ACCOUNT(cookie=cookie), API_URLS.ACCOUNT_AUTHENTICATED_URL ).json()
		if 'errors' in r.keys():
			return -1
		return r["id"]

	@staticmethod
	def is_user_account_valid( account : USER_ACCOUNT ) -> bool:
		'''
		Check if the account's cookie is valid by getting their user id via web-apis.
		'''
		return UserAPI.get_user_id_from_cookie(account.cookie) != -1
