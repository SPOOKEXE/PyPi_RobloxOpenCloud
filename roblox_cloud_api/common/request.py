
from requests import Response, Session
from .structs import ( API_KEY, USER_ACCOUNT )

DEFAULT_USER_AGENT = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36'

class _RequestWrapper:

	@staticmethod
	def _build_session( owner : API_KEY | USER_ACCOUNT ) -> Session:
		assert isinstance( owner, USER_ACCOUNT ) or isinstance( owner, API_KEY ), "Passed USER_ACCOUNT/API_KEY is not valid, inherit from or use these classes directly."

		sess = Session()
		sess.headers.update({'User-Agent' : DEFAULT_USER_AGENT})
		if isinstance( owner, API_KEY ):
			sess.headers.update({"x-api-key" : owner.api_key })
		elif isinstance( owner, USER_ACCOUNT ):
			sess.cookies.set(".ROBLOSECURITY", owner.cookie)
		return sess

	@staticmethod
	def get( owner : API_KEY | USER_ACCOUNT, url : str, *args, **kwargs ) -> Response:
		s = _RequestWrapper._build_session( owner )
		try:
			return s.get( url, *args, **kwargs )
		except Exception as exception:
			raise exception

	@staticmethod
	def post( owner : API_KEY | USER_ACCOUNT, url : str, *args, **kwargs ) -> Response:
		s = _RequestWrapper._build_session( owner )
		try:
			return s.post( url, *args, **kwargs )
		except Exception as exception:
			raise exception
