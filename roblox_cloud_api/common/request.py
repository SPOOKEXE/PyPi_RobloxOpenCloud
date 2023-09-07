
from requests import Response, Session
from .structs import ( API_KEY, USER_ACCOUNT )

DEFAULT_USER_AGENT = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36'

class _RequestWrapper:
	'''
	Requests utility for ANY api calls to Roblox via API_KEY or USER_ACCOUNT.

	Contains methods to call.
	'''

	@staticmethod
	def build_session( auth : API_KEY | USER_ACCOUNT ) -> Session:
		'''
		Build a requests session to be used with an API call
		'''
		assert isinstance( auth, USER_ACCOUNT ) or isinstance( auth, API_KEY ), "USER_ACCOUNT/API_KEY is not valid, inherit from or use these classes directly."
		sess = Session()
		sess.headers.update({'User-Agent' : DEFAULT_USER_AGENT})
		auth.append_auth( sess )
		return sess

	@staticmethod
	def get( auth : API_KEY | USER_ACCOUNT, url : str, *args, **kwargs ) -> Response:
		'''
		Get request using an API_KEY / USER_ACCOUNT.
		- Syntax Sugar
		'''
		return _RequestWrapper.build_session( auth ).get( url, *args, **kwargs )

	@staticmethod
	def post( auth : API_KEY | USER_ACCOUNT, url : str, *args, **kwargs ) -> Response:
		'''
		Post request using an API_KEY / USER_ACCOUNT.
		- Syntax Sugar
		'''
		return _RequestWrapper.build_session( auth ).post( url, *args, **kwargs )

